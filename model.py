from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class Classifiers():

    @staticmethod
    def Random_Forest(data):
        iris = load_iris()
        X = iris.data
        y = iris.target
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
        clf_forest = RandomForestClassifier(n_estimators=15, max_depth=5)
        clf_forest.fit(X_train, y_train)
        y_pred = clf_forest.predict(X_test)
        accuracy = (accuracy_score(y_test, y_pred)*100)
        return clf_forest.predict(data), accuracy



