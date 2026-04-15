from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

raise Exception("Intentional failure for pipeline test")

data = load_iris()
X = data.data
y = data.target
