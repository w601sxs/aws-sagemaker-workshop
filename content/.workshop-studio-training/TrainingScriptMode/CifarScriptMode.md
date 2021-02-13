---
title: "Img Classification"
chapter: false
weight: 220
---
## Amazon SageMaker script mode

You can use Amazon SageMaker to train and deploy models using custom TensorFlow code without having to worry about building containers or managing the underlying infrastructure. The [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/using_tf.html) TensorFlow estimators make it easy to write a TensorFlow script and then simply run it in Amazon SageMaker. The preferred way to leverage these capabilities is to use script mode.

You can use script mode with Amazon SageMaker prebuilt TensorFlow containers to train TensorFlow models with the same kind of training script you would use outside SageMaker. Your script mode code does not need to comply with any specific Amazon SageMaker-defined interface or use any specific TensorFlow API.

1. Access the SageMaker Studio you started earlier.
2. On the left sidebar, navigate into `MLAI/Script-mode/keras_cifar10_script_mode` folder, double click on `TF_keras_CIFAR10_ScriptMode.ipynb` to open it.
3. You are now ready to begin the notebook.

> Note: It is recommended to use `Python 3 (TensorFlow 2 CPU Optimized)` kernel in SageMaker Studio for this notebook.

This notebook shows how to train a Keras Sequential model on SageMaker. We use a Python script to train a classification model on the CIFAR dataset. The model used for this notebook is a simple deep CNN that was extracted from the Keras examples.

To train a TensorFlow model by using the SageMaker Python SDK:

1. Prepare a training script
    * The training script is very similar to a training script you might run outside of SageMaker, but you can access useful properties about the training environment through various environment variables, such as `SM_NUM_GPUS` which represents the number of GPUs available to the host.
    * we stroed this file as `source_dir/cifar10_keras_main.py`

2. Create a `sagemaker.tensorflow.TensorFlow` estimator

    * The sagemaker.tensorflow.TensorFlow estimator handles locating the script mode container, uploading your script to a S3 location and creating a SageMaker training job. 

    ```python
    from sagemaker.tensorflow import TensorFlow
    estimator = TensorFlow(base_job_name='cifar10-tf',
                        entry_point='cifar10_keras_main.py',
                        source_dir=source_dir,
                        hyperparameters=hyperparameters,
                        train_instance_count=1, 
                        train_instance_type='ml.p3.2xlarge',
                        ...)

    ```

3. Call the estimator’s fit method

    ```python
    remote_inputs = {'train' : dataset_location+'/train', 'validation' : dataset_location+'/validation', 'eval' : dataset_location+'/eval'}
    estimator.fit(remote_inputs, wait=True)
    ```

### View the job training metrics

SageMaker used the regular expression configured above, to send the job metrics to CloudWatch metrics.
You can also view the job metrics directly from the SageMaker Studio . On the left side bar select the SageMaker Experiment List, right click on  _Unassigned trial components_, open in trial component list, choose the latest training job, open in trial details, and now you can see all the metrics that you defined to sent to Cloud watch.
You can also use CloudWatch metrics, where you can change the period and configure the statistics.

![Script Mode metrics](/images/1metrics.png)
