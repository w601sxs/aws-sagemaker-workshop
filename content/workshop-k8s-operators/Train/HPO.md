---
title: "Hyper Parameter Optimization"
date: 2020-04-28T15:10:39-06:00
weight: 35
---

As we've seen, the performance of our very simple TensorFlow model is medicore.  While we should look at the basic network architecture and feature engineering, we can also look at tuning some hyperparameters like the learning rate.  SageMaker HPO helps find the best set of hyperparameters.

## Save the TensorFlow script

We need to make some changes to the TensorFlow script to accept learning rate as a parameter, and output the loss (error) as a recognizable metric.  

Download the [training and serving script](/files/tftab-lr.py).  Create a gzipped tar file with this script, and upload it to your S3 bucket.  In the snippet below, `BUCKET` is the name of your S3 bucket.

    tar cvf sourcedir.tar tftab-lr.py
    gzip sourcedir.tar
    aws s3 cp sourcedir.tar.gz s3://BUCKET/hpo/source/sourcedir.tar.gz

## Create training job definition

You'll see in the HPO job definition that we want to minimize the loss (error).  In a production case, you should consider which metric you want to minimize or maximize, and which hyperparameters you want to explore.

    hyperParameterTuningJobObjective:
      type: Minimize
      metricName: tferror

Download the [template job definition](/files/tf-hpo-job.yaml) and make the following changes:

* Lines 4 and 29: Give your job a unique name
* Lines 6 and 39: Set the correct region
* Lines 27 and 41 and 50 and 62: Set the bucket name
* Line 43: Set the URI for the SageMaker TensorFlow image.  This will normally be `763104351884.dkr.ecr.REGION.amazonaws.com/tensorflow-training:2.1.0-gpu-py3`.
* Line 48: Set the ARN, using the same ARN you used for the earlier training job

## Execute training job 

Run:

    kubectl apply -f tf-hpo-job.yaml

## Monitor training job

You can list all HPO jobs:

    kubectl get hyperparametertuningjob

You'll see the job status in the output of that command.  You can get more details on a job, including the best value for the hyperparameters, by describing it:

    kubectl describe hyperparametertuningjob <JOBNAME>

In this case, it seems that the best value for `learning_rate` is about `0.005`.

    Status:
      Best Training Job:
        Creation Time:  2020-04-28T22:34:37Z
        Final Hyper Parameter Tuning Job Objective Metric:
          Metric Name:        tferror
          Value:
        Objective Status:     Succeeded
        Training End Time:    2020-04-28T22:38:13Z
        Training Job Status:  Completed
        Training Start Time:  2020-04-28T22:36:52Z
        Tuned Hyper Parameters:
          Name:                                    learning_rate
          Value:                                   0.005037803259063151

Detailed logs for a job are available with:

    kubectl smlogs hyperparametertuningjob <JOBNAME>