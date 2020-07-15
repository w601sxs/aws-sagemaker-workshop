---
title: "Real Time Inference"
date: 2020-04-28T09:16:41-06:00
weight: 35
---

The pipeline also deployed an inference endpoint.  In the SageMaker console, go to the _Endpoints_ section and note the name of the deployed endpoint.  We'll refer to this as `ENDPOINT` going forward.

![Endpoint](/images/pipeline/endpoint.png)

In order to test the endpoint, first download the MNIST data set archive.

    aws s3 cp s3://sagemaker-sample-data-us-east-1/algorithms/kmeans/mnist/mnist.pkl.gz .

Now download the [inference script](/files/pipeline/inference.py).  On line 8, insert the name of your `ENDPOINT`.  

Run the script.  Note that you'll need the Numpy module installed in your Python environment.  The script will call the inference endpoint for one record from the training data and print the output.

    $ python inference.py

    {'predictions': [{'distance_to_cluster': 7.269891262054443, 'closest_cluster': 8.0}]}
