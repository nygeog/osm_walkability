import pandas as pd
import numpy as np

inCSV = 'data/processing/walkability_highway_features.csv'

df = pd.read_csv(inCSV)

msk = np.random.rand(len(df)) < 0.8 #split 80/20, 80% for training, 20% for testing
#http://stackoverflow.com/questions/24147278/how-do-i-create-test-and-train-samples-from-one-dataframe-with-pandas
train = df[msk]
test = df[~msk]

print len(df)
print len(train)
print len(test)

test.to_csv('data/machine_learning/test_w_label.csv', index=False)

testDropCols = ['t10walk'] #['health','label']

test = test.drop(testDropCols,axis=1)

train.to_csv('data/machine_learning/train.csv',index=False)
test.to_csv('data/machine_learning/test.csv', index=False)