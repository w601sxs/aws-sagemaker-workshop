---
title: "Create and Run Pipeline"
date: 2020-04-28T09:16:41-06:00
weight: 15
---

The code to register and execute the pipeline is in the sample notebook _kfp-sagemaker-script-mode.ipynb_, which should be in the root of the file system for the notebok.

Let's start executing the notebook cell by cell.  You can execute each cell by typing _Shift+Enter_.

### Imports and other prerequisites

The first block just installs the Kubeflow Pipeline DSL compiler in the local Python environment.  

    !pip install kfp --upgrade
    !which dsl-compile

Since we just installed a new module, go to the _Kernel_ menu and select _Restart_.

In the next cell we'll import a few Python modules.

    import kfp
    from kfp import components
    from kfp.components import func_to_container_op
    from kfp import dsl
    import time, os, json

Next we register the location of the SageMaker Components.

    sagemaker_hpo_op = components.load_component_from_url('https://raw.githubusercontent.com/kubeflow/pipelines/cb36f87b727df0578f4c1e3fe9c24a30bb59e5a2/components/aws/sagemaker/hyperparameter_tuning/component.yaml')
    sagemaker_train_op = components.load_component_from_url('https://raw.githubusercontent.com/kubeflow/pipelines/cb36f87b727df0578f4c1e3fe9c24a30bb59e5a2/components/aws/sagemaker/train/component.yaml')
    sagemaker_model_op = components.load_component_from_url('https://raw.githubusercontent.com/kubeflow/pipelines/cb36f87b727df0578f4c1e3fe9c24a30bb59e5a2/components/aws/sagemaker/model/component.yaml')
    sagemaker_deploy_op = components.load_component_from_url('https://raw.githubusercontent.com/kubeflow/pipelines/cb36f87b727df0578f4c1e3fe9c24a30bb59e5a2/components/aws/sagemaker/deploy/component.yaml')

Now we'll set up some basic variables for SageMaker, including our session and role.  Change the `role` to use the `ROLE_ARN` from the previous chapter.

    import sagemaker
    import boto3

    sess = boto3.Session()
    sm   = sess.client('sagemaker') 
    role = 'ROLE_ARN'
    sagemaker_session = sagemaker.Session(boto_session=sess)

If you don't have the _sagemaker_ module available in your Python environment yet, add this line in a new cell and try again:

    !pip install sagemaker

### Upload data and code

In the next two cells we'll upload the data and code to the S3 bucket that SageMaker uses by default.

    bucket_name = sagemaker_session.default_bucket()
    job_folder      = 'jobs'
    dataset_folder  = 'datasets'
    local_dataset = 'cifar10'

    !python generate_cifar10_tfrecords.py --data-dir {local_dataset}
    datasets = sagemaker_session.upload_data(path='cifar10', key_prefix='datasets/cifar10-dataset')

    !tar cvfz sourcedir.tar.gz --exclude=".ipynb*" -C code .
    source_s3 = sagemaker_session.upload_data(path='sourcedir.tar.gz', key_prefix='training-scripts')
    print('\nUploaded to S3 location:')
    print(source_s3)

If you do not yet have Tensorflow installed in your Python environment, run this first in a new cell:

    !pip install tensorflow==1.15

You'll need to use TensorFlow 1.x.  If you see an error about no `1.15` version existing, please follow the suggestions in this [ticket](https://github.com/tensorflow/tensorflow/issues/34302).

Finally we'll register a helper function for getting the results from an HPO job.

    def update_best_model_hyperparams(hpo_results, best_model_epoch = "80") -> str:
    import json
    r = json.loads(str(hpo_results))
    return json.dumps(dict(r,epochs=best_model_epoch))

    get_best_hyp_op = func_to_container_op(update_best_model_hyperparams)

### Register the pipeline

The next cell registers the pipeline.  We need change the region from `us-west-2` to `us-east-1`, as highlighted below.

    @dsl.pipeline(
        name='cifar10 hpo train deploy pipeline',
        description='cifar10 hpo train deploy pipeline using sagemaker'
    )
    def cifar10_hpo_train_deploy(region='us-east-1',
                               training_input_mode='File',
                               train_image='763104351884.dkr.ecr.us-east-1.amazonaws.com/tensorflow-training:1.15.2-gpu-py36-cu100-ubuntu18.04',
                               serving_image='763104351884.dkr.ecr.us-east-1.amazonaws.com/tensorflow-inference:1.15.2-cpu',
                               volume_size='50',
                               max_run_time='86400',

                               ...

    hpo = sagemaker_hpo_op(
        region=region,
        image=train_image,
        training_input_mode=training_input_mode,
        strategy='Bayesian',
        metric_name='val_acc',
        metric_definitions='{"val_acc": "val_acc: ([0-9\\\\.]+)"}',
        metric_type='Maximize',
        static_parameters='{ \
            "epochs": "10", \
            "momentum": "0.9", \
            "weight-decay": "0.0002", \
            "model_dir":"s3://'+bucket_name+'/jobs", \
            "sagemaker_program": "cifar10-training-sagemaker.py", \
            "sagemaker_region": "us-east-1", \
            "sagemaker_submit_directory": "'+source_s3+'" \
        }',
        ...

Next we compile the pipeline.

    kfp.compiler.Compiler().compile(cifar10_hpo_train_deploy,'sm-hpo-train-deploy-pipeline.zip')

As you can see from the pipeline definition code, the pipeline will have five stages:

* HPO
* Updating with HPO output and increasing the number of epochs
* Training
* Model creation
* Model deployment 

### Execute the pipeline

The next cell creates a new experiment and executes a run of the pipeline.

    client = kfp.Client()
    aws_experiment = client.create_experiment(name='sm-kfp-experiment')

    exp_name    = f'cifar10-hpo-train-deploy-kfp-{time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime())}'
    my_run = client.run_pipeline(aws_experiment.id, exp_name, 'sm-hpo-train-deploy-pipeline.zip')

After you execute this cell, you'll get links in the notebook for the experiment and run.  Click on those links, but note that you may need to adjust the URL if you are not using k8s port forwarding to `localhost:8888`.  You can also navigate to the experiment by going to your Kubeflow dashboard, clicking on _Experiments_ in the menu on the left, and opening the _sm-kfp-experiment_.

Note that the HPO job may take over an hour to complete, while the training job and endpoint deployment may take several more minutes each.

### Monitor the results

Drilling into the new _sm-kfp-experiment_, we can see the output.  (If your pipeline fails due to limits on the number of _p3.2xlarge_ instances you can run, change the HPO specification in the pipeline to no more than 2 concurrent jobs and try again.)

![Pipeline](/images/pipeline/script-pipeline.png)

### Test the endpoint

The last cell in the notebook uses the deployed inference endpoint to classify an image of a dog.  Note that you need to adjust the _EndpointName_ to match your deployed endpoint.

    import json, boto3, numpy as np
    client = boto3.client('runtime.sagemaker')

    file_name = '1000_dog.png'
    with open(file_name, 'rb') as f:
        payload = f.read()

    response = client.invoke_endpoint(EndpointName='ENDPOINT',
                                       ContentType='application/x-image', 
                                       Body=payload)
    pred = json.loads(response['Body'].read())['predictions']
    labels = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']
    for l,p in zip(labels, pred[0]):
        print(l,"{:.4f}".format(p*100))

You'll see output showing confidence scores for each possible class, with the _dog_ class having a score over 99.
