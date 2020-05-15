---
title: "Data Preparation"
date: 2020-04-27T08:58:06-06:00
weight: 15
---

Now that you're connected to your Jupyter notebook, let's prepare a data set for processing.  We're going to tackle the customer churn prediction problem found in this [SageMaker example](https://github.com/awslabs/amazon-sagemaker-examples/blob/master/introduction_to_applying_machine_learning/xgboost_customer_churn/xgboost_customer_churn.ipynb), except we're going to use a neural network in TensorFlow rather than XGBoost.

## S3 bucket

We need an S3 bucket to store our training data.  Making sure that you're working in the same region as your EKS cluster, run:

    aws s3 mb s3://<BUCKET>

Choose an appropriate name in place of `<BUCKET>`.

## IAM permissions

We need to give our EKS nodes permission to use the S3 bucket we just made.  We do this by associating an IAM policy to the IAM role that `eksctl` created for the nodes.

First, create the following IAM policy in the AWS IAM console.  Name it `smoperators-s3`.  Be sure to replace the value `BUCKET` with the name of the S3 bucket you just created.

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": [
                    "s3:PutObject",
                    "s3:GetObject",
                    "s3:ListBucket",
                    "s3:PutObjectTagging"
                ],
                "Resource": [
                    "arn:aws:s3:::BUCKET/*",
                    "arn:aws:s3:::BUCKET"
                ]
            },
            {
                "Sid": "VisualEditor1",
                "Effect": "Allow",
                "Action": "s3:HeadBucket",
                "Resource": "*"
            }
        ]
    }

Now find the IAM role whose name starts with `eksctl-eks-kubeflow-nodegroup`.  Add the new policy to this role.  

## Python modules

Before running a notebook, we'll install the `boto3` module so that we can work with S3 through the Python SDK.  In your notebook, click `New -> Terminal`.  In the new terminal window, enter:

    pip install --user boto3 pandas numpy sklearn

## Data preparation

Next, download the [example notebook](/files/customer_churn_tf.ipynb).  In your notebook, click `Upload` and select this notebook.  Click `Upload` again to complete the upload.

Now click the imported notebook to open it.  Read through and execute each cell in the notebook, making sure to edit the `bucket` and `prefix` variables in the first code cell.

After you finish executing this notebook, you'll have train, validation, and test data sets stored in S3.
