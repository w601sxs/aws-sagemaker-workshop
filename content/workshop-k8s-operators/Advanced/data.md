---
title: "Data Preparation"
date: 2020-04-29T17:12:16-06:00
weight: 15
---

We'll still need to do some initial data exploration and preparation.  Download the [example notebook](/files/customer_churn_tf_csv.ipynb).  In your notebook, click `Upload` and select this notebook.  Click `Upload` again to complete the upload.

Now click the imported notebook to open it.  Read through and execute each cell in the notebook, making sure to edit the `bucket` and `prefix` variables in the first code cell.

After you finish executing this notebook, you'll have train, validation, and test data sets stored in S3.  

Note that this notebook does not require the use of one-hot encoding; our data preparation steps mainly include dropping columns we don't need.

