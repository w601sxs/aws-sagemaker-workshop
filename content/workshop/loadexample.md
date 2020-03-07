---
title: "Load Autopilot Example"
chapter: true
weight: 4
description: Start by loading the AutoPilot example on SageMaker 
---

# Load AutoPilot Example


## Load Example on Sagemaker Studio

1. Navigate to the Commands tab - 4th icon on the left ( {{< fa palette >}} ) and click "Getting Started". 
![](/images/welcomestudio.png)

2. Then click "Create Autopilot Experiment" - you will see the following window:

![](/images/createauto.png)

- For ```Experiment name```, enter : Sagemaker-test-autopilot" or something similar

- For ```S3 location of input data```, enter : https://sagemaker-getting-started-data.s3.us-east-2.amazonaws.com/bank-additional-full.csv

- For ```Target attribute name```, enter : y

- And for ```S3 location of output data```, enter an s3 location within your account. To create an S3 bucket within your account, [use this link](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html). *Note* : please use ```us-east-2``` for "region" in step 4 of this guide. If you have an existing bucket in ```us-east-2``` that you would like to use, feel free to do so!

## Load Example on Sagemaker Notebook Instance

1. Once you open Jupyter on your SageMaker notebook instance, you can navigate to the "SageMaker examples" tab

![](/images/SagemakerExamples.png)

2. Expand the title "Autopilot" by clicking it, and then click "Use" 

![](/images/Use.png) 

3. This will open the Autopilot example:

![](/images/jupyterexample.png)

4. Make sure you change your Kernel to "Conda Python 3" if it isn't already set to that.

![](/images/changekernel.png)