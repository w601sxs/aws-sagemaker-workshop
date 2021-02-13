---
title: "Img Classification-Debugger"
chapter: false
weight: 260
---

## Amazon SageMaker Debugger

Amazon SageMaker Debugger helps you to debug machine learning models during training by identifying and detecting problems with the models in near real-time.

### How does Amazon SageMaker Debugger work

Amazon SageMaker Debugger lets you go beyond just looking at scalars like losses and accuracies during training and gives you full visibility into all tensors 'flowing through the graph' during training. Furthermore, it helps you monitor your training in near real-time using rules and provides you alerts, once it has detected inconsistency in training flow.

### Concepts

* **Tensors**: These represent the state of the training network at intermediate points during its execution
* **Debug Hook**: Hook is the construct with which Amazon SageMaker Debugger looks into the training process and captures the tensors requested at the desired step intervals
* **Rule**: A logical construct, implemented as Python code, which helps analyze the tensors captured by the hook and report anomalies, if at all

With these concepts in mind, let's understand the overall flow of things that Amazon SageMaker Debugger uses to orchestrate debugging

### Saving tensors during training

The tensors captured by the debug hook are stored in the S3 location specified by you.
As we are using the Amazon SageMaker provided TensorFlow container, we don't need to make any changes to our training script for the tensors to be stored. Amazon SageMaker Debugger will use the configuration you provide through Amazon SageMaker SDK's Tensorflow `Estimator` when creating your job to save the tensors in the fashion you specify.

To run this lab:

1. Access the SageMaker studio you started earlier.
2. On the left sidebar, navigate into `MLAI/Script-mode/keras_cifar10_debugger` folder, double click on `TF_keras_CIFAR10_debugger.ipynb` to open it.
3. You are now ready to begin the notebook.
