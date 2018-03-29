# Kaggle comp

#### Ideas/Thoughts
- Cluster/generate a latent representation of feature IP
- Cluster/generate a latent representation of feature APP
- Cluster/generate a latent representation of feature CHANNEL
- Test dilated convolutional networks (see: https://www.kaggle.com/alexanderkireev/deep-learning-support-966/output)
- Feature ideas: Aggregations, time-related features,
- Autoencoders (to create ensamble of multiple time series) (over time?)
- For splitting the dataset into train/test, maybe use: http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html
- Because of unbalanced classes, maybe train an autoencoder on the 0-samples, and use the error with a threshold to predict 0/1
- ip_app count
- device_app count
- hourly user count (user = device + ip)
- Bag features (if user 1 use APP1 and APP2, group APP1 and APP2)
e.g. this will be user_app_bag. This makes it easier to 'categorize' each user

- CLICK HISTORY! History could be bagged based on app as well. This could be awesome:

| label | user | history |
|-------|------|---------|
| 0	| user1 | |
| 1	| user1 |0 |
| 1	| user1 | 01 |
| 0 | user1 | 011 |


#### Notes
- Maybe fix unbalanced data with XGBoost/LGB by: 'scale_pos_weight':99
- See nice features from: https://www.kaggle.com/pranav84/lightgbm-fixing-unbalanced-data/code
- See this one for a winning solution for a similar comp.: https://www.csie.ntu.edu.tw/~r01922136/slides/kaggle-avazu.pdf

