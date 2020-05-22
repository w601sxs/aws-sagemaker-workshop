---
title: "Inference"
date: 2020-04-27T14:57:41-06:00
weight: 15
---

Now that we've built a model, let's deploy a hosted SageMaker inference endpoint and use it to get some predictions.

## Deploy the endpoint

Download the [template file](/files/tf-endpoint.yaml) for an endpoint.  Make the following changes:

* Lines 4, 9, and 14: Give the endpoint a unique name
* Line 6: Set the correct region
* Line 15: Use the same execution role as you used for the training job.
* Line 18: Set the path to the model artifact.  You can find this by running `kubectl describe trainingjob <JOBNAME>` and looking for the `Model Path`.
* Line 19: Set the correct image URI.  This is usually in the form `763104351884.dkr.ecr.REGION.amazonaws.com/tensorflow-inference:2.1-gpu`.

Now run:

    kubectl apply -f tf-endpoint.yaml

You can check on the endpoint status by running `kubectl get hostingdeployments` and `kubectl describe hostingdeployments <ENDPOINT>`.

## Add permission to invoke endpoint to IAM role

Find the IAM role whose name starts with `eksctl-eks-kubeflow-nodegroup`.  Attach the policy `AmazonSageMakerFullAccess` to let this role invoke our endpoint.

## Get predictions

Download the [example notebook](/files/customer_churn_inference.ipynb).  In your notebook, click `Upload` and select this notebook.  Click `Upload` again to complete the upload.

Now click the imported notebook to open it.  Read through and execute each cell in the notebook, making sure to edit the variables in the first code cell.  You can find the `endpoint` by describing your inference endpoint.

After you finish executing this notebook, you'll see metrics like precision and recall for our model.

