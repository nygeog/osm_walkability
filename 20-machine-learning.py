import pandas as pd
import numpy as np
# from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier, AdaBoostClassifier #try xg boost
# from sklearn.linear_model import SGDClassifier
# from sklearn.cross_validation import cross_val_score
# from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeRegressor
from datetime import datetime
from sklearn import metrics
 
print datetime.now()
 
wd = 'data/'

def one_hot(D, index_dict=None, num_indexes=-1):
    # dictionary D.column -> value -> index in output
    if index_dict is None:
        idx = 0
        index_dict = {}
        for c in D.columns:
            index_dict[c] = {}
            s = set(D[c])
            if len(s) > 2:
                for col in s:
                    index_dict[c][col] = idx
                    idx += 1
            elif len(s) == 2:
                s = list(s)
                index_dict[c][s[0]] = idx
                index_dict[c][s[1]] = idx + 1
                idx += 2
            else:
                pass
                # do nothing, this column only has 1 value, can't be used for prediction
        num_indexes = idx
 
    X = np.zeros((len(D), num_indexes))
    for i in xrange(len(D)):
        row = D.iloc[i]
        for c in D.columns:
            val = row[c]
            if val in index_dict[c]:
                j = index_dict[c][val]
                X[i,j] = 1
    return X, index_dict, num_indexes
 
 
def main():
    data = pd.read_csv(wd + 'machine_learning/train.csv').astype(np.float32)
    data = data.replace(np.inf, 0)
    data = data.drop('geoid',axis=1)
    data = data.fillna(data.mean())
    
    print data.dtypes
    t0 = datetime.now()
    #X, index_dict, num_indexes = one_hot(data[data.columns[:-1]])
    X = data[data.columns.difference(['t10walk'])]
    print "one hot training set time:", (datetime.now() - t0)
    Y = data['t10walk']
 
    #clf = SGDClassifier() #Ran this
 
    # fit here
    # TRY THIS RANDOM FOREST AT 700
    # Maybe try SGD or kernel approximation
    # http://scikit-learn.org/stable/tutorial/machine_learning_map/
    #clf = RandomForestClassifier(n_estimators=700)
    #clf = ExtraTreesClassifier()
    clf = DecisionTreeRegressor()
 
     
 
    #Try This:
    #sklearn.kernel_approximation.RBFSampler
 
     
    print datetime.now()
 
    t0 = datetime.now()
    clf.fit(X, Y)
    print "training time:", (datetime.now() - t0)
    # print "training accuracy:", clf.score(X, Y)
 
    #quiz = pd.read_csv('quiz.csv')
    quiz = pd.read_csv(wd+'machine_learning/test.csv').astype(np.float32)
    quiz = quiz.drop('geoid',axis=1)
    quiz = quiz.replace(np.inf, 0)
    quiz = quiz.fillna(quiz.mean())

    for i in quiz.dtypes:
        print i


    t0 = datetime.now()
    # Xtest, _, _ = one_hot(quiz, index_dict, num_indexes)
    Xtest = quiz[quiz.columns.difference(['t10walk'])]
    #from IPython import embed 
    #embed()
    print "one hot test set time:", (datetime.now() - t0)
    # do prediction and save it
    prediction = clf.predict(Xtest)
 
    ftime = str(datetime.now()).replace(' ','-').replace(':','-').replace('.','-')
    print ftime
 
    with open(wd+'machine_learning/output/myoutput-'+ftime+'.csv', 'w') as f:
        f.write('id,prediction\n')
        the_id = 1
        for p in prediction:
            f.write("%s,%s\n" % (the_id, p))
            the_id += 1
 
    # print 'cross validating...'
    # scores = cross_val_score(clf, X, Y, cv=5)
    # print scores
 
    #print prediction.score(X, Y)
    importance = pd.DataFrame(zip(data.columns.difference(['t10walk']), clf.feature_importances_) )
    importance.columns = ['feature', 'importance']
    importance = importance.sort_values('importance',ascending=False)
    importance.to_csv(wd+'machine_learning/output/myoutput-'+ftime+'_importances.csv', index=False)
    print(clf.feature_importances_)
 
if __name__ == '__main__':
    main()

