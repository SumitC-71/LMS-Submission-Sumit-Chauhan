# E-Commerce Analytics & Data Engineering System
## Overview
You are tasked with building a PySpark data processing pipeline for an e-commerce analytics company. The goal of this assignment is to evaluate your proficiency in Apache Spark, including DataFrame APIs, data cleaning, partitioning strategies, and distributed aggregations by simulating a real-world data engineering workflow.

## Assumptions & Scope
To ensure consistency and technical accuracy, please follow these explicit assumptions while implementing the system:

The system will be written using Python (PySpark) and executed in Local Spark Mode (local[*]).

Data must be processed using SparkSession and DataFrame APIs; RDDs should be avoided unless necessary.
Input involves multiple CSV files which may contain missing values, duplicates, or malformed records.
Programmatic handling of empty files and schema enforcement is required.
The Spark Web UI (http://localhost:4040) should be used to observe execution stages and tasks.
## Functional Requirements
### 1. Spark Application Setup
    The application must initialize a valid environment:

    Create a SparkSession with a clear application name.

    Explicitly configure the master URL to local mode.

### 2. Data Ingestion & Validation
    Validation Logic: Separate valid records from invalid/malformed records.

    Audit: Report the total number of records vs. incomplete records.

    Schema: Enforce an explicit schema (StructType) during the ingestion of valid data.

### 3. Data Cleaning & Standardization
    Apply transformations to ensure data readiness:

    Null Handling: Remove or impute missing values.

    Deduplication: Identify and remove duplicate transaction records.

    Standardization: Normalize inconsistent category values and cast columns to correct numeric/timestamp types.

### 4. Partitioning & Performance
    Demonstrate awareness of Spark’s distributed architecture:

    Inspect and modify the number of partitions to optimize parallel processing.

    Use coalesce() or repartition() appropriately to reduce partitions before writing.

    Implement caching or persistence only for DataFrames reused in multiple actions.

### 5. Business Analytics & Aggregations
    Generate the following reports using distributed operations:

    Total Revenue: Calculated per country.

    Top Performers: Identify the top 5 products by total revenue.

    Platform Metrics: Average order value per platform.

    Trends: Daily transaction count trends.

### 6. Data Integration & Advanced Features
    Join Operations: Join transactional data with a reference dataset (Product name, Brand) using optimization techniques like Broadcast Joins.

    Tracking: Utilize Accumulators to track specific metrics (e.g., total invalid records) across the cluster.

### 7. Output Management
    Write the final processed dataset to the local filesystem.

    The output must use a columnar storage format.

    Partitioning: Organize the output folder by a logical business column.

    Deliverables
    One PySpark File: A .py script or a Jupyter Notebook containing the complete pipeline logic.

