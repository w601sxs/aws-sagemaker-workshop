---
title: "Training with your own script"
chapter: false
weight: 205
---


### Submit custom code to train with deep learning frameworks (Script mode)

You can use Amazon SageMaker to train models using your custom codes (script). Amazon SageMaker makes extensive use of Docker containers for training. You can put scripts, algorithms, and inference code for your machine learning models into containers. Amazon SageMaker provides some prebuilt containers that you can add your script into it without having to worry about building containers or managing the underlying infrastructure.

Amazon SageMaker provides prebuilt deep learning frameworks and machine learning libraries such as:

* TensorFlow
* PyTorch
* Apache MXNet
* scikit-learn
* SparkML

 You can train your models with your custom code (script) on SageMaker using these containers. Script mode enables you to use Amazon SageMaker prebuilt containers to train your models with the same kind of training script you would use outside SageMaker.

To train a model in script mode, you create a training job with the following information:

* The URL of the Amazon S3 bucket where you've stored the training data.
* The compute resources that you want Amazon SageMaker to use for model training.
* The URL of the S3 bucket where you want to store the output of the job.
* The Amazon Elastic Container Registry (ECR) path of the AWS managed DL framework or Machine Learning library.
* The training scripts similar to those you would use outside SageMaker.

![Example image](/images/1scriptmode.png)

This section contains examples and related resources regarding Amazon SageMaker’s Script Mode.