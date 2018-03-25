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

#### Notes
- Maybe fix unbalanced data with XGBoost/LGB by: 'scale_pos_weight':99
- See nice features from: https://www.kaggle.com/pranav84/lightgbm-fixing-unbalanced-data/code

