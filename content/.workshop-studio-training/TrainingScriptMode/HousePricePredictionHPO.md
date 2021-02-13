---
title: "House Price Prediction-HPO"
chapter: false
weight: 215
---
## Hyper Parameter Optimization (HPO)

Amazon SageMaker automatic model tuning finds the best version of a model by running many training jobs on your dataset using the algorithm and ranges of hyperparameters that you specify. It then chooses the hyperparameter values that result in a model that performs the best, as measured by a metric that you choose.

Amazon SageMaker supports two types of HPO:

* Random Search
* Bayesian Search

In this lab, we use Bayesian Search HPO which uses an Amazon SageMaker implementation of Bayesian optimization.

Before you start using hyperparameter tuning, you should have:

1. An understanding of the type of algorithm you need to train, for example Random Forest

2. The hyperparmeters that you want the HPO optimize for you, for example number of estimators in Random Forest.

    ```python
    hyperparameter_ranges = {
        'n-estimators': IntegerParameter(20, 100),
        'min-samples-leaf': IntegerParameter(2, 6)}
    ```

3. A clear understanding of how you measure success, for example Absolute Error, F1, etc.

    ```python
    objective_metric_name = 'median-AE'
    objective_type = 'Minimize'
    ```

4. Finally, you need to define the optimizer and call fit method:

    ```python
    Optimizer = sagemaker.tuner.HyperparameterTuner(
        estimator=sklearn_estimator,
        hyperparameter_ranges=hyperparameter_ranges,
        objective_type=objective_type,
        objective_metric_name=objective_metric_name,
        ...)
    Optimizer.fit({'train': trainpath, 'test': testpath})
    ```

In this notebook we show how to use Amazon SageMaker to develop, train and tune a Scikit-Learn based ML model (Random Forest). It leverages hyperparameter tuning to kick off multiple training jobs with different hyperparameter combinations, to find the one with best model training result.

1. Access the SageMaker Studio you opened earlier.
2. On the left sidebar, navigate into `MLAI/Script-mode/skl_Boston_house_price` folder, double click on `Sklearn_script_mode-HPO.ipynb` to open it.
3. You are now ready to begin the notebook.

Check the training jobs that HPO runs in parallel.
![HPO image](/images/1HPOjobs.png)
