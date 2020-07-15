+++
title = "Deep Learning Pipeline"
date = 2020-04-27T16:03:48-06:00
weight = 45
chapter = true
type = "mylayout"
+++

### Kubeflow Pipeline for Deep Learning

To date in this workshop, we've seen how to build and use a Kubeflow Pipeline for an image classification problem using SageMaker's built-in KMeans algorithm.  The pipeline had steps for hyperparameter optimization, training, batch inference, and model deployment for real-tine inference in a hosted endpoint. 

In this section, we'll use a similar process to classify the [CIFAR-10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html) using a deep learning network built in Keras.  This section will be more in-depth than the previous sections, and we'll dive a little deeper into the code.  However, note that this section requires the use of more powerful training instances with GPUs.  The cost will be higher if you are hosting this workshop in your own AWS account.  (As of June 2020, the on-demand cost for an _ml.m5.2xlarge_ instance in the _us-east-2_ region is $0.538 per hour, compared to $4.284 for a _p3.2xlarge_ instance.)  

This section is based on the blog post [Introducing Amazon SageMaker Components for Kubeflow Pipelines](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-sagemaker-components-for-kubeflow-pipelines/).  We will make a few minor changes to the code provided by this blog post.
