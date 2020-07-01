---
title: "House Price Prediction"
chapter: false
weight: 310 
---

 

As we saw in the previous *Script Mode* section, SageMaker includes a pre-built Scikit-Learn container.  We usually recommend that the pre-built container be used for almost all cases requiring a Scikit_Learn algorithm.  In this lab, however, we will build a custom Scikit-Learn container to demonstrate the steps involved in packaging custom code and libraries into a container that will be used with SageMaker.

In this lab we will use AWS CodeBuild to build our Docker image and push it to the Amazon Elastic Container Registry (Amazon ECR).

1. We will bring our custom container into the SageMaker by packaging it and uploading it into S3 (e.g. `codebuild__random_forest.zip`). This compress files includes:
    * Your docker file. It describes how to build your Docker container image.
    * Your ML scripts(.py) for training that you installed in the container.
    * Your script (buildspec.yml) to build and push the Docker Image into ECR

    Note:
    * You can jump into the lab notebook and run the first cell to package and upload it into S3.
    * You can also use AWS CLI, Cloud 9, EC2, your local machine, or anywhere else that you would like to build the docker files.
    * For this lab, we have already packaged  [codebuild__random_forest.zip](https://github.com/saeedaghabozorgi/MLAI/blob/master/BYOC/scikit_bring_your_own/codebuild__random_forest.zip) file that you can download.  
2. Store the `codebuild__random_forest.zip` file into a S3 bucket (e.g. `s3://<BUCKET_NAME>/<PREFIX>/codebuild__random_forest.zip`).
3. Before we can run our CodeBuild job, we first need to make sure that we have an ECR repository in which we will store our Docker images.
    * Browse to the AWS Consol, Browse to the ECR, click on `Create repository`, and enter `sagemaker-random-forest` as the name of the repository. Take note of the full repository name as you will need it in the next section.
4. Now that we have uploaded our training script and Dockerfile to S3, the next step is to define a CodeBuild project. Remember, we'll be using a CodeBuild project to automate the Docker build process.
    * In a new tab, browse to AWS CodeBuild.
    * Click on `Create build project`, and set the parameters:

        ```xml
        Project Name: SM_BuildWorkshopContainer
        Source
            Source provider: Amazon S3
            bucket: <BUCKET_NAME>
            S3 object key or S3 folder:<PREFIX>/codebuild__random_forest.zip
        Environment
            Operating system: Amazon Linux 2
            Runtime(s): Standard
            Image: amazonlinux2-x86_64-standard:3.0
        Privileged
            Enable this flag to build Docker images
        RoleName: codebuild-SM_BuildWorkshopContainer-service-role
        ```

    * Set the Environment Variables:

        ```xml
        AWS_DEFAULT_REGION:us-east-1
        ALGORITHM_NAME:sagemaker-random-forest
        IMAGE_NAME:<ACCOUNT_NO>.dkr.ecr.us-east-1.amazonaws.com/sagemaker-random-forest:latest
        ```

        ![CodeBuild](/images/1codebuild.png)

5. Before start building the Docker Image, you should give proper permission to AWS CodeBuild to push the Docker Image to the ECR repository.
    * Open a new instance of the AWS Console in a separate browser tab/window
    * On the left-hand side, choose `Roles`
    * Search for CodeBuild service role (usually something like `codebuild-<PROJECT_NAME>-service-role`)
    * Click the correct role in the list, and choose `Attach Policies`
    * Search for the `AmazonEC2ContainerRegistryFullAccess` policy, placing a checkmark next to each
    * Click `Attach Policy`

6. You can click on `Start build` to build the Docker Image and push it into the repository. Monitor your ongoing build job (try clicking the first link under 'Build run' to view the log files). When your container image has been created, the 'Latest Build Status' column will show as `Succeeded`.

    > Note:  
    Once the Codebuild job is complete, click the `ECR` link above. If your CodeBuild job was successful in pushing your new image into ECR, you will see a new image with the image tag `latest`. Under the `Pushed at` column for this image, you should see that this image was pushed very recently.

7. Now, let's open our notebook and begin the training based on the custom container you built:

    * Access the SageMaker Studio instance you created earlier.
    * On the left sidebar, click the Folder icon and navigate into the `MLAI/BYOC/scikit_bring_your_own` folder. Double click on `scikit_bring_your_own.ipynb` to open it.
    * You are now ready to begin the notebook. Follow through the provided steps to build your custom container, and then leverage it for training in SageMaker
