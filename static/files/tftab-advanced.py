# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.import tensorflow as tf

import tensorflow as tf
from tensorflow import feature_column
import argparse
import os
import numpy as np
import json
import pandas as pd

def model(ds_train, ds_test, output_bias=None, lr=0.001, neg, pos, epochs=20):
    
    if output_bias is not None:
        output_bias = tf.keras.initializers.Constant(output_bias)
    
    # embeddings
    stateC = feature_column.categorical_column_with_vocabulary_list(
      'State', ['KS', 'OH', 'NJ', 'OK', 'AL', 'MA', 'MO', 'LA', 'WV', 'IN', 'RI',
           'IA', 'MT', 'NY', 'ID', 'VT', 'VA', 'TX', 'FL', 'CO', 'AZ', 'SC',
           'NE', 'WY', 'HI', 'IL', 'NH', 'GA', 'AK', 'MD', 'AR', 'WI', 'OR',
           'MI', 'DE', 'UT', 'CA', 'MN', 'SD', 'NC', 'WA', 'NM', 'NV', 'DC',
           'KY', 'ME', 'MS', 'TN', 'PA', 'CT', 'ND'])
    stateF = feature_column.embedding_column(stateC, dimension=8)
    
    # one-hot encodings
    areacodeC = feature_column.categorical_column_with_vocabulary_list(
      'AreaCode', [415, 408, 510])
    areacodeF = feature_column.indicator_column(areacodeC)
    intplanC = feature_column.categorical_column_with_vocabulary_list(
      "IntlPlan", ['no','yes'])
    intplanF = feature_column.indicator_column(intplanC)
    vmPlanC = feature_column.categorical_column_with_vocabulary_list(
      "VMailPlan", ['no','yes'])
    vmPlanF = feature_column.indicator_column(vmPlanC)
    
    # bucketed ints
    acctC = feature_column.numeric_column("AccountLength")
    acctF = feature_column.bucketized_column(acctC, boundaries=[74,101,127,243])
    vmMsgC = feature_column.numeric_column("VMailMessage")
    vmMsgF = feature_column.bucketized_column(vmMsgC, boundaries=[0,20,51])
    dayMinsC = feature_column.numeric_column("DayMins")
    dayMinsF = feature_column.bucketized_column(dayMinsC, boundaries=[143,179,216,350])
    dayCallsC = feature_column.numeric_column("DayCalls")
    dayCallsF = feature_column.bucketized_column(dayCallsC, boundaries=[87,101,114,165])
    eveMinsC = feature_column.numeric_column("EveMins")
    eveMinsF = feature_column.bucketized_column(eveMinsC, boundaries=[166,201,235,364])
    eveCallsC = feature_column.numeric_column("EveCalls")
    eveCallsF = feature_column.bucketized_column(eveCallsC, boundaries=[87,100,114,170])
    nightMinsC = feature_column.numeric_column("NightMins")
    nightMinsF = feature_column.bucketized_column(nightMinsC, boundaries=[167,201,235,395])
    nightCallsC = feature_column.numeric_column("NightCalls")
    nightCallsF = feature_column.bucketized_column(nightCallsC, boundaries=[87,100,113,175])
    intMinsC = feature_column.numeric_column("IntlMins")
    intMinsF = feature_column.bucketized_column(intMinsC, boundaries=[8,10,12,20])
    intCallsC = feature_column.numeric_column("IntlCalls")
    intCallsF = feature_column.bucketized_column(intCallsC, boundaries=[3,4,6,20])
    custCallsC = feature_column.numeric_column("CustServCalls")
    custCallsF = feature_column.bucketized_column(custCallsC, boundaries=[1,2,9])
    
    # all features
    feature_layer = tf.keras.layers.DenseFeatures([stateF,areacodeF,intplanF,vmPlanF,acctF,vmMsgF,dayMinsF,dayCallsF,eveMinsF,
                                                  eveCallsF,nightMinsF,nightCallsF,intMinsF,intCallsF,custCallsF])
    
    # early stopping
    cb = tf.keras.callbacks.EarlyStopping(
        monitor='val_loss', min_delta=0.01, patience=5, mode='auto'
    )
    
    # class weights
    total = neg + pos
    weight_for_0 = (1 / neg)*(total)/2.0 
    weight_for_1 = (1 / pos)*(total)/2.0
    class_weight = {0: weight_for_0, 1: weight_for_1}
    
    # model
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

    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=lr),
                  loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    model.fit(ds_train, validation_data=ds_test, 
              callbacks=[cb],
              epochs=epochs,
             class_weight=class_weight)

    r = model.evaluate(ds_test)
    print(f"Loss={r[0]},accuracy={r[1]}")
    
    return model

def df_to_dataset(dataframe, shuffle=True, batch_size=32):
    dataframe = dataframe.copy()
    labels = dataframe.pop('Churn')
    ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
    if shuffle:
        ds = ds.shuffle(buffer_size=len(dataframe))
        ds = ds.batch(batch_size)
    return ds

def _load_training_data(base_dir):

    train = pd.read_csv(os.path.join(base_dir, 'train_data.csv'))
    print(train.dtypes)

    return df_to_dataset(train)


def _load_testing_data(base_dir):
                        
    val = pd.read_csv(os.path.join(base_dir, 'validation_data.csv'))

    return df_to_dataset(val)

def _parse_args():
    parser = argparse.ArgumentParser()

    # Data, model, and output directories
    # model_dir is always passed in from SageMaker. By default this is a S3 path under the default bucket.
    parser.add_argument('--model_dir', type=str)
    parser.add_argument('--sm-model-dir', type=str, default=os.environ.get('SM_MODEL_DIR'))
    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAINING'))
    parser.add_argument('--hosts', type=list, default=json.loads(os.environ.get('SM_HOSTS')))
    parser.add_argument('--current-host', type=str, default=os.environ.get('SM_CURRENT_HOST'))

    # Hyperparameters
    parser.add_argument('--learning_rate', type=float, default=0.001)
    parser.add_argument('--output_bias', type=float, default=0)
    parser.add_argument('--num_positive', type=float, default=0)
    parser.add_argument('--num_negative', type=float, default=0)
    parser.add_argument('--epochs', type=int, default=20)

    return parser.parse_known_args()


if __name__ == "__main__":
    args, unknown = _parse_args()

    train_ds = _load_training_data(args.train)
    eval_ds = _load_testing_data(args.train)

    tab_classifier = model(train_ds, eval_ds, output_bias=args.output_bias, lr=args.learning_rate, neg=args.num_negative, pos=args.num_positive, epochs=args.epochs)

    if args.current_host == args.hosts[0]:
        # save model to an S3 directory with version number '00000001'
        tab_classifier.save(os.path.join(args.sm_model_dir, '000000001'), 'tab_model.h5')
