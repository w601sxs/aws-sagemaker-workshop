---
title: "Dashboard"
date: 2020-04-27T08:30:42-06:00
weight: 5
---

Use `port-forward` to access the Kubeflow dashboard.

    kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80

You can now access the dashboard at [localhost:8080](http://localhost:8080) if you are running on your own machine.  If you are running in Cloud9, click `Preview -> Preview running application`.   You must leave the `port-forward` command running in order to use the dashboard.  In a production environment, we'd change the dashboard to use a load balancer with authentication, but port forwarding is fine for development purposes.

Once you have the dashboard open, click `Start Setup` and enter `smoperators` for the Namespace Name.  After clicking `Finish`, if the dashboard does not appear, refresh the page.  Finally, select the `smoperators` namespace using the drop-down at the top of the page.
