---
title: "Image Classification"
chapter: false
weight: 140 
---

In this section, we will use the Amazon SageMaker image classification algorithm to train on the [cifar10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html). 

The Amazon SageMaker image classification algorithm is a supervised learning algorithm that supports multi-label classification. It takes an image as input and outputs one or more labels assigned to that image. It uses a convolutional neural network (ResNet) that can be trained from scratch or trained using transfer learning when a large number of training images are not available.

To train a model in Amazon SageMaker, you can use either the `Amazon SageMaker Python SDK` or the `AWS SDK for Python (Boto 3)`. In the last two labs, we used `AWS SDK for Python (Boto 3)` to train the model. In this lab, you will use the Boto 3 to train the model. Amazon SageMaker uses the `CreateTrainingJob API` to run the training.


1. Access the SageMaker Studio you opened earlier.
2. On the left sidebar, navigate into `MLAI/built-in-algorithm` , double click on `cifar10.ipynb` to open it.
3. You are now ready to begin the notebook.
4. Run each cell of the notebook.

Please notice that you can still see the progress of your training job and the metrics, even though you have not setup the experiment in the notebook when you built the estimator. You can click on the `Unassigned trial component` section of the `SageMaker Experiment List` tab in the left sidebar.
![Experiment unassigned image](/images/1experimentunassigned.png)
Then, you can right click on the training job and either deploy it with one click or check the details of the training.
![Experiment training list](/images/1traininglist.png)

You can see the details of training such as charts (e.g. validation accuracy per epoch), metrics, parameters, etc.
![Experiment training details](/images/1trainingdetails.png)
