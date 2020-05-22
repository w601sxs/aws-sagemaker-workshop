---
title: "Cleanup"
date: 2020-04-28T10:16:11-06:00
weight: 15 
---

If you used an account provided by Event Engine, you do not need to do any cleanup.  The account terminates when the event is over.

If you used your own account, please remove the following resources:

* The SageMaker endpoint you deployed 
* The EKS cluster you created
* The S3 bucket you created
* The Cloud9 IDE (if you used one)

Optionally, you can remove the SageMaker model artifact you created.