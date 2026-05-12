import numpy as np


class KNNRegression:
    def __init__(self):
        self.x_points = np.array([])
        self.y_points = np.array([])

    def insert_points(self, x, y):
        self.x_points = np.append(self.x_points, x)
        self.y_points = np.append(self.y_points, y)

    def predict(self, x_value, k):
        n = len(self.x_points)

        if k > n:
            return "Error: k should be less than or equal to N"

        # Calculate distances
        distances = np.abs(self.x_points - x_value)

        # Get indices of k nearest neighbors
        nearest_indices = np.argsort(distances)[:k]

        # Calculate average of corresponding y values
        prediction = np.mean(self.y_points[nearest_indices])

        return prediction


# Read N
n = int(input("Enter number of points (N): "))

# Read k
k = int(input("Enter value of k: "))

# Create object
knn = KNNRegression()

# Read points
for i in range(n):
    x = float(input("Enter x value: "))
    y = float(input("Enter y value: "))
    knn.insert_points(x, y)

# Read X for prediction
x_input = float(input("Enter X value for prediction: "))

# Output prediction
result = knn.predict(x_input, k)

print("Result:", result)