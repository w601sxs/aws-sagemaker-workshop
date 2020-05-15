---
title: "Batch Inference"
date: 2020-04-28T13:00:53-06:00
weight: 25
---

In the last section we used a real-time inference endpoint.  Real-time endpoints are useful when we need predictions as part of a low-latency system.  For example, we might want to provide a customer churn prediction while a call center agent is still talking to the customer on the phone.  That way, we can provide help to the agent if the customer is at risk of churn, such as providing a sales incentive over the phone.

However, in other cases, we don't need predictions in real-time.  With recommendation systems, for example, we might want to generate a very large number of predictions and store them in a NoSQL database for use later on.  Or, we may want to generate a sales forecast for the next seven days.  In these cases, the immediate context doesn't affect the prediction, and we can use a SageMaker batch transformation job to get a large number of predictions at once.  Using a batch transformation is often more cost-effective than keeping a prediction endpoint on all the time.

## Define the batch transform job

Download the [template file](/files/tf-batch.yaml) for an endpoint.  Make the following changes:

* Line 4: Give the job a unique name
* Line 6: Set the correct region
* Line 7: Set the model name.  You can find the actual model name in the SageMaker console under `Models`.
* Lines 13 and 17: Set the bucket name

## Running the job

Run:

    kubectl apply -f tf-batch.yaml

## Monitoring the job

You can check on job status by running:

    kubectl get batchtransformjob

You can see more details about a specific job with:

    kubectl describe batchtransformjob <JOBNAME>

Finally, you can see detailed job logs with:

    kubectl smlogs batchtransformjob <JOBNAME>

## Job results

Download the [example notebook](/files/customer_churn_batch.ipynb).  In your notebook, click `Upload` and select this notebook.  Click `Upload` again to complete the upload.

Now click the imported notebook to open it.  Read through and execute each cell in the notebook, making sure to edit the variables in the first code cell.  

After you finish executing this notebook, you'll see metrics like precision and recall for our model.  Note that the results are the same as when we got predictions from the real-time endpoint in the last chapter, but now we only had to make one call to SageMaker, rather than using the real-time endpoint.