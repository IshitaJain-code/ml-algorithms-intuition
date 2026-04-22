# @ ml-algorithms-intuition
From-scratch implementations of core ML algorithms with mathematical intuition, NumPy-based code, and real-world examples.

# 🧠 Machine Learning Algorithms From Scratch

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![NumPy](https://img.shields.io/badge/NumPy-Used-orange)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

> A structured collection of Machine Learning algorithms implemented from scratch using NumPy, with clear intuition, mathematical explanations, and practical examples.

---

## 🚀 Overview

This repository focuses on building core Machine Learning algorithms **from scratch**, without relying on high-level libraries like `scikit-learn`.

The goal is to:
- Understand the **internal working** of ML algorithms  
- Strengthen **mathematical intuition**  
- Write **clean and modular code**  
- Prepare for **ML interviews and real-world applications**  

---

## 📂 Repository Structure
ml-from-scratch/
│
├── linear_regression/
├── logistic_regression/
├── knn/
├── decision_tree/
├── kmeans/
│
├── utils/
└── README.md


Each algorithm includes:
- 📘 `theory.md` → intuition + math  
- ⚙️ `implementation.py` → from-scratch code  
- 📊 `example.ipynb` → visualization and usage  

---

## 🧩 Algorithms Implemented

### 🔹 Supervised Learning
- Linear Regression
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Trees

### 🔹 Unsupervised Learning
- K-Means Clustering

### 🔜 Coming Soon
- Naive Bayes  
- PCA  
- Support Vector Machines (SVM)  

---

## ⚙️ Tech Stack

- Python  
- NumPy  
- Matplotlib  
- Jupyter Notebook  

---

## 📊 Example Usage

```python
from linear_regression import LinearRegression

model = LinearRegression(lr=0.01, epochs=1000)
model.fit(X, y)
predictions = model.predict(X)
