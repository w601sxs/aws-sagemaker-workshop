---
title: "Run the Pipeline"
date: 2020-04-28T09:16:41-06:00
weight: 5
---

To get started, click the _Create run_ button.

![Pipeline](/images/pipeline/trigger.png)

On the next screen, you can give this run a unique name and description.  You can also associate it with an experiment, or just use the _Default_ experiment.

![Pipeline](/images/pipeline/run1.png)

Moving further down the page, you'll now need to enter and review two pieces of information.

* Region: Confirm this is set to _us-east-1_
* role_arn: Set this to the `ROLE_ARN` you created in the [previous chapter](/workshop-k8s-pipeline/createpipeline/role/)

![Pipeline](/images/pipeline/run2.png)

There are several additional parameters you can review or modify, but you only need to fill out the _Region_ and _role_arn_.

Finally, click _Start_ at the bottom of the screen.  You'll see your job running in the list of _Runs_; click on the job name to see the detailed execution status.  Your pipeline will take several minutes to complete.

![Pipeline](/images/pipeline/runs.png)
