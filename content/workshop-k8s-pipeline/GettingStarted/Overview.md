---
title: "Overview"
date: 2020-04-28T09:16:41-06:00
weight: 5
---

This [blog post](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-sagemaker-components-for-kubeflow-pipelines/) gives a good summary of how the SageMaker components for Kubeflow Pipelines will help your data science teams.

> Kubeflow is a popular open-source machine learning (ML) toolkit for Kubernetes users who want to build custom ML pipelines.  Kubeflow Pipelines is an add-on to Kubeflow that lets you build and deploy portable and scalable end-to-end ML workflows. However, when using Kubeflow Pipelines, data scientists still need to implement additional productivity tools such as data-labeling workflows and model-tuning tools.
>
> Additionally, with Kubeflow Pipelines, ML ops teams need to manage a Kubernetes cluster with CPU and GPU instances, and keep its utilization high at all times to provide the best return on investment. Maximizing the utilization of a cluster across data science teams is challenging and adds operational overhead to the ML ops teams. For example, you should restrict GPU instances to demanding tasks such as deep learning training and inference, and use CPU instances for the less demanding tasks such data preprocessing and running essential services such as Kubeflow Pipeline control plane.
> 
> As an alternative, with Amazon SageMaker Components for Kubeflow Pipelines, you can take advantage of powerful Amazon SageMaker features such as fully managed services, including data labeling, large-scale hyperparameter tuning and distributed training jobs, one-click secure and scalable model deployment, and cost-effective training through Amazon Elastic Compute Cloud (Amazon EC2) Spot Instances.

In this workshop, we're going to perform image classification tasks on the [MNIST](http://yann.lecun.com/exdb/mnist/) dataset.  The example is based on this [SageMaker example notebook](https://github.com/awslabs/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/1P_kmeans_highlevel/kmeans_mnist.ipynb).

Specifically, we'll use a Kubeflow pipeline with the SageMaker components to perform these tasks:

* Pre-process the data set to convert it into the format we need for ML training
* Run a hyperparameter optimization job to find the optimal set of hyperparameters
* Train our model
* Deploy the model for real-time inference
* Get batch inferences

![Machine Learning Pipeline with Kubeflow and SageMaker](/images/pipeline/sagemaker-kf.png)

