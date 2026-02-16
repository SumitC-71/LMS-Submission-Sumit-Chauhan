----------------------- case study #4 ----------------------------

-- tables and related data for Data bank case study:
-- https://www.db-fiddle.com/f/2GtQz4wZtuNNu7zXH5HtV4/3

SET search_path='data_bank';

SELECT * FROM regions;

SELECT * FROM customer_nodes
WHERE customer_id <= 2;

SELECT * FROM customer_transactions
WHERE customer_id <= 2
ORDER BY customer_id;

----------------- Section A. Customer Nodes Exploration -----------------

-- 1. How many unique nodes are there on the Data Bank system?
SELECT 
    COUNT(DISTINCT node_id) AS unique_node_count
FROM customer_nodes;

-- 2. What is the number of nodes per region?
SELECT 
    r.region_id,
    COUNT(DISTINCT c.node_id) AS total_nodes_per_region
FROM regions r
LEFT JOIN customer_nodes c 
    ON r.region_id = c.region_id
GROUP BY r.region_id
ORDER BY r.region_id;

-- 3. How many customers are allocated to each region?
SELECT 
    region_id,
    COUNT(DISTINCT customer_id) AS customer_count
FROM customer_nodes
GROUP BY region_id
ORDER BY region_id;

-- 4. How many days on average are customers reallocated to a different node?
SELECT 
    ROUND(AVG(end_date - start_date), 2) AS avg_days_customer_reallocated
FROM customer_nodes
WHERE end_date <> '9999-12-31';

-- 5. What is the median, 80th and 95th percentile for this same reallocation days metric for each region?
SELECT
    region_id,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY end_date - start_date) 
        AS median_days,
    PERCENTILE_CONT(0.8) WITHIN GROUP (ORDER BY end_date - start_date) 
        AS percentile_80_days,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY end_date - start_date) 
        AS percentile_95_days
FROM customer_nodes
WHERE end_date <> '9999-12-31'
GROUP BY region_id
ORDER BY region_id;


----------------- B. Customer Transactions -----------------
-- 1. What is the unique count and total amount for each transaction type?
SELECT 
    txn_type,
    COUNT(*) AS transaction_count,
    SUM(txn_amount) AS total_amount
FROM customer_transactions
GROUP BY txn_type
ORDER BY txn_type;


-- 2. What is the average total historical deposit counts and amounts for all customers?
WITH customer_deposits AS (
    SELECT 
        customer_id,
        COUNT(*) AS deposit_count,
        SUM(txn_amount) AS deposit_amount
    FROM customer_transactions
    WHERE txn_type = 'deposit'
    GROUP BY customer_id
)

SELECT 
    ROUND(AVG(deposit_count), 2) AS avg_deposit_count,
    ROUND(AVG(deposit_amount), 2) AS avg_deposit_amount
FROM customer_deposits;

-- 3. For each month - how many Data Bank customers make more than 1 deposit and either 1 purchase or 1 withdrawal in a single month?
WITH monthly_summary AS (
    SELECT 
        customer_id,
        DATE_TRUNC('month', txn_date) AS month_start,
        SUM(CASE WHEN txn_type = 'deposit' THEN 1 ELSE 0 END) AS deposit_count,
        SUM(CASE WHEN txn_type = 'purchase' THEN 1 ELSE 0 END) AS purchase_count,
        SUM(CASE WHEN txn_type = 'withdrawal' THEN 1 ELSE 0 END) AS withdrawal_count
    FROM customer_transactions
    GROUP BY customer_id, DATE_TRUNC('month', txn_date)
)

SELECT 
    month_start,
    COUNT(*) AS customer_count
FROM monthly_summary
WHERE deposit_count > 1
  AND (purchase_count >= 1 OR withdrawal_count >= 1)
GROUP BY month_start
ORDER BY month_start;

-- 4. What is the closing balance for each customer at the end of the month?
WITH monthly_net AS (
    SELECT 
        customer_id,
        DATE_TRUNC('month', txn_date) AS month_start,
        SUM(
            CASE 
                WHEN txn_type = 'deposit' THEN txn_amount
                WHEN txn_type IN ('withdrawal', 'purchase') THEN -txn_amount
            END
        ) AS monthly_change
    FROM customer_transactions
    GROUP BY customer_id, DATE_TRUNC('month', txn_date)
)

SELECT 
    customer_id,
    month_start,
    SUM(monthly_change) OVER (
        PARTITION BY customer_id
        ORDER BY month_start
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS closing_balance
FROM monthly_net
ORDER BY customer_id, month_start;

-- 5. What is the percentage of customers who increase their closing balance by more than 5%?
WITH monthly_net AS (
    SELECT 
        customer_id,
        DATE_TRUNC('month', txn_date) AS month_start,
        SUM(
            CASE 
                WHEN txn_type = 'deposit' THEN txn_amount
                WHEN txn_type IN ('withdrawal', 'purchase') THEN -txn_amount
            END
        ) AS monthly_change
    FROM customer_transactions
    GROUP BY customer_id, DATE_TRUNC('month', txn_date)
),

closing_balance_cte AS (
    SELECT 
        customer_id,
        month_start,
        SUM(monthly_change) OVER (
            PARTITION BY customer_id
            ORDER BY month_start
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS closing_balance
    FROM monthly_net
),

growth_cte AS (
    SELECT 
        customer_id,
        closing_balance,
        LAG(closing_balance) OVER (
            PARTITION BY customer_id
            ORDER BY month_start
        ) AS prev_closing_balance
    FROM closing_balance_cte
)

SELECT 
    ROUND(
        COUNT(DISTINCT customer_id) * 100.0
        / (SELECT COUNT(DISTINCT customer_id) FROM customer_transactions),
        2
    ) AS percentage_customers
FROM growth_cte
WHERE 
    prev_closing_balance > 0
    AND (
        (closing_balance - prev_closing_balance)::numeric
        / prev_closing_balance
    ) > 0.05;

