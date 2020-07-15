---
title: "Batch Transform Output"
date: 2020-04-28T09:16:41-06:00
weight: 25
---

The pipeline executed a batch transformation job for you, getting inferences for each record in the validation dataset.  In the pipeline results page, click on the _sagemaker-batch-transformation_ stage and view the _Input/Output_ section.

![Pipeline Status](/images/pipeline/batch.png)

Locate the `batch_transform_ouput` field and copy the S3 path.  List that path to see and download the batch job output. 

    aws s3 cp s3://BUCKET/mnist_kmeans_example/output/valid-data.csv.out .
    more valid-data.csv.out

You'll see a set of records that looks like this:

    {"closest_cluster": 4.0, "distance_to_cluster": 6.285102367401123}

You can inspect the results to see how well the model performed on the validation data set.
