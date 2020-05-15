---
title: "Install Kubeflow"
date: 2020-04-27T08:20:05-06:00
weight: 35
---

First, follow the [aws-iam-authenticator installation instructions](https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html) for your platform.

Download the latest release of [kfctl](https://github.com/kubeflow/kfctl/releases/tag/v1.0.2). (At the time of writing, the latest release was 1.0.2.) This binary will allow you to install Kubeflow on Amazon EKS.

Note that the Kubeflow installation process may change quite often.  If you have trouble installing Kubeflow, please check the latest [installation instructions](https://www.kubeflow.org/docs/aws/deploy/install-kubeflow/).

Follow these steps after you download the `kfctl` binary:

    tar zxf kfctl_<version>.tar.gz
    sudo mv kfctl /usr/local/bin

Now save the following into a file called `kf-install.sh`:

    export AWS_CLUSTER_NAME=eks-kubeflow
    export AWS_REGION=REGION
    export KF_NAME=${AWS_CLUSTER_NAME}

    export BASE_DIR=$HOME/kf_environment
    export KF_DIR=${BASE_DIR}/${KF_NAME}

    export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_aws.v1.0.2.yaml"

    export CONFIG_FILE=${KF_DIR}/kfctl_aws.yaml
  
On line 2 of that file, replace `REGION` with your AWS region.

Now run:

    source kf-install.sh
    mkdir -p ${KF_DIR}
    cd ${KF_DIR}
    wget -O kfctl_aws.yaml $CONFIG_URI

Make the following changes to `kfctl_aws.yaml`:

* Replace the default region (`us-west-2`) with the region you are working in
* On the line immediately after the region, add `enablePodIamPolicy: true`
* Replace the default cluster name (`kubeflow-aws`) with `eks-kubeflow`
* Comment out the line starting with `roles` and the line immediately after it

After making these changes, your `kfctl_aws.yaml` file should look like this:

    apiVersion: kfdef.apps.kubeflow.org/v1
    kind: KfDef
    metadata:
      namespace: kubeflow
    spec:
      applications:
      - kustomizeConfig:
          parameters:
          - name: namespace
            value: istio-system
          repoRef:
            name: manifests
            path: istio/istio-crds
        name: istio-crds
      - kustomizeConfig:
          parameters:
          - name: namespace
            value: istio-system
          repoRef:
            name: manifests
            path: istio/istio-install
        name: istio-install
      - kustomizeConfig:
          parameters:
          - name: namespace
            value: istio-system
          repoRef:
            name: manifests
            path: istio/cluster-local-gateway
        name: cluster-local-gateway
      - kustomizeConfig:
          parameters:
          - name: clusterRbacConfig
            value: 'OFF'
          repoRef:
            name: manifests
            path: istio/istio
        name: istio
      - kustomizeConfig:
          parameters:
          - name: namespace
            value: istio-system
          repoRef:
            name: manifests
            path: istio/add-anonymous-user-filter
        name: add-anonymous-user-filter
      - kustomizeConfig:
          repoRef:
            name: manifests
            path: application/application-crds
        name: application-crds
      - kustomizeConfig:
          overlays:
          - application
          repoRef:
            name: manifests
            path: application/application
        name: application
      - kustomizeConfig:
          parameters:
          - name: namespace
            value: cert-manager
          repoRef:
            name: manifests
            path: cert-manager/cert-manager-crds
        name: cert-manager-crds
      - kustomizeConfig:
          parameters:
          - name: namespace
            value: kube-system
          repoRef:
            name: manifests
            path: cert-manager/cert-manager-kube-system-resources
        name: cert-manager-kube-system-resources
      - kustomizeConfig:
          overlays:
          - self-signed
          - application
          parameters:
          - name: namespace
            value: cert-manager
          repoRef:
            name: manifests
            path: cert-manager/cert-manager
        name: cert-manager
      - kustomizeConfig:
          repoRef:
            name: manifests
            path: metacontroller
        name: metacontroller
      - kustomizeConfig:
          overlays:
          - istio
          - application
          repoRef:
            name: manifests
            path: argo
        name: argo
      - kustomizeConfig:
          repoRef:
            name: manifests
            path: kubeflow-roles
        name: kubeflow-roles
      - kustomizeConfig:
          overlays:
          - istio
          - application
          repoRef:
            name: manifests
            path: common/centraldashboard
        name: centraldashboard
      - kustomizeConfig:
          overlays:
          - application
          repoRef:
            name: manifests
            path: admission-webhook/webhook
        name: webhook
      - kustomizeConfig:
          overlays:
          - application
          parameters:
          - name: webhookNamePrefix
            value: admission-webhook-
          repoRef:
            name: manifests
            path: admission-webhook/bootstrap
        name: bootstrap
      - kustomizeConfig:
          overlays:
          - istio
          - application
          parameters:
          - name: userid-header
            value: kubeflow-userid
          repoRef:
            name: manifests
            path: jupyter/jupyter-web-app
        name: jupyter-web-app
      - kustomizeConfig:
          overlays:
          - application
          repoRef:
            name: manifests
            path: spark/spark-operator
        name: spark-operator
      - kustomizeConfig:
          overlays:
          - istio
          - application
          - db
          repoRef:
            name: manifests
            path: metadata
        name: metadata
      - kustomizeConfig:
          overlays:
          - istio
          - application
          repoRef:
            name: manifests
            path: jupyter/notebook-controller
        name: notebook-controller
      - kustomizeConfig:
          overlays:
          - application
          repoRef:
            name: manifests
            path: pytorch-job/pytorch-job-crds
        name: pytorch-job-crds
      - kustomizeConfig:
          overlays:
          - application
          repoRef:
            name: manifests
            path: pytorch-job/pytorch-operator
        name: pytorch-operator
      - kustomizeConfig:
          overlays:
          - application
          parameters:
          - name: namespace
            value: knative-serving
          repoRef:
            name: manifests
            path: knative/knative-serving-crds
        name: knative-crds
      - kustomizeConfig:
          overlays:
          - application
          parameters:
          - name: namespace
            value: knative-serving
          repoRef:
            name: manifests
            path: knative/knative-serving-install
        name: knative-install
      - kustomizeConfig:
          overlays:
          - application
          repoRef:
            name: manifests
            path: kfserving/kfserving-crds
        name: kfserving-crds
      - kustomizeConfig:
          overlays:
          - application
          repoRef:
            name: manifests
            path: kfserving/kfserving-install
        name: kfserving-install
      - kustomizeConfig:
          overlays:
          - application
          parameters:
          - name: usageId
            value: <randomly-generated-id>
          - name: reportUsage
            value: 'true'
          repoRef:
            name: manifests
            path: common/spartakus
        name: spartakus
      - kustomizeConfig:
          overlays:
          - istio
          repoRef:
            name: manifests
            path: tensorboard
        name: tensorboard
      - kustomizeConfig:
          overlays:
          - application
          repoRef:
            name: manifests
            path: tf-training/tf-job-crds
        name: tf-job-crds
      - kustomizeConfig:
          overlays:
          - application
          repoRef:
            name: manifests
            path: tf-training/tf-job-operator
        name: tf-job-operator
      - kustomizeConfig:
          overlays:
          - application
          repoRef:
            name: manifests
            path: katib/katib-crds
        name: katib-crds
      - kustomizeConfig:
          overlays:
          - application
          - istio
          repoRef:
            name: manifests
            path: katib/katib-controller
        name: katib-controller
      - kustomizeConfig:
          overlays:
          - application
          repoRef:
            name: manifests
            path: pipeline/api-service
        name: api-service
      - kustomizeConfig:
          overlays:
          - application
          parameters:
          - name: minioPvcName
            value: minio-pv-claim
          repoRef:
            name: manifests
            path: pipeline/minio
        name: minio
      - kustomizeConfig:
          overlays:
          - application
          parameters:
          - name: mysqlPvcName
            value: mysql-pv-claim
          repoRef:
            name: manifests
            path: pipeline/mysql
        name: mysql
      - kustomizeConfig:
          overlays:
          - application
          repoRef:
            name: manifests
            path: pipeline/persistent-agent
        name: persistent-agent
      - kustomizeConfig:
          overlays:
          - application
          repoRef:
            name: manifests
            path: pipeline/pipelines-runner
        name: pipelines-runner
      - kustomizeConfig:
          overlays:
          - istio
          - application
          repoRef:
            name: manifests
            path: pipeline/pipelines-ui
        name: pipelines-ui
      - kustomizeConfig:
          overlays:
          - application
          repoRef:
            name: manifests
            path: pipeline/pipelines-viewer
        name: pipelines-viewer
      - kustomizeConfig:
          overlays:
          - application
          repoRef:
            name: manifests
            path: pipeline/scheduledworkflow
        name: scheduledworkflow
      - kustomizeConfig:
          overlays:
          - application
          repoRef:
            name: manifests
            path: pipeline/pipeline-visualization-service
        name: pipeline-visualization-service
      - kustomizeConfig:
          overlays:
          - application
          - istio
          repoRef:
            name: manifests
            path: profiles
        name: profiles
      - kustomizeConfig:
          overlays:
          - application
          repoRef:
            name: manifests
            path: seldon/seldon-core-operator
        name: seldon-core
      - kustomizeConfig:
          overlays:
          - application
          repoRef:
            name: manifests
            path: mpi-job/mpi-operator
        name: mpi-operator
      - kustomizeConfig:
          overlays:
          - application
          parameters:
          - name: clusterName
            value: eks-kubeflow
          repoRef:
            name: manifests
            path: aws/aws-alb-ingress-controller
        name: aws-alb-ingress-controller
      - kustomizeConfig:
          overlays:
          - application
          repoRef:
            name: manifests
            path: aws/nvidia-device-plugin
        name: nvidia-device-plugin
      plugins:
      - kind: KfAwsPlugin
        metadata:
          name: aws
        spec:
          auth:
            basicAuth:
              password:
                name: password
              username: admin
          region: <REGION>
          enablePodIamPolicy: true
          #roles:
          #- eksctl-kubeflow-aws-nodegroup-ng-a2-NodeInstanceRole-xxxxxxx
      repos:
      - name: manifests
        uri: https://github.com/kubeflow/manifests/archive/v1.0.2.tar.gz
      version: v1.0.2


Finally, run:

    kfctl apply -V -f ${CONFIG_FILE}

Verify the installation status by running:

    kubectl -n kubeflow get all

Installing Kubeflow and its toolset may take 2 - 3 minutes. A few pods may initially give `Error` or `CrashLoopBackOff` status. Eventually they will auto-heal and come to a `Running` state.

## Install SageMaker logs plugin

Download the binary and install it.  On Linux:

    wget https://amazon-sagemaker-operator-for-k8s-us-east-1.s3.amazonaws.com/kubectl-smlogs-plugin/v1/linux.amd64.tar.gz
    tar zxf linux.amd64.tar.gz
    sudo cp ./kubectl-smlogs.linux.amd64/kubectl-smlogs /usr/local/bin

On Mac:

    wget https://amazon-sagemaker-operator-for-k8s-us-east-1.s3.amazonaws.com/kubectl-smlogs-plugin/v1/darwin.amd64.tar.gz
    tar zxf darwin.amd64.tar.gz
    sudo cp ./kubectl-smlogs.darwin.amd64/kubectl-smlogs /usr/local/bin