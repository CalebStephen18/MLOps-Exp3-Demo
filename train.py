from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron
import joblib
import os

# Load the Iris dataset
iris = load_iris()
# Split the dataset into features and target
X = iris.data
y = iris.target
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Train a Random Forest classifier
clf = Perceptron(max_iter = 5)
clf.fit(X_train, y_train)
# Save the trained model
os.makedirs('model', exist_ok=True)
model_path = os.path.join('model', 'model.joblib')
joblib.dump(clf, model_path)
with open('metrics.txt', 'w') as fw:
  fw.write(f"\nAccuracy: {accuracy_score(y_test, clf.predict(X_test))}")
  fw.write(f"\n{classification_report(y_test,clf.predict(X_test))})
