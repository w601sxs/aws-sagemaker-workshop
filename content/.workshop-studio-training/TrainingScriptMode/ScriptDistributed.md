---
title: "Img Classificaiton-Distributed"
chapter: false
weight: 240
---

### Distributed training with horovod

Horovod is a distributed training framework based on MPI. Horovod is only available with TensorFlow version 1.12 or newer.

1. Access the SageMaker zstudio you started earlier.
2. On the left sidebar, navigate into `MLAI/Script-mode/keras_cifar10` folder, double click on `TF_keras_CIFAR10_ScriptMode_Distributed.ipynb` to open it.
3. You are now ready to begin the notebook.

To enable Horovod, we need to add the following code to our script:

```python
import horovod.keras as hvd
hvd.init()
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
config.gpu_options.visible_device_list = str(hvd.local_rank())
K.set_session(tf.Session(config=config))
```

Add the following callbacks:

```python
hvd.callbacks.BroadcastGlobalVariablesCallback(0)
hvd.callbacks.MetricAverageCallback()
```

Configure the optimizer:

```python
opt = Adam(lr=learning_rate * size, decay=weight_decay)
opt = hvd.DistributedOptimizer(opt)
```

Now, in the notebook:  

1. To run the training job with multiple instances in a distributed fashion, set `train_instance_count` to a number larger than 1.

2. We should set the `distributions` parameter to configure which distributed training strategy to use. To start a distributed training job with Horovod, configure the job distribution:

    ```python
    distributions = {'mpi': {
                        'enabled': True,
                        'processes_per_host': # Number of Horovod processes per host
                            }
                    }
    ```

    ```python
    estimator_dist = TensorFlow(base_job_name='dist-cifar10-tf',
                        entry_point='cifar10_keras_main.py',
                        source_dir=source_dir,
                        role=role,
                        framework_version='1.12.0',
                        py_version='py3',
                        hyperparameters=hyperparameters,
                        train_instance_count=2,
                        train_instance_type='ml.p3.2xlarge',
                        metric_definitions=keras_metric_definition,
                        distributions=distributions)
    ```
