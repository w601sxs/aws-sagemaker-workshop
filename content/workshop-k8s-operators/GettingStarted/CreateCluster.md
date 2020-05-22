---
title: "Create Cluster"
date: 2020-04-27T08:19:20-06:00
weight: 25
---

First, install [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl).  

Then, save the YAML snippet below into a file called `ekskubeflow.yaml`.  

    ---
    apiVersion: eksctl.io/v1alpha5
    kind: ClusterConfig

    metadata:
      name: eks-kubeflow
      region: us-east-2

    managedNodeGroups:
    - name: nodegroup
      desiredCapacity: 6
      minSize: 6
      maxSize: 6
      iam:
        withAddonPolicies:
          albIngress: true

On line 7, replace `us-east-2` with your AWS region.

Now, create the cluster.

    eksctl create cluster -f ekskubeflow.yaml

This command takes 5-10 minutes to complete.
