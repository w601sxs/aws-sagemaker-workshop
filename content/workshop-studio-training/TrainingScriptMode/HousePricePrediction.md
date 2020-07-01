---
title: "House Price Prediction"
chapter: false
weight: 210
---
## Training Scikit-learn models in Script mode

With Scikit-learn Estimators, you can train Scikit-learn models on Amazon SageMaker Studio.

You can use Amazon SageMaker to train and deploy models using custom python code to run with ScikitLearn library without having to worry about building containers or managing the underlying infrastructure. The Amazon SageMaker Python SDK ScikitLearn estimators, and the Amazon SageMaker open source ScikitLearn container, make it easy to run your algorithm it in Amazon SageMaker. The preferred way to leverage these capabilities is to use script mode.


1. Access the SageMaker Studio you opened earlier.
2. On the left sidebar, navigate into `MLAI/Script-mode/skl_Boston_house_price` folder, double click on `Sklearn_script_mode.ipynb` to open it.
3. You are now ready to begin the notebook.

In this notebook we show how to use Amazon SageMaker to develop, train, tune and deploy a Scikit-Learn based ML model. We will use an script that leverage `Random Forest` algorithm to train the model.

To train a Scikit-learn model by using the SageMaker Python SDK:

1. Prepare a training script, i.e. `script.py`
2. Create a `sagemaker.sklearn.SKLearn` Estimator

    ```python
    from sagemaker.sklearn.estimator import SKLearn

    sklearn_estimator = SKLearn(
        entry_point='script.py',
        role = get_execution_role(),
        train_instance_count=1,
        train_instance_type='ml.c5.xlarge',
        framework_version='0.20.0',
        base_job_name='rf-scikit')

    ```

3. Call the estimator’s fit method

    ```python
    sklearn_estimator.fit({'train':trainpath, 'test': testpath}, wait=False)
    ```

In this notebook we show 2 options for launching your training:  

* Launching a training job with the Python SDK
* Launching a training with boto3

As always, you can go to `SageMaker Experiment list` tab on the left sidebar and check the progress of the training jobs.
