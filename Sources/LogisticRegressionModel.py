## Logistic Regression Classification
import pandas as pd
dataset = pd.read_csv("dataset.csv")

##print(dataset.head())

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

##print(X)
##print(y)

from sklearn.model_selection import train_test_split as tts

X_train, X_test, y_train, y_test = tts(X, y, test_size=0.3, random_state=0)

from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression(random_state=0, solver='lbfgs')

classifier.fit(X_train, y_train)

print(classifier.predict(X_test))

# Accuracy of the model
acc = classifier.score(X_test, y_test)
acc *= 100
accu = round(acc, 2)
accuracy = str(accu)+"%"
print(
f"""
The Accuracy of our model, using the Logistic Regression Classifier
{accuracy}
"""
)
