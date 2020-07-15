---
title: "Prerequisites"
date: 2020-04-28T10:02:27-06:00
weight: 10
---

## Prerequisites

To run this workshop, you need an AWS account, and a user identity with access to the following services:

* SageMaker
* S3
* EKS (If you want to use a managed kubernetes cluster)

You can use your own account, or an account provided through Event Engine as part of an AWS organized workshop.  Using an account provided by Event Engine is the easier path, as you will have full access to all AWS services, and the account will terminate automatically when the event is over.

You should also have familiarity with using the AWS CLI, including configuring the CLI for a specific account and region profile.  If not, please follow the [CLI setup instructions](https://github.com/aws/aws-cli).  Make sure you have a default profile set up.

Finally, you'll need to have a kubernetes cluster set up with Kubeflow installed, and a local copy of the KFP SDK.

### Account setup 

#### Using an account provided through Event Engine

If you are running this workshop as part of an Event Engine lab, please log into the console using [this link](https://dashboard.eventengine.run/) and enter the hash provided to you as part of the workshop.

#### Using your own AWS account

If you are using your own AWS account, be sure you have access to create S3 buckets, run SageMaker training jobs, create SageMaker endpoints, and optionally create and manage EKS clusters.

*After completing the workshop, remember to complete the [cleanup](/workshop-k8s-pipeline/next) section to remove any unnecessary AWS resources.*

#### Note your account and region

After you have your account identified, make sure to work in the `us-east-1` region.  

Also note your AWS account number.  You find this in the console or by running `aws sts get-caller-identity` on the CLI.  We'll refer to this as `ACCOUNT` going forward.

### Cloud 9 (Optional)

Whichever AWS account option you use, you may prefer to use a cloud-based environment rather than installing tools like `eksctl` on your own machine.  In that case, you can use a [Cloud 9](https://aws.amazon.com/cloud9/) IDE.  See the [getting started guide](https://docs.aws.amazon.com/cloud9/latest/user-guide/welcome.html#how-to-get-started) for how to set up your own Cloud 9 IDE.

If you use Cloud 9, you'll need to make a few changes to your IDE to let you run the labs from the environment.

* Go to the IAM console and create an instance profile for the Cloud 9 VM.  
    * Go to the `Roles` section.
    * Click `Create role`.
    * Select `AWS service` for the entity and leave the service set to `EC2`.
    * On the next screen, choose `Create policy`.
    * Switch to the JSON tab and paste in the contents of the file [cloud9-iam.json](/files/pipeline/cloud9-iam.json).
    * Call the policy `Cloud9-kube-policy`.
    * Click `Create policy`.
    * Switch back to the browser tab with the new role, and assign the policy you just made.
    * Call the role `Cloud9-kube-role`.
    * Click `Create role`.
* Once this new profile is created, go to EC2 and find the Cloud9 instance, and assign the instance profile to this instance.
* Go to Cloud9 Preferences and under AWS Credentials disable `AWS managed temporary credentials`.  

Note that this role grants a very broad set of permissions to your Cloud9 instance.  

In your Cloud9 IDE, create the file `~/.aws/config` with these lines, replacing `ACCOUNT` with your own settings:

    [default]
    region=us-east-1
    account=ACCOUNT

### Kubernetes cluster with Kubeflow

You'll need a kubernetes (k8s) cluster with Kubeflow installed.  

If you need to make a k8s cluster, you can create an EKS cluster using [eksctl](https://eksctl.io/) or by following one of the other [Quick Start guides](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html).  For the purposes of this workshop, a small cluster with three `m5.xlarge` nodes should be sufficient.

If you use EKS, make sure you have the [aws-iam-authenticator](https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html) installed as well, unless you have [AWS CLI 1.16.156](https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html) or later.

If you do not yet have Kubeflow installed, follow the [instructions](https://www.kubeflow.org/docs/aws/deploy/install-kubeflow/) to install it on your k8s cluster.

Once your cluster is set up, follow the `IAM Permissions` [instructions](https://github.com/kubeflow/pipelines/tree/master/samples/contrib/aws-samples) to grant the Kubeflow Components permission to access AWS services on your behalf.  Only follow the instructions under the `IAM Permissions` section on this page; we will handle the other steps later in the workshop.

### KFP SDK

Install the [KFP SDK](https://www.kubeflow.org/docs/pipelines/sdk/install-sdk/#install-the-kubeflow-pipelines-sdk).

### Alternative simpler setup

If you want an easier way to deploy an EKS cluster with Kubeflow, you can use this [CloudFormation template](https://github.com/aws-samples/eks-kubeflow-cloudformation-quick-start).

