---
title: "Overview"
date: 2020-04-28T09:16:41-06:00
weight: 5
---

The machine learning (ML) workflow is an iterative process involving data collection and engineering, data science, and operations.

![Machine Learning Workflow](/images/sagemaker-k8s-overview.png)

In this workshop, we're going to use Kubeflow to provision Jupyter notebooks for interactive data exploration and model development.  Then we'll switch to SageMaker for model training and deployment, taking advantage of SageMaker's scaled-out training and hosted inference endpoints.  Those capabilities let us take advantage of more compute power, including GPUs, for training and hosting models, without having to scale out our kubernetes cluster for training and inference. 

![Machine Learning Workflow with Kubeflow and SageMaker](/images/sagemaker-k8s-svc.png)

In a nutshell, this workflow suits teams where kubernetes and Kubeflow are the hub for data teams, but want to take advantage of SageMaker's automation of the tough parts of ML model training and deployment.