---
title: "Check Pipeline Status"
date: 2020-04-28T09:16:41-06:00
weight: 15
---

After your pipeline completes, you will see a check mark by each stage.

![Pipeline Status](/images/pipeline/status.png)

If you click on a stage, you can get detailed status, including the log output.

![Stage Status](/images/pipeline/status-detailed.png)

In the [SageMaker console](https://console.aws.amazon.com/sagemaker/home?region=us-east-1), you can go to the _Hyperparameter tuning jobs_ section and see the HPO job that the pipeline ran.

![HPO](/images/pipeline/hpo.png)

If you click on the HPO job and scroll down, you'll see the hyperparameters from the best result.

![Best parameters](/images/pipeline/hpo-params.png)

Similarly, you can see the training job that the pipeline ran.

![Training job](/images/pipeline/train.png)

Under the _Models_ section, you can see the model created during the pipeline run.

![Model](/images/pipeline/model.png)

We'll dig into the inference endpoint and batch transformation outputs in the next section.
