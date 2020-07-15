---
title: "Register the Pipeline"
date: 2020-04-28T09:16:41-06:00
weight: 35
---

Now let's register the pipeline in Kubeflow.  To get started, access the Kubeflow dashboard.  (See the [Kubeflow installation guide](https://www.kubeflow.org/docs/aws/deploy/install-kubeflow/) for information on accessing the Kubeflow dashboard.  The details will vary based on how you installed Kubeflow.)

Now go to the _Pipelines_ section, which you can access in the menu on the dashboard.  The _Pipelines_ item is the second item in the menu.

![Kubeflow Dashboard](/images/pipeline/kfdash.png)

Now click on _Upload Pipeline_.  

![Upload Pipeline](/images/pipeline/kfupload.png)

On the next screen, enter the following information:

* Choose _Create a new pipeline_
* Give your pipeline a name and description
* Select _Upload a file_ and select the package you created in the last section

![Pipeline](/images/pipeline/pipeline.png)

Now click _Create_.  You'll see the pipeline in _Graph_ view.

![Pipeline](/images/pipeline/graph.png)
