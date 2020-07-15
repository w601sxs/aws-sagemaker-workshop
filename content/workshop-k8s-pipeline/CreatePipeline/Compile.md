---
title: "Compile the Pipeline Definition"
date: 2020-04-28T09:16:41-06:00
weight: 25
---

Download the [pipeline definition script](/files/pipeline/mnist-classification-pipeline.py) into a working directory.  On line 9, insert the name of the S3 bucket you created earlier in this chapter.

Now execute this command to generate the pipeline artifact.

    dsl-compile --py mnist-classification-pipeline.py --output mnist-classification-pipeline.tar.gz

You may see several DSL warnings, which you can safely ignore.
