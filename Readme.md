# Movie Analysis Project

# Overview
This project explores a dataset of movies and performs an in-depth analysis of budget, revenue, movie franchises, directors, and trends over time.

The goal is to uncover insights such as:
* Which franchises perform best
* Budget vs. revenue relationships
* Trends across decades
* Top-performing directors
* Yearly averages and patterns

All analysis is conducted inside the Movie_Analysis.ipynb Jupyter Notebook.

# Project Structure

├── Movie_Analysis.ipynb   # Main analysis notebook
└── README.md              # Project documentation

# Requirements

Make sure you have Python 3.9+ installed.

Install dependencies:

```bash
pip install pandas numpy matplotlib,os,request
```

(Optional but common):

```bash
pip install seaborn
```

---

# Key Analysis Steps

# Data Loading & Cleaning

* Load raw dataset (CSV)
* Handle missing values
* Convert date columns to datetime
* Compute additional features (profit, decade, etc.)

# Exploratory Data Analysis (EDA)

* Summary statistics
* Correlation between budget and revenue
* Visualization of distributions

# Franchise Analysis

* Group movies by franchise
* Calculate:

  * total movie count
  * average budget
  * total revenue
  * average revenue

# Director Analysis

* Rank directors based on:

  * number of movies
  * total revenue
  * average revenue

# 5. Yearly Trends

* Compute yearly means for:

  * budget
  * revenue
* Plot trends using line charts

# Insights & Conclusions

Examples:

* Which franchises are most profitable
* Changes in movie spending over the years
* Revenue evolution

---

# Sample Visualizations

The notebook generates plots such as:

* Yearly Average Revenue
* Yearly Average Budget
* Correlation plots (budget vs revenue)
* Top 5 franchises/directors

---

# How to Run

1. Open Jupyter Notebook:

   ```bash
   jupyter notebook
   ```
2. Navigate to:

   ```
   Movie_Analysis.ipynb
   ```
3. Run all cells:

   * Kernel → Restart & Run All

---

# Contributing

Feel free to fork the project or suggest improvements
