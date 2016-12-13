# from sklearn import a decision tree
from sklearn import tree

# Features contain the input to the classifier
# first element is the weight of the fruit
# second element is if it is bumpy or smooth
# 0 = bumpy   1 = smooth
features = [[140, 1], [130, 1], [150, 0], [170, 0]]

# labels would be the output of the classifier
# to train the algorithm we provide the labels for the features above
# 0 = Apples   1  = oranges
labels = [0, 0, 1, 1]

# Create the decision tree classifier
clf = tree.DecisionTreeClassifier()

# train the desicion tree classifier by passign in the features
# along with the corresponding labels
clf.fit(features, labels)

# pass in features in the format for features used above,
# this will predict based off of the features passed in what fruit it is
if(clf.predict([160,0]) == 1):
    print "Orange"

else:
    print "Apples"
#print clf.predict([160, 0])
