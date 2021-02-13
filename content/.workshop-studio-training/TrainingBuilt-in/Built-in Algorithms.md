---
title: "Built-in Algorithms"
chapter: false
weight: 110 
---


Amazon SageMaker provides several built-in machine learning algorithms that you can use for a variety of problem types.

| Algorithm                                    | Task                                               |
|----------------------------------------------|----------------------------------------------------|
| BlazingText                                  | Word2vec and text classification                   |
| DeepAR Forecasting                           | forecasting scalar time series                     |
| Factorization Machines                       | discrete recommendations                           |
| Image Classification                         | to classify images                                 |
| IP Insights                                  | learning the usage patterns for IPv4 addresses     |
| K-Means                                      | clustering                                         |
| K-Nearest Neighbors (k-NN)                   | classification or regression                       |
| Latent Dirichlet Allocation (LDA)            | topic modeling                                     |
| Linear Learner                               | discrete classification or quantitative prediction |
| Neural Topic Model (NTM)                     | topic modeling                                     |
| Object2Vec                                   | neural embeddings of high-dimensional objects      |
| Object Detection                             | to detect and classify objects in images           |
| Principal Component Analysis (PCA)           | dimensionality reduction                           |
| Random Cut Forest (RCF)                      | detecting anomalous data points                    |
| Semantic Segmentation                        | classification of every pixel in an image          |
| Sequence-to-Sequence                         | neural machine translation                         |
| XGBoost                                      | discrete classification or quantitative prediction |

Amazon SageMaker provides containers for its built-in algorithms. However, containers are used behind the scenes when you use one of the Amazon SageMaker built-in algorithms, so you do not deal with them directly. You can train and deploy these algorithms from the Amazon SageMaker console, the AWS Command Line Interface (AWS CLI), a Python notebook, or the Amazon SageMaker Python SDK.

In this workshop, we will use some of these algorithms using Python notebooks.
