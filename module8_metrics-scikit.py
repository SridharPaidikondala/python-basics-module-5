import numpy as np
from sklearn.metrics import precision_score, recall_score

N = int(input("Enter the number of points (N): "))

data = np.zeros((N, 2), dtype=int)

for i in range(N):
    print(f"Point {i + 1}:")
    x = int(input("  Enter x (ground truth, 0 or 1): "))
    y = int(input("  Enter y (predicted, 0 or 1): "))
    data[i] = [x, y]

y_true = data[:, 0]
y_pred = data[:, 1]

precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)

print(f"\nPrecision: {precision:.2f}")
print(f"Recall:    {recall:.2f}")
