---
title: "Training"
date: 2020-04-27T11:35:49-06:00
weight: 5
---

Let's manually run a SageMaker training job using the SageMaker training job operator.

## Save the TensorFlow script

Download the [training and serving script](/files/tftab.py).  Create a gzipped tar file with this script, and upload it to your S3 bucket.  In the snippet below, `JOBNAME` is a training job identifier that you define, such as `tf-churn-2020-04-01`.

    tar cvf sourcedir.tar tftab.py
    gzip sourcedir.tar
    aws s3 cp sourcedir.tar.gz s3://BUCKET/JOBNAME/source/sourcedir.tar.gz

## Create an IAM role for training

We need an IAM role for our training job to use.

* Go to the IAM console.
* Go to the `Roles` section.
* Click `Create role`.
* Select `AWS service` and for the entity set the service to `SageMaker`.
* Call the role `sm-job-role`.
* Click `Create role`.
* Note the ARN of the new role.
* After the role is created, attach the policy `smoperators-s3`.

## Create training job definition

Download the [template job definition](/files/tf-job.yaml) and make the following changes:

* Lines 4 and 14: Give your job a unique name
* Line 8: Change the S3 path to `s3://BUCKET/JOBNAME/model`
* Lines 20 and 27: Set the correct region
* Line 22: Set the S3 path to `s3://BUCKET/JOBNAME/source/sourcedir.tar.gz`
* Line 24: Set the URI for the SageMaker TensorFlow image.  This will normally be `763104351884.dkr.ecr.REGION.amazonaws.com/tensorflow-training:2.1.0-gpu-py3`.
* Line 26: Set the ARN you noted in the previous step.
* Line 29: Change the S3 path to `s3://BUCKET/JOBNAME/out/`
* Line 41: Set the S3 path to where you saved the data sets in your Jupyter notebook

You'll notice on line 32 that we use an `ml.m5.xlarge` instance, which does not have a GPU.  Normally with TensorFlow we'd want to use GPU-powered instances, but new AWS accounts often have limits on using GPU instances.

## Execute training job 

Run:

    kubectl apply -f tf-job.yaml

## Monitor training job

You can list all training jobs:

    kubectl get TrainingJob

You'll see the job status in the output of that command.  You can get more details on a job by describing it:

    kubectl describe trainingjob <JOBNAME>

To see the full logs from the job:

    kubectl smlogs trainingjob <JOBNAME>


