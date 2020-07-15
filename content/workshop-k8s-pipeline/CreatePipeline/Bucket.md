---
title: "S3 Bucket"
date: 2020-04-28T09:16:41-06:00
weight: 5
---

We'll store our pre-processing script and other data in an S3 bucket in the `us-east-1` region.  Follow the [getting started guide](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) to create a bucket in the `us-east-1` region.  The bucket should *NOT* be public.  We'll refer to the bucket as `BUCKET` going forward.

Download the [pre-processing script](/files/pipeline/kmeans_preprocessing.py) to a working directory and then upload it to S3.

    aws s3 cp kmeans_preprocessing.py s3://BUCKET/mnist_kmeans_example/processing_code/kmeans_preprocessing.py
