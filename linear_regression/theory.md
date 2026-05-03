# 📈 Linear Regression — Theory & Intuition

---

## 🧠 What is Linear Regression?

Linear Regression is a supervised machine learning algorithm used to model the relationship between:

- **Independent variable(s)** (input features)
- **Dependent variable** (target/output)

It assumes that this relationship is **linear**, meaning it can be represented by a straight line.

---

## 🎯 Goal

The goal of linear regression is to find the best-fitting line that predicts the output variable based on the input features.

---

## 📊 Intuition

Imagine plotting data points on a graph.

👉 Linear Regression tries to draw a straight line such that:
- The line is as close as possible to all data points  
- The prediction error is minimized  

This line is called the **best-fit line**.

---

## 🧮 Mathematical Representation


y = mx + b


Where:
- \( y \) → predicted output  
- \( x \) → input feature  
- \( m \) → slope (weight)  
- \( b \) → intercept (bias)  

---

## 🧩 Multiple Features Case

For multiple input features:

y = w₁x₁ + w₂x₂ + ... + wₙxₙ + b

---

## 📉 Cost Function (Error Measurement)

To measure how well our model is performing, we use a cost function.

The most common one is **Mean Squared Error (MSE)**:

MSE = (1/n) * Σ(yᵢ - ŷᵢ)²


Where:
- yᵢ → actual value  
- ŷ → predicted value  
- n → number of data points  

👉 The goal is to **minimize this error**.

---

## ⚙️ How does it learn?

Linear Regression learns by adjusting parameters:
- weights (slope)  
- bias (intercept)  

This is done using an optimization algorithm like **Gradient Descent**.

---

## 🔽 Gradient Descent (Concept)

- Start with random values of weights and bias  
- Compute prediction error  
- Adjust parameters in the direction that reduces error  
- Repeat until error is minimized  

👉 This process is iterative.

---

## 📌 Assumptions of Linear Regression

1. Linear relationship between input and output  
2. No or little multicollinearity  
3. Homoscedasticity (constant variance of errors)  
4. Errors are normally distributed  

---

## ✅ Advantages

- Simple and easy to understand  
- Fast to train  
- Interpretable  

---

## ⚠️ Limitations

- Cannot capture non-linear relationships  
- Sensitive to outliers  
- Assumes strong conditions on data  

---

## 📍 When to use Linear Regression?

Use it when:
- Relationship is approximately linear  
- You need interpretability  
- Dataset is not too complex  

---

## 🧠 Summary

- Linear Regression models a linear relationship between variables  
- It finds the best-fit line by minimizing error  
- Uses cost functions like MSE  
- Optimized using Gradient Descent  

---