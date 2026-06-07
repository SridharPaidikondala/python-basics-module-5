# module9_knn_gridsearchcv.py

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

# Read training set size
N = int(input("Enter N (number of training samples): "))

# Create NumPy arrays for training data
X_train = np.zeros((N, 1))
y_train = np.zeros(N, dtype=int)

print("\nEnter training pairs (x, y):")
for i in range(N):
    x = float(input(f"Training sample {i + 1} - x: "))
    y = int(input(f"Training sample {i + 1} - y: "))

    X_train[i, 0] = x
    y_train[i] = y

# Read test set size
M = int(input("\nEnter M (number of test samples): "))

# Create NumPy arrays for test data
X_test = np.zeros((M, 1))
y_test = np.zeros(M, dtype=int)

print("\nEnter test pairs (x, y):")
for i in range(M):
    x = float(input(f"Test sample {i + 1} - x: "))
    y = int(input(f"Test sample {i + 1} - y: "))

    X_test[i, 0] = x
    y_test[i] = y

# Define kNN model
knn = KNeighborsClassifier()

# Hyperparameter grid
param_grid = {
    'n_neighbors': list(range(1, 11))
}

# Grid Search with cross-validation
grid_search = GridSearchCV(
    estimator=knn,
    param_grid=param_grid,
    cv=min(5, N),
    scoring='accuracy'
)

# Train model and find best k
grid_search.fit(X_train, y_train)

best_k = grid_search.best_params_['n_neighbors']

# Best model
best_model = grid_search.best_estimator_

# Predict on test set
y_pred = best_model.predict(X_test)

# Compute accuracy
test_accuracy = accuracy_score(y_test, y_pred)

# Output results
print("\nResults:")
print(f"Best k: {best_k}")
print(f"Test Accuracy: {test_accuracy:.4f}")