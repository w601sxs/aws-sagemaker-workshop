---
title: "Network Improvements"
date: 2020-04-29T17:01:39-06:00
weight: 5
---

The model we used in the previous chapter is a simple fully connected network with three layers.  Here's the section of `tftab.py` that defines the layers:

    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(128, activation=tf.nn.relu),
        tf.keras.layers.Dense(128, activation=tf.nn.relu),
        tf.keras.layers.Dense(1)
    ])

Additionally, we did a lot of feature engineering in our Jupyter notebook.  That will complicate our use of the inference endpoint.  For example, rather than passing in `State = CO`, we need to understand which column of the transformed data set contains the equivalent one-hot encoded variable.

In the rest of this chapter, we'll make the following improvements to our TensorFlow model:

* Use TensorFlow feature columns that take the raw CSV data as input
* Add early stopping to our training job
* Add class weights to account for an imbalanced training set
* Add output bias
* Add dropout and batch normalization layers to improve fit and reduce overfitting
* Train for more epochs