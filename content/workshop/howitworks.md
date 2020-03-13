---
title: "How Amazon SageMaker Autopilot works"
chapter: true
weight: 2
description: "Learn how Sagemaker Autopilot Works"
---

![How it works](/images/autopilot-how-it-works.png)

Using a single API call, or a few clicks in [Amazon SageMaker Studio](https://aws.amazon.com/blogs/aws/amazon-sagemaker-studio-the-first-fully-integrated-development-environment-for-machine-learning/), SageMaker Autopilot first inspects your data set, and runs a number of candidates to figure out the optimal combination of data preprocessing steps, machine learning algorithms and hyperparameters. Then, it uses this combination to train an [Inference Pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipelines.html), which you can easily deploy either on a real-time endpoint or for batch processing. As usual with Amazon SageMaker, all of this takes place on fully-managed infrastructure.

Last but not least, SageMaker Autopilot also generate Python code showing you exactly how data was preprocessed: not only can you understand what SageMaker Autopilot did, you can also reuse that code for further manual tuning if you’re so inclined.

As of today, SageMaker Autopilot supports:

- Input data in tabular format, with automatic data cleaning and preprocessing,
- Automatic algorithm selection for linear regression, binary classification, and multi-class classification,
- Automatic hyperparameter optimization,
- Distributed training,
- Automatic instance and cluster size selection.

Also see these links for a walkthrough for what we will be doing today:

- [AutoML with SageMaker Part 1](https://www.youtube.com/watch?v=qMEtqJPhqpA)
- [AutoML with SageMaker Part 2](https://www.youtube.com/watch?v=WsfRAeGzgm8)
- [AutoML with SageMaker Part 3](https://www.youtube.com/watch?v=KZSTsWrDGXs)




