---
title: "SageMaker Job Role"
date: 2020-04-28T09:16:41-06:00
weight: 15
---

The SageMaker jobs created by the Kubeflow Pipeline need permission to access other resources in your AWS account, such as data in S3 buckets.  Run these commands to create a role.

    TRUST="{ \"Version\": \"2012-10-17\", \"Statement\": [ { \"Effect\": \"Allow\", \"Principal\": { \"Service\": \"sagemaker.amazonaws.com\" }, \"Action\": \"sts:AssumeRole\" } ] }"
    aws iam create-role --role-name kfp-example-sagemaker-execution-role --assume-role-policy-document "$TRUST"
    aws iam attach-role-policy --role-name kfp-example-sagemaker-execution-role --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerFullAccess
    aws iam attach-role-policy --role-name kfp-example-sagemaker-execution-role --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
    aws iam get-role --role-name kfp-example-sagemaker-execution-role --output text --query 'Role.Arn'

Note the role ARN returned by the last command.  We'll use it later and refer to it as `ROLE_ARN`.
