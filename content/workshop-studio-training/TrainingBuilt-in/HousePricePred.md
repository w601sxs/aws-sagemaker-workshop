---
title: "House Price Prediction"
chapter: false
weight: 120 
---

This section walks you through training your first model using Amazon SageMaker. You use notebooks and training algorithms provided by Amazon SageMaker.

This notebook describes using machine learning (ML) for predicting price of house. We use the Boston Housing dataset, present in Scikit-Learn: <https://scikit-learn.org/stable/datasets/index.html#boston-dataset.>

The method that we'll use is a linear regressor. Amazon SageMaker's __Linear Learner__ algorithm extends upon typical linear models by training many models in parallel, in a computationally efficient manner. Each model has a different set of hyperparameters, and then the algorithm finds the set that optimizes a specific criteria. This can provide substantially more accurate models than typical linear algorithms at the same, or lower, cost.

1. Access the SageMaker Studio you started earlier.
2. On the left sidebar, navigate into `MLAI/built-in-algorithms` , double click on `linearLearner_boston_house.ipynb` to open it.
3. You are now ready to begin the notebook.
4. You also need to specify the S3 bucket and prefix that you want to use for training and model data. This should be within the same region as the Notebook Instance, training, and hosting.

    * Create a bucket for this notebook (ie: "house-price-CURRENTDATE")
        * You can do that in the terminal of the Jupyter Notebook with this:

        ```bash
        aws s3api create-bucket --bucket house-price-`date +%s`
        ```

        * Copy the bucket name for future references.
5. In the notebook, set the bucket name. Change the bucket name to some of your own in the notebook and from then it can run without modifications.

    > To train the model in this notebook, you will use the `Amazon SageMaker Python SDK` which abstracts several implementation details, and is easy to use.


    ```python
    container = get_image_uri(boto3.Session().region_name, 'linear-learner')
    ll = sagemaker.estimator.Estimator(container,
                                    train_instance_count=1, 
                                    train_instance_type='ml.m4.xlarge',
                                    ...)
    ll.set_hyperparameters(feature_dim=13,
                            predictor_type='regressor',
                            mini_batch_size=100)
    ll.fit({'train': s3_input_train, 'validation': s3_input_validation})
    ``` 

6. Run each cell of the notebook.
