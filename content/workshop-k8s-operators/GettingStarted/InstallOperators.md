---
title: "Install SageMaker Operators"
date: 2020-04-27T12:52:06-06:00
weight: 45
---

Finally, let's install the SageMaker Operators for kubernetes.  The full installation process is documented [here](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_operators_for_kubernetes.html#namespace-scoped-deployment), but below we have some quick notes to get you started.

## Policy 

Download [trust.json](/files/trust.json), making substitutions as follows:

* AWS account number: use your AWS account number
* EKS Cluster region: use the region your EKS cluster is deployed in
* OIDC ID: Get this from your EKS cluster by running `aws eks describe-cluster --name ${CLUSTER_NAME} --region ${AWS_REGION} --query cluster.identity.oidc.issuer --output text`.  The OIDC ID is the last element in the returned URL.

Now run:

    aws iam create-role --role-name sm_ops_role --assume-role-policy-document file://trust.json --output=text
    aws iam attach-role-policy --role-name sm_ops_role  --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerFullAccess

## Deploy the operators

Download the installation file.

    wget https://raw.githubusercontent.com/aws/amazon-sagemaker-operator-for-k8s/master/release/rolebased/installer.yaml

Edit the file `installer.yaml` and edit the setting for `eks.amazonaws.com/role-arn`, setting the value to the ARN of the role you created in the previous step.  For example:

    eks.amazonaws.com/role-arn: arn:aws:iam::<ACCOUNT>:role/sm_ops_role

Then run:

    kubectl apply -f installer.yaml