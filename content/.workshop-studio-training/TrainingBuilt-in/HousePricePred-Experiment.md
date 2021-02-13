---
title: "House Price Prediction Experiment"
chapter: false
weight: 130
---

### SageMaker Experiment

During the course of a single project, you might preprocess your data with various approach or train many models in search of maximum accuracy. Indeed, the number of combinations for preprocessing approaches, algorithms, data sets, and hyperparameter is infinite. SageMaker experiment allow you organize, track, compare and evaluate machine learning (ML) experiments and model versions.

Core concepts:

* An __experiment__ is simply a collection of trials, i.e. a group of related training jobs.
* A __trial__ is a collection of training steps involved in a single training job. Training steps typically includes preprocessing, training, model evaluation, etc. A trial is also enriched with metadata for inputs (e.g. algorithm, parameters, data sets) and outputs (e.g. models, checkpoints, metrics).

1. Access the SageMaker Studio you started earlier.
2. On the left sidebar, navigate into `MLAI/built-in-algorithms` , double click on `linearLearner_boston_house_experiment.ipynb` to open it.

In this notebook we will run training with various loss functions. The available loss functions and their default values depend on the value of `predictor_type`. The available options are `auto`, `squared_loss`, `absolute_loss`, `eps_insensitive_squared_loss`, `eps_insensitive_absolute_loss`, `quantile_loss`, and `huber_loss`. The default value for auto is `squared_loss`. You can specify the loss function with various values and compare the accuracy of the model using SageMaker experiment.

First, you create an experiment object:

```python
price_pred_experiment = Experiment.create(
    experiment_name=f"Boston-Housing-prediction-{int(time.time())}", 
    description="prediction of house price", 
    sagemaker_boto_client=sm_boto3)
print(price_pred_experiment)
```

Then, you create a Trial for each training run to track the it's parameters and metrics.:

```python
for i,loss_function in enumerate(['squared_loss','absolute_loss','huber_loss']):
    trial_name = f"boston-house-training-job-with-{fn_name}-loss-function-{int(time.time())}"
    boston_house_trial = Trial.create(
        trial_name=trial_name, 
        experiment_name=price_pred_experiment.experiment_name,
        sagemaker_boto_client=sm_boto3,
    )
    loss_function_trial_name_map[loss_function] = trial_name

    ll = sagemaker.estimator.Estimator(...)
    ll.set_hyperparameters(predictor_type='regressor',
                           ...,
                           loss = loss_function)

    ll.fit({'train': s3_input_train, 'validation': s3_input_validation}, experiment_config={
            "TrialName": boston_house_trial.trial_name,
            "TrialComponentDisplayName": "Training",
        },
        wait=False,)
```

### Compare the model training runs for an experiment

On the left sidebar, click on `SageMaker Experiment List` and find the experiment saved as `Boston-Housing-prediction-Date`. Right click on the experiment and select `open in trial component list`. It will show you list of the trials.

![Experiment image](/images/1experiment.png)

You can compare various metrics produced by each training job:

![Experiment Chart image](/images/1experimentchart.png)
