-- Foodie-F-
-- Solution Query tool

CREATE SCHEMA IF NOT EXISTS foodie_fi;
SET search_path = foodie_fi;

---------------------- Table Schemas ----------------------
CREATE TABLE plans (
  plan_id INTEGER,
  plan_name VARCHAR(13),
  price DECIMAL(5,2)
);

CREATE TABLE subscriptions (
  customer_id INTEGER,
  plan_id INTEGER,
  start_date DATE
);


---------------------- SELECT ----------------------

SELECT * FROM plans;

SELECT * FROM subscriptions LIMIT 10;

-- SELECT count(*) FROM subscriptions;
-- contains total of 2650 rows



---------------------- A. Customer Journey ----------------------

-- Based off the 8 sample customers provided in the sample from the subscriptions table, 
-- write a brief description about each customer’s onboarding journey.

-- Try to keep it as short as possible -
-- you may also want to run some sort of join to make your explanations a bit easier!

SELECT count(DISTINCT customer_id) FROM subscriptions; 
-- There are total of 1000 customers

SELECT * 
FROM subscriptions
WHERE customer_id <= 8 AND plan_id=0
ORDER BY customer_id;
-- All customers starts with trial plan

SELECT * 
FROM subscriptions
WHERE customer_id <= 8
ORDER BY customer_id;


-- customer 1: Started a trial on 1 Aug 2020, converted to the Basic Monthly plan after 7 days, and remains an active subscriber.
-- customer 2: Started a trial on 20 Sep 2020, upgraded directly to the Pro Annual plan after the trial, and remains active.
-- customer 3: Began with a trial on 13 Jan 2020, converted to the Basic Monthly plan, and continues the subscription.
-- customer 4: Started with a trial on 17 Jan 2020, moved to the Basic Monthly plan, and later churned in April 2020.
-- customer 5: Started with a trial on 3 Aug 2020, converted to Basic Monthly, and remains active.
-- customer 6: Began with a trial on 23 Dec 2020, moved to Basic Monthly, and churned in February 2021.
-- customer 7: Started with a trial on 5 Feb 2020, converted to Basic Monthly, and later upgraded to Pro Monthly in May 2020.
-- customer 8: Started with a trial on 11 Jun 2020, converted to Basic Monthly, and upgraded to Pro Monthly in August 2020.


---------------------- B. Data Analysis Questions ----------------------
-- 1. How many customers has Foodie-Fi ever had?
SELECT COUNT(DISTINCT customer_id) customers_ever_had_Foodie_Fi FROM subscriptions;


-- 2. What is the monthly distribution of trial plan start_date values for our dataset -
-- use the start of the month as the group by value
SELECT 
	DATE_TRUNC('month', start_date)::date AS month_start,
	COUNT(*) as distribution
FROM subscriptions
WHERE plan_id=0
GROUP BY month_start
ORDER BY month_start;


-- 3. What plan start_date values occur after the year 2020 for our dataset?
-- Show the breakdown by count of events for each plan_name
SELECT p.plan_name, COUNT(*) count_of_events
FROM plans p
JOIN subscriptions s USING(plan_id)
WHERE s.start_date > DATE '2020-12-31'
GROUP BY p.plan_name
ORDER BY p.plan_name;


-- 4. What is the customer count 
-- and percentage of customers who have churned rounded to 1 decimal place?
SELECT 
	COUNT(distinct customer_id) 
		FILTER (WHERE plan_id=4) customer_count,
	ROUND((COUNT(distinct customer_id) 
		FILTER (WHERE plan_id=4) 
		/ (COUNT(distinct customer_id)*1.0)) * 100,1) percentage
FROM subscriptions s;

-- 5. How many customers have churned straight after their initial free trial -
-- what percentage is this rounded to the nearest whole number?
WITH trial_next AS (
    SELECT 
        customer_id,
		plan_id,
        LEAD(plan_id) OVER (
            PARTITION BY customer_id
            ORDER BY start_date
        ) AS next_plan
    FROM subscriptions
)
SELECT 
    COUNT(*) AS churn_after_trial,
    ROUND(COUNT(*) * 100.0 
          / (SELECT COUNT(DISTINCT customer_id) FROM subscriptions)
    ,0) AS percentage
FROM trial_next
WHERE next_plan = 4 and plan_id = 0

-- 6. What is the number and percentage of customer plans after their initial free trial?
WITH cte AS (
	SELECT customer_id, plan_id, 
		LEAD(plan_id) OVER (
			PARTITION BY customer_id 
			ORDER BY start_date
		) next_plan_id
	FROM subscriptions
)
SELECT next_plan_id as plan_id, 
	COUNT(*) cnt,
	ROUND(
		COUNT(*) * 100.0
		/ (SELECT COUNT(distinct customer_id) tot FROM subscriptions)
	,2) as percentage
FROM cte
WHERE plan_id=0
GROUP BY next_plan_id
ORDER BY next_plan_id;

-- 7. What is the customer count and percentage breakdown of all 5 plan_name values at 2020-12-31?
WITH cte AS (
	SELECT 
		customer_id,
		plan_id,
		ROW_NUMBER() OVER (
			PARTITION BY customer_id
			ORDER BY start_date DESC
		) rn
	FROM subscriptions
	WHERE start_date <= DATE '2020-12-31'
)
SELECT 
	plan_name,
	COUNT(*) cnt,
	ROUND(
		COUNT(*) * 100.0
		/ (SELECT COUNT(distinct customer_id) FROM cte)
	,2) percentage
FROM cte
JOIN plans USING (plan_id)
WHERE rn=1
GROUP BY plan_name;


-- 8. How many customers have upgraded to an annual plan in 2020?
-- we already know that each customer will initially given free trail plan (plan_id=0)
-- in the question, there is no specification of transition from any plan to annual plan
-- so taking generic upgrade
SELECT 
	COUNT(distinct customer_id) customers_upgraded
FROM subscriptions
WHERE EXTRACT(YEAR FROM start_date) = 2020 and plan_id=3;

-- 9. How many days on average does it take for a customer to an annual plan from the day they join Foodie-Fi?
-- assumption: we are ignoring the persons who never taken annual plan
-- assumption: the customer is only upgrading to annual plan in his/her lifetime
-- meaning that there does not exist a seq: trial -> basic -> annual -> monthly -> annual
WITH trials AS (
	SELECT customer_id, start_date as trial_date
	FROM subscriptions
	WHERE plan_id=0
),
annuals AS (
	SELECT customer_id, start_date as annual_date
	FROM subscriptions
	WHERE plan_id=3
)
SELECT 
	ROUND( AVG(annual_date - trial_date) ) as avg_days_to_upgrade_to_annual 
FROM trials 
JOIN annuals USING (customer_id)

-- 10. Can you further breakdown this average value into 30 day periods (i.e. 0-30 days, 31-60 days etc)
WITH trials AS (
	SELECT customer_id, start_date as trial_date
	FROM subscriptions
	WHERE plan_id=0
),
annuals AS (
	SELECT customer_id, start_date as annual_date
	FROM subscriptions
	WHERE plan_id=3
), avg_30_days_interval AS (
	SELECT 
		((annual_date - trial_date)-1)/30 as pivot,
		ROUND(
			AVG(annual_date - trial_date)
		) as avg_days_to_upgrade_to_annual
	FROM trials 
	JOIN annuals USING (customer_id)
	GROUP BY ((annual_date - trial_date)-1)/30
)
SELECT 
	CONCAT(
		30*pivot + 1,
		'-',
		30*(pivot+1),
		' days'
	) as interval,
	avg_days_to_upgrade_to_annual
FROM avg_30_days_interval
ORDER BY pivot;

-- 11. How many customers downgraded from a pro monthly to a basic monthly plan in 2020?
-- assumption: we are counting customers with seq: trial -> pro monthly -> annual -> basic as well
-- we will only focus on downgrad year, which should be 2020
-- even if pro montly plan has started before year 2020
WITH pro AS (
	SELECT customer_id, start_date
	FROM subscriptions
	WHERE plan_id=2
),
basic as (
	SELECT customer_id, start_date 
	FROM subscriptions
	WHERE start_date >= '2020-01-01' AND start_date < '2021-01-01' AND plan_id=1
)
SELECT basic.customer_id
FROM basic
JOIN pro 
ON pro.customer_id=basic.customer_id AND pro.start_date<basic.start_date;

WITH cte as (
	SELECT
		customer_id, plan_id,
		LEAD(plan_id) OVER (
			PARTITION BY customer_id
			ORDER BY start_date
		) lead_plan,
		start_date
	FROM subscriptions
) 
SELECT COUNT(*) cnt
FROM cte
WHERE start_date < '2021-01-01' AND start_date >= '2020-01-01' AND plan_id=2 AND lead_plan=1;





--------------------------- Section C ---------------------------

-- we need to create a table payments

-- payments schema: (customer_id	plan_id	plan_name	payment_date	amount	payment_order)

SELECT * FROM plans;

SELECT * FROM subscriptions WHERE customer_id<20;

WITH cte AS (
	SELECT customer_id, 
			s.plan_id, 
			LAG(s.plan_id) OVER(
				PARTITION BY customer_id
				ORDER BY start_date
			) prev_plan_id,
			plan_name, 
			start_date as curr_date,
			LEAD(start_date) OVER(
				PARTITION BY customer_id
				ORDER BY start_date
			) next_start_date,
			price,
			LAG(price) OVER(
				PARTITION BY customer_id
				ORDER BY start_date
			) prev_price
	FROM plans p
	JOIN subscriptions s USING(plan_id)
	WHERE customer_id<=19 AND plan_id!=0 AND plan_id!=4
),
cte2 AS (
	SELECT customer_id,
			plan_id,
			plan_name,
			curr_date,
			next_start_date,
			(CASE
				WHEN prev_plan_id=1
				THEN price-prev_price
				ELSE price
			END) amount
	FROM cte
),
cte3 AS (
	SELECT customer_id,
			plan_id,
			plan_name,
			GENERATE_SERIES(
				curr_date,
				curr_date- interval '1 DAY' ,
				CASE 
					WHEN next_start_date IS NULL
					THEN DATE '2020-12-31'
					WHEN plan_id=1
					THEN next_start_date
					WHEN plan_id=2 and curr_date 
					THEN next_start_date
				END,
				'1 month'::interval
			)::date payment_date,
			amount
	FROM cte2
)
SELECT *,ROW_NUMBER() OVER(
				PARTITION BY customer_id
				ORDER BY payment_date
			) payment_order
FROM cte3
ORDER BY customer_id;


SELECT * FROM subscriptions
WHERE customer_id=19;

