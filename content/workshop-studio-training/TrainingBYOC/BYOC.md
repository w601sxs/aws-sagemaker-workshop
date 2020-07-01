---
title: "Bring Your Own Container"
chapter: false
weight: 305
---

### Bringing custom algorithms into Amazon SageMaker by using Containers

With Amazon SageMaker, you can package your own algorithm in a container that can then be used for model training, inference, and hyperparameter tuning. The following notebooks guide you through the process of building custom Docker containers that leverage the Scikit-Learn and TensorFlow frameworks. You will then use your custom containers for training and hyperparameter tuning with SageMaker.

By packaging an algorithm in a container, you can bring almost any code to the Amazon SageMaker environment, regardless of programming language, environment, framework, or dependencies.

Even in cases where SageMaker already provides direct SDK support (ex: an Estimator) for your desired environment or framework, you may find it more effective to build your own container.

Some of the reasons to build a container for a framework that is already support in SageMaker include:

1. You require a specific version of a framework that is not available in SageMaker
2. Your algorithm requires external dependencies and/or specific environment configuration
3. You would like to provide a custom hosting mechanism for your model
