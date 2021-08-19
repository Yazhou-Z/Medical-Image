# https://amaozhao.gitbooks.io/python-real-world-machine-learning/content/Module-1/predictive-modeling/svm-linear-classifier.html
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import xlrd

path = 'D:\XML2SVM\svm\est.xlsx'


def load_excel(path):
    resArray = []
    data = xlrd.open_workbook(path)
    table = data.sheet_by_index(0)
    for i in range(table.nrows):
        line = table.row_values(i)
        resArray.append(line)
    resArray = np.array(resArray)
    return resArray


x = load_excel(path)
print(x.shape)


def readmatrix(x):
    X = []
    y = []

    for i in range(len(x)):
        X.append(x[i][:-1])
        y.append(x[i][-1])

    X = np.array(X)
    y = np.array(y)

    return X, y


X, y = readmatrix(x)
print(y)

# Separate the data into classes based on label
class_0 = np.array([X[i] for i in range(len(X)) if y[i] == '0.0'])
class_1 = np.array([X[i] for i in range(len(X)) if y[i] == '1.0'])


def plot(class_0, class_1):
    plt.figure()
    plt.scatter(
        class_0[:, 0],
        class_0[:, 1],
        facecolors='black',
        edgecolors='black',
        marker='s'
    )
    plt.scatter(
        class_1[:, 0],
        class_1[:, 1],
        facecolors='None',
        edgecolors='black',
        marker='s'
    )
    plt.title('Input data')
    plt.show()


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=5
)

# params = {'kernel': 'linear'}
# params = {'kernel': 'poly', 'degree': 3}
params = {'kernel': 'rbf'}
classifier = SVC(**params)

# training
classifier.fit(X_train, y_train)

# test
y_test_pred = classifier.predict(X_test)

# print
target_names = ['Class-' + str(i) for i in set(y)]
print("\n" + "#" * 30)
print("\nClassifier performance on training dataset\n")
print(classification_report(
    y_train,
    classifier.predict(X_train),
    target_names=target_names)
)
print("#" * 30 + "\n")

print("#" * 30)
print("\nClassification report on test dataset\n")
print(classification_report(y_test, y_test_pred, target_names=target_names))
print("#" * 30 + "\n")