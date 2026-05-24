import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# --- Step 1: Read N ---
while True:
    try:
        N = int(input("Enter N (number of points, positive integer): "))
        if N > 0:
            break
        print("N must be a positive integer. Try again.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# --- Step 2: Read k ---
while True:
    try:
        k = int(input("Enter k (number of neighbors, positive integer): "))
        if k > 0:
            break
        print("k must be a positive integer. Try again.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# --- Step 3: Read N (x, y) points using NumPy ---
# Initialize arrays with NumPy
X_train = np.empty(N, dtype=float)
y_train = np.empty(N, dtype=float)

print(f"\nEnter {N} point(s) one by one (x then y for each):")
for i in range(N):
    while True:
        try:
            x_val = float(input(f"  Point {i + 1} - x: "))
            break
        except ValueError:
            print("  Invalid input. Please enter a real number.")
    while True:
        try:
            y_val = float(input(f"  Point {i + 1} - y: "))
            break
        except ValueError:
            print("  Invalid input. Please enter a real number.")
    X_train[i] = x_val
    y_train[i] = y_val

# --- Step 4: Variance of labels in the training dataset ---
label_variance = np.var(y_train)
print(f"\nVariance of labels (y) in the training dataset: {label_variance:.6f}")

# --- Step 5: Check k <= N, then run k-NN Regression ---
if k > N:
    print(f"\nError: k ({k}) must be less than or equal to N ({N}). "
          f"Cannot run k-NN with more neighbors than training points.")
else:
    while True:
        try:
            X_query = float(input("\nEnter X value to predict Y: "))
            break
        except ValueError:
            print("Invalid input. Please enter a real number.")

    # Scikit-learn expects 2D arrays for X
    X_train_2d = X_train.reshape(-1, 1)
    X_query_2d = np.array([[X_query]])

    # Fit k-NN Regressor using Scikit-learn
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_train_2d, y_train)

    # Predict
    y_pred = knn.predict(X_query_2d)[0]

    print(f"\nk-NN Regression Result:")
    print(f"  Input  X = {X_query}")
    print(f"  k      = {k}")
    print(f"  Output Y = {y_pred:.6f}")
