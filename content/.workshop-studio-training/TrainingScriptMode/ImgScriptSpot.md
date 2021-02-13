---
title: "Img Classificaiton-Spot training"
chapter: false
weight: 250
---

### Training using SageMaker Managed Spot Training

Managed Spot Training uses Amazon EC2 Spot instance to run training jobs instead of on-demand instances. You can specify which training jobs use spot instances and a stopping condition that specifies how long Amazon SageMaker waits for a job to run using Amazon EC2 Spot instances. Metrics and logs generated during training runs are available in CloudWatch.

Spot instances can be interrupted, causing jobs to take longer to start or finish. You can configure your managed spot training job to use checkpoints. Amazon SageMaker copies checkpoint data from a local path to Amazon S3. When the job is restarted, Amazon SageMaker copies the data from Amazon S3 back into the local path. The training can then resume from the last checkpoint instead of restarting.

This lab tackles the exact same problem with the same solution, but it has been modified to be able to run using SageMaker Managed Spot infrastructure. SageMaker Managed Spot uses [EC2 Spot Instances](https://aws.amazon.com/ec2/spot/) to run Training at a lower cost.

Setting up of Spot is simple. For Managed Spot Training using a TensorFlow Estimator we need to configure two things:

1. just set the `train_use_spot_instances` to `true` in the Estimator constructor.
2. Set the `train_max_wait` which represents the amount of time you are willing to wait for Spot infrastructure to become available. 
3. You can set the`train_max_run` to force Amazon SageMaker terminates the job regardless of its current status after this amount of time.

    ```python
    estimator = TensorFlow(base_job_name='spot-cifar10-tf',
                        entry_point='cifar10_keras_main.py',
                        source_dir=source_dir,
                        output_path=model_artifacts_location,
                        train_use_spot_instances=train_use_spot_instances,
                        train_max_run=train_max_run,
                        train_max_wait=train_max_wait,
                        ...)
    ```

To start the notebook:

1. Access the SageMaker Studio you started earlier.
2. On the left sidebar, navigate into `MLAI/Script-mode/keras_cifar10` folder, double click on `TF_keras_CIFAR10_ScriptMode_Spot.ipynb` to open it.
3. You are now ready to begin the notebook.

### Savings

Towards the end of the job you should see two lines of output printed:

* `Training seconds: X` : This is the actual compute-time your training job spent
* `Billable seconds: Y` : This is the time you will be billed for after Spot discounting is applied.

If you enabled the `train_use_spot_instances` var then you should see a notable difference between `X` and `Y` signifying the cost savings you will get for having chosen Managed Spot Training. This should be reflected in an additional line:
`Managed Spot Training savings: (1-Y/X)*100 %`
