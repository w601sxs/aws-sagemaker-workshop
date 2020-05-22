---
title: "Training and Inference"
date: 2020-04-29T17:37:06-06:00
weight: 35
---

Now that we have a better training script, we can repeat the steps in the [Training](/workshop-k8s-operators/train) chapter.  You'll need to make the following changes:

* Repackage the `sourcedir.tar.gz` file with the improved training script
* In the training job definition, use the path to the updated training data CSV files on line 41
* While getting inferences, you'll want to pass in rows from the updated test CSV data, rather than the original (more heavily pre-processed) test data set stored as a Numpy file.
* If you run an HPO job, you can experiment with the additional hyperparameters.  You'll also need to provide the path to the updated data set.

We'll leave these changes as an exercise for you!

As a final note, given that our data set is quite small, it's very likely that our model won't meet the performance of tree-based algorithms like XGBoost.  XGBoost achieves over 95% accuracy with this data set, while achieving better than 86% accuracy with our TensorFlow model is quite good.
