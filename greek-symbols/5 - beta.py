from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([[1], [2], [3], [4]])
y = np.array([40, 55, 70, 85])

model = LinearRegression()
model.fit(x, y)

β = model.coef_[0]  # Slope
α = model.intercept_  # Intercept

print(f"Slope intercept form: y = {β}x + {α}")

hours = np.array([[4.5], [5]])
predicted_score = model.predict(hours)

print(f"Predicted score: {predicted_score}")