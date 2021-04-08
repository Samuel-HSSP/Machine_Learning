## Decision Tree Classification
import pandas as pd
dataset = pd.read_csv("dataset.csv")

##print(dataset.head())

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

##print(X)
##print(y)

from sklearn.tree import DecisionTreeClassifier

dtClassifier = DecisionTreeClassifier()

dtClassifier.fit(X_train, y_train)

print(dtClassifier.predict(X_test))

# Accuracy of the model
dtacc = dtClassifier.score(X_test, y_test)
dtacc *= 100
dtaccu = round(dtacc, 2)
dtaccuracy = str(dtaccu)+"%"
print(
f"""
The Accuracy of our model, using the Decision Tree Classifier
{dtaccuracy}
"""
)
