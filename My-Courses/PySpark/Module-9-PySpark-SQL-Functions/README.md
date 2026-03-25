# PySpark Data Analysis Assignment

## Objective

By completing this assignment, you will:

* Apply aggregate functions on grouped data
* Use window functions for ranking and analytics
* Work with date & timestamp functions for ETL use cases

---

## Part 1: Data Loading & Setup

### Q1. Spark Session & Data Loading

* Initialize a Spark Session
* Load the dataset (sales_data.csv)
* Infer schema automatically
* Display the schema

### Q2. Data Type Conversion

* Convert order_date into Date format
* Convert order_timestamp into Timestamp format

---

## Part 2: Aggregate Functions

### Q3. Overall Sales Metrics

Compute the following:

* Total sales amount
* Average order amount
* Maximum order amount
* Minimum order amount

### Q4. Region-wise Analysis

For each region:

* Total sales
* Average sales
* Number of orders

### Q5. Customer Count

* Calculate the number of unique customers

### Q6. Product-wise Aggregation

* Aggregate order amounts into a list
* Aggregate distinct order amounts into a set

---

## Part 3: Window Functions – Ranking

### Q7. Regional Ranking

For each region:

* Assign row numbers based on highest order amount
* Assign rank
* Assign dense rank

### Q8. Top Orders per Region

* Identify the top 2 highest orders in each region

---

## Part 4: Window Functions – Analytical

### Q9. Order Comparison per Customer

For each customer:

* Show previous order amount
* Show next order amount

### Q10. Running Total

* Calculate cumulative order amount
* Partition by customer
* Order by date

---

## Part 5: Window Functions – Aggregates

### Q11. Average Order per Customer

* Add a column showing average order amount per customer

### Q12. Maximum Order per Region

* Add a column showing maximum order amount per region

---

## Part 6: Date & Timestamp Functions

### Q13. Date Components Extraction

Extract:

* Year
* Month
* Day

### Q14. Date Difference

* Calculate number of days between current date and order date

### Q15. New Date Columns

Create:

* Order year
* Order month
* Order week

### Q16. Date-based Filtering

* Filter orders placed in March 2023

---

## Part 7: Real-World ETL Scenarios

### Q17. Monthly Sales Trend

* Calculate total sales grouped by year and month

### Q18. Customer Activity Analysis

* Identify customers with more than 2 orders

---

## Summary

This assignment covers:

* Data ingestion and preprocessing
* Aggregations and grouping
* Window functions for ranking and analytics
* Date-time transformations
* Real-world ETL scenarios
