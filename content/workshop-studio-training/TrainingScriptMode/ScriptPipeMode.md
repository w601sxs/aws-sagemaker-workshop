---
title: "Img Classification-Pipe Mode"
chapter: false
weight: 230
---

Your data is transferred from S3 into the training instances when you start the training job. You can accelerate the speed at which data can be streamed from S3 into SageMaker, while training ML models, through Pipe Mode.

SageMaker Pipe Mode is a mechanism for providing S3 data to a training job via Linux fifos. Training programs can read from the fifo and get high-throughput data transfer from S3, without managing the S3 access in the program itself. Pipe Mode is covered in more detail in the SageMaker [documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo.html#your-algorithms-training-algo-running-container-inputdataconfig)

1. Access the SageMaker Studio you setup earlier.
2. On the left sidebar, navigate into `MLAI/Script-mode/keras_cifar10` folder, double click on `TF_keras_CIFAR10_ScriptMode_PipeMode.ipynb` to open it.
3. You are now ready to begin the notebook.

in our script, we enabled Pipe Mode using the following code:

```python
from sagemaker_tensorflow import PipeModeDataset
dataset = PipeModeDataset(channel=channel_name, record_format='TFRecord')
```

and then we set `input_mode='Pipe'` in the estimator:

```python
estimator_pipe = TensorFlow(base_job_name='pipe-cifar10-tf',
                       entry_point='cifar10_keras_main.py',
                       source_dir=source_dir,
                       hyperparameters=hyperparameters,
                       train_instance_count=1,
                       train_instance_type='ml.p3.2xlarge',
                       input_mode='Pipe')
```
