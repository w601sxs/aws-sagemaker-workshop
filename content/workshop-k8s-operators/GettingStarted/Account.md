---
title: "Prerequisites"
date: 2020-04-28T10:02:27-06:00
weight: 10
---

## Prerequisites

To run this workshop, you need an AWS account, and a user identity with access to the following services:

* EKS
* SageMaker
* S3

You can use your own account, or an account provided through Event Engine as part of an AWS organized workshop.  Using an account provided by Event Engine is the easier path, as you will have full access to all AWS services, and the account will terminate automatically when the event is over.

You should also have familiarity with using the AWS CLI, including configuring the CLI for a specific account and region profile.  If not, please follow the [CLI setup instructions](https://github.com/aws/aws-cli).  Make sure you have a default profile set up.

### Account setup 

#### Using an account provided through Event Engine

If you are running this workshop as part of an Event Engine lab, please log into the console using [this link](https://dashboard.eventengine.run/) and enter the hash provided to you as part of the workshop.

#### Using your own AWS account

If you are using your own AWS account, be sure you have access to create S3 buckets, run SageMaker training jobs, create SageMaker endpoints, and create and manage EKS clusters.

*After completing the workshop, remember to complete the [cleanup](/workshop-k8s-operators/next) section to remove any unnecessary AWS resources.*

#### Note your account and region

After you have your account identified, pick an AWS region to work in, such as `us-west-2`.  We'll refer to this as `REGION` going forward.

Also note your AWS account number.  You find this in the console or by running `aws sts get-caller-identity` on the CLI.  We'll refer to this as `ACCOUNT` going forward.

### Cloud 9 (Optional)

Whichever AWS account option you use, you may prefer to use a cloud-based environment rather than installing tools like `eksctl` on your own machine.  In that case, you can use a [Cloud 9](https://aws.amazon.com/cloud9/) IDE.  

In the AWS console, go to the Cloud9 service and select `Create environment`.  Call your new IDE `KubeIDE` and click `Next Step`.  On the next screen, change the instance type to `m5.large` and click `Next step` again.  On the final page, click `Create environment`.  Make sure that you leave the VPC settings at the default values.

Once the environment builds, you'll automatically redirect to the IDE.  Take a minute to explore the interface, and note that you can change the color scheme if you like (AWS Cloud9 menu -> Preferences -> Themes).

Next, let's update the Cloud9 environment to let you run the labs from the environment.

* Go to the IAM console and create an instance profile for the Cloud 9 VM.  
    * Go to the `Roles` section.
    * Click `Create role`.
    * Select `AWS service` for the entity and leave the service set to `EC2`.
    * On the next screen, choose `Create policy`.
    * Switch to the JSON tab and paste in the contents of the file [cloud9-iam.json](/files/cloud9-iam.json).
    * Call the policy `Cloud9-kube-policy`.
    * Click `Create policy`.
    * Switch back to the browser tab with the new role, and assign the policy you just made.
    * Call the role `Cloud9-kube-role`.
    * Click `Create role`.
* Once this new profile is created, go to EC2 and find the Cloud9 instance, and assign the instance profile to this instance.
* Go to Cloud9 Preferences and under AWS Credentials disable `AWS managed temporary credentials`.  

Note that this role grants a very broad set of permissions to your Cloud9 instance.  

In your Cloud9 IDE, create the file `~/.aws/config` with these lines, replacing `REGION` and `ACCOUNT` with your own settings:

    [default]
    region=REGION
    account=ACCOUNT
