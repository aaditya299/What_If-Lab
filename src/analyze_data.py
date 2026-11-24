import pandas as pd
import numpy as np
data=pd.read_csv("data/raw/students.csv")
correlation=data.corr()
print(correlation)
slope = data["study_hours"].cov(data["exam_score"]) / data["study_hours"].var()
print("\nNaive regression slope:", slope)
print("Actual causal effect: 2.5")
X=np.column_stack((
    np.ones(len(data)),
    data["study_hours"],
    data["motivation"]
))
y=data["exam_score"].to_numpy()
coefficients=np.linalg.lstsq(X,y,rcond=None)[0]
print("\nRegression coefficients:")
print("Intercept:", coefficients[0])
print("Study hours:",coefficients[1])
print("Motivation:",coefficients[2])

print("\nCausal Effect Comparison")
naive_effect = slope
adjusted_effect = coefficients[1]
true_effect = 2.5
print(f"Naive estimate: {naive_effect:.3f}")
print(f"Adjusted estimate: {adjusted_effect:.3f}")
print(f"True effect: {true_effect:.3f}")
print(f"Naive error: {abs(naive_effect - true_effect):.3f}")
print(f"Adjusted error: {abs(adjusted_effect - true_effect):.3f}")