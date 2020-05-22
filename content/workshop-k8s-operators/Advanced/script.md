---
title: "Training Script"
date: 2020-04-29T17:19:53-06:00
weight: 25
---

Let's walk through some of the improvements to the [training script](/files/tftab-advanced.py).

## Hyperparameters

We've added three extra hyperparameters.  Besides the learning rate, we have epochs, output bias, and the number of positive and negative samples in the data set.  These hyperparameters will help us improve accuracy and deal with an imbalanced data set, as we'll see in the next section.

    parser.add_argument('--learning_rate', type=float, default=0.001)
    parser.add_argument('--output_bias', type=float, default=0)
    parser.add_argument('--num_positive', type=float, default=0)
    parser.add_argument('--num_negative', type=float, default=0)
    parser.add_argument('--epochs', type=int, default=20)

Recall that we calculated the `bias` and number of positive and negative samples in the notebook in the last section.

## Dealing with imbalanced data set

Often with binary classification problems we find that one class is much more common than the other.  To help account for this, we will add an output bias and class weights to our model.

    if output_bias is not None:
        output_bias = tf.keras.initializers.Constant(output_bias)

We'll add this bias to our final layer.

    tf.keras.layers.Dense(1, bias_initializer=output_bias)

Next we'll calculate class weights for each class.

    total = neg + pos
    weight_for_0 = (1 / neg)*(total)/2.0 
    weight_for_1 = (1 / pos)*(total)/2.0
    class_weight = {0: weight_for_0, 1: weight_for_1}
    
We use the class weights during model fitting.

    model.fit(ds_train, validation_data=ds_test, 
            ...,
             class_weight=class_weight)

## Using feature columns

TensorFlow feature columns help us with common data transformations.  In this data set, we use feature columns to calculate embeddings for high-cardinality categorical variables.

    # embeddings
    stateC = feature_column.categorical_column_with_vocabulary_list(
      'State', ['KS', 'OH', 'NJ', 'OK', 'AL', 'MA', 'MO', 'LA', 'WV', 'IN', 'RI',
           'IA', 'MT', 'NY', 'ID', 'VT', 'VA', 'TX', 'FL', 'CO', 'AZ', 'SC',
           'NE', 'WY', 'HI', 'IL', 'NH', 'GA', 'AK', 'MD', 'AR', 'WI', 'OR',
           'MI', 'DE', 'UT', 'CA', 'MN', 'SD', 'NC', 'WA', 'NM', 'NV', 'DC',
           'KY', 'ME', 'MS', 'TN', 'PA', 'CT', 'ND'])
    stateF = feature_column.embedding_column(stateC, dimension=8)

We use simple one-hot encodings for low-cardinality categorical variables.
    
    # one-hot encodings
    areacodeC = feature_column.categorical_column_with_vocabulary_list(
      'AreaCode', [415, 408, 510])
    areacodeF = feature_column.indicator_column(areacodeC)
    
And for most of the numeric columns, we'll bucket them into categories according to the data distribution.  

    # bucketed ints
    acctC = feature_column.numeric_column("AccountLength")
    acctF = feature_column.bucketized_column(acctC, boundaries=[74,101,127,243])

Recall that in the notebook in the previous section, we calculated the percentiles of the numeric columns using the `describe` method for a Pandas dataframe.  As a start, we'll bucket according to the 25th, 50th, and 75th percentiles.

## Additional layers

We'll add a feature layer for the feature columns, and add dropout and batch normalization.  Our final network looks like this:

    feature_layer = tf.keras.layers.DenseFeatures([stateF,areacodeF,intplanF,vmPlanF,acctF,vmMsgF,dayMinsF,dayCallsF,eveMinsF,
                                                  eveCallsF,nightMinsF,nightCallsF,intMinsF,intCallsF,custCallsF])

    dropout_rate = 0.5
    model = tf.keras.models.Sequential([
      feature_layer,
      tf.keras.layers.Dropout(dropout_rate),
      tf.keras.layers.BatchNormalization(),
      tf.keras.layers.Dense(128, activation=tf.nn.relu),
      tf.keras.layers.Dropout(dropout_rate),
      tf.keras.layers.BatchNormalization(),
      tf.keras.layers.Dense(128, activation=tf.nn.relu),
      tf.keras.layers.Dropout(dropout_rate),
      tf.keras.layers.BatchNormalization(),
      tf.keras.layers.Dense(1, bias_initializer=output_bias)
    ])

## Early stopping and additional epochs

While training, we want to run for more epochs to improve accuracy.  But we'll stop if the validation loss stops improving.

    # early stopping
    cb = tf.keras.callbacks.EarlyStopping(
        monitor='val_loss', min_delta=0.01, patience=5, mode='auto'
    )

    model.fit(ds_train, validation_data=ds_test, 
              callbacks=[cb],
              epochs=epochs,
             class_weight=class_weight)