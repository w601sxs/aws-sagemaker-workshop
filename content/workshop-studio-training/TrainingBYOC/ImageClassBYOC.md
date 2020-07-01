---
title: "Image Classification"
chapter: false
weight: 315 
---

### Building your own TensorFlow container

Much like the previous `House Price Prediction` lab in which you built a custom container for a Scikit-Learn algorithm, in this lab you will be building a custom Tensorflow-based container that will be used for image classification. Also, you will call AWS CodeBuild from the notebook to build and push the Docker Image.

Let's open our notebook and begin the lab:

1. Access the SageMaker Studio instance you created earlier.
2. On the left sidebar, click the Folder icon and navigate into the `MLAI/BYOC/TF_bring_your_own` folder. Double-click on `tensorflow_bring_your_own.ipynb` to open it.
3. You are now ready to begin the notebook. Follow through the provided steps to build your custom container, and then leverage it for training in SageMaker.
