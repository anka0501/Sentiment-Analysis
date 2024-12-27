import kagglehub
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("jp797498e/twitter-entity-sentiment-analysis")

print("Path to dataset files:", path)

train = pd.read_csv(path + '\\twitter_training.csv')
val = pd.read_csv(path + '\\twitter_validation.csv')

train.columns = ['id', 'entity', 'sentiment', 'tweet']
print(train.head())

# check nulls in colums
print(train[['sentiment', 'tweet']].isnull().sum())

print()

#https://www.kaggle.com/code/jvrco22/twitter-sentiment-analysis-96-val-acc