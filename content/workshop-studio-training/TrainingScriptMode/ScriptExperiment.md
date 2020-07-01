---
title: "Img Classification-Experiment"
chapter: false
weight: 235
---

### SageMaker Experiment

In the training with built-in algorithms you learned how to use SageMaker Experiment to track trials. In this section, you will learn:

1. how to define and add a __tracker__ to a trial for pre-processing
2. how to pass the parameters to scripts for each experiment
3. How to query and compare the training runs for identifying the best model produced by our experiment. 

To start the notebook:

1. Access the SageMaker Studio you started earlier.
2. On the left sidebar, navigate into `MLAI/Script-mode/keras_cifar10_experiment` folder, double click on `TF_keras_CIFAR10_ScriptMode-experiment.ipynb` to open it.
3. You are now ready to begin the notebook.

You first add a tracker to the notebook to track the the preprocessing and dataset location:

```python
with Tracker.create(display_name="Preprocessing", sagemaker_boto_client=sm_client) as tracker:
    tracker.log_parameters({
        "datatype": 'tfrecords',
        "image_size": 32,
    })
    tracker.log_input(name="cifar10-dataset", media_type="s3/uri", value=dataset_location)
```

Then you create an experiment object:

```python
cifar10_experiment = Experiment.create(
    experiment_name=f"cifar10-image-classification-{int(time.time())}", 
    description="Classification of images", 
    sagemaker_boto_client=sm_client)
print(cifar10_experiment)
```

Then, you create a Trial for each training run to track the it's inputs, parameters, and metrics.:

```python
for i, opt_method in enumerate(['adam','sgd','rmsprop']):
    trial_name = f"cifar10-training-job-with-{opt_method}"
    cifar10_trial = Trial.create(
        trial_name=trial_name, 
        experiment_name=cifar10_experiment.experiment_name,
        sagemaker_boto_client=sm_client,
    )
    # associate the preprocessing trial component with the current trial
    cifar10_trial.add_trial_component(tracker.trial_component)

    estimator = TensorFlow(base_job_name='cifar10-tf',
                           entry_point='cifar10_keras_main.py',
                           ....
                           hyperparameters={'epochs': 1, 'batch-size' : 256, 'optimizer' : opt_method},
                           ....
                            )
    
    estimator.fit(remote_inputs, job_name=cifar10_training_job_name,
        experiment_config={
            "TrialName": cifar10_trial.trial_name,
            "TrialComponentDisplayName": "Training",
        },
        wait=False)
```
