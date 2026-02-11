----------------- Case Study #2 -----------------

----------------- SETUP -----------------

CREATE SCHEMA pizza_runner;
SET search_path = pizza_runner;

DROP TABLE IF EXISTS runners;
CREATE TABLE runners (
  "runner_id" INTEGER,
  "registration_date" DATE
);
INSERT INTO runners
  ("runner_id", "registration_date")
VALUES
  (1, '2021-01-01'),
  (2, '2021-01-03'),
  (3, '2021-01-08'),
  (4, '2021-01-15');


DROP TABLE IF EXISTS customer_orders;
CREATE TABLE customer_orders (
  "order_id" INTEGER,
  "customer_id" INTEGER,
  "pizza_id" INTEGER,
  "exclusions" VARCHAR(4),
  "extras" VARCHAR(4),
  "order_time" TIMESTAMP
);

INSERT INTO customer_orders
  ("order_id", "customer_id", "pizza_id", "exclusions", "extras", "order_time")
VALUES
  ('1', '101', '1', '', '', '2020-01-01 18:05:02'),
  ('2', '101', '1', '', '', '2020-01-01 19:00:52'),
  ('3', '102', '1', '', '', '2020-01-02 23:51:23'),
  ('3', '102', '2', '', NULL, '2020-01-02 23:51:23'),
  ('4', '103', '1', '4', '', '2020-01-04 13:23:46'),
  ('4', '103', '1', '4', '', '2020-01-04 13:23:46'),
  ('4', '103', '2', '4', '', '2020-01-04 13:23:46'),
  ('5', '104', '1', 'null', '1', '2020-01-08 21:00:29'),
  ('6', '101', '2', 'null', 'null', '2020-01-08 21:03:13'),
  ('7', '105', '2', 'null', '1', '2020-01-08 21:20:29'),
  ('8', '102', '1', 'null', 'null', '2020-01-09 23:54:33'),
  ('9', '103', '1', '4', '1, 5', '2020-01-10 11:22:59'),
  ('10', '104', '1', 'null', 'null', '2020-01-11 18:34:49'),
  ('10', '104', '1', '2, 6', '1, 4', '2020-01-11 18:34:49');


DROP TABLE IF EXISTS runner_orders;
CREATE TABLE runner_orders (
  "order_id" INTEGER,
  "runner_id" INTEGER,
  "pickup_time" VARCHAR(19),
  "distance" VARCHAR(7),
  "duration" VARCHAR(10),
  "cancellation" VARCHAR(23)
);

INSERT INTO runner_orders
  ("order_id", "runner_id", "pickup_time", "distance", "duration", "cancellation")
VALUES
  ('1', '1', '2020-01-01 18:15:34', '20km', '32 minutes', ''),
  ('2', '1', '2020-01-01 19:10:54', '20km', '27 minutes', ''),
  ('3', '1', '2020-01-03 00:12:37', '13.4km', '20 mins', NULL),
  ('4', '2', '2020-01-04 13:53:03', '23.4', '40', NULL),
  ('5', '3', '2020-01-08 21:10:57', '10', '15', NULL),
  ('6', '3', 'null', 'null', 'null', 'Restaurant Cancellation'),
  ('7', '2', '2020-01-08 21:30:45', '25km', '25mins', 'null'),
  ('8', '2', '2020-01-10 00:15:02', '23.4 km', '15 minute', 'null'),
  ('9', '2', 'null', 'null', 'null', 'Customer Cancellation'),
  ('10', '1', '2020-01-11 18:50:20', '10km', '10minutes', 'null');


DROP TABLE IF EXISTS pizza_names;
CREATE TABLE pizza_names (
  "pizza_id" INTEGER,
  "pizza_name" TEXT
);
INSERT INTO pizza_names
  ("pizza_id", "pizza_name")
VALUES
  (1, 'Meatlovers'),
  (2, 'Vegetarian');


DROP TABLE IF EXISTS pizza_recipes;
CREATE TABLE pizza_recipes (
  "pizza_id" INTEGER,
  "toppings" TEXT
);
INSERT INTO pizza_recipes
  ("pizza_id", "toppings")
VALUES
  (1, '1, 2, 3, 4, 5, 6, 8, 10'),
  (2, '4, 6, 7, 9, 11, 12');


DROP TABLE IF EXISTS pizza_toppings;
CREATE TABLE pizza_toppings (
  "topping_id" INTEGER,
  "topping_name" TEXT
);
INSERT INTO pizza_toppings
  ("topping_id", "topping_name")
VALUES
  (1, 'Bacon'),
  (2, 'BBQ Sauce'),
  (3, 'Beef'),
  (4, 'Cheese'),
  (5, 'Chicken'),
  (6, 'Mushrooms'),
  (7, 'Onions'),
  (8, 'Pepperoni'),
  (9, 'Peppers'),
  (10, 'Salami'),
  (11, 'Tomatoes'),
  (12, 'Tomato Sauce');


----------------- SELECT -----------------
SELECT * FROM runners;

SELECT * FROM customer_orders;

SELECT * FROM runner_orders;

SELECT * FROM pizza_names;

SELECT * FROM pizza_recipes;

SELECT * FROM pizza_toppings;

----------------- Handling Corrupted data -----------------

-- cleaning up fake null values in exclusions from customer_orders table 
UPDATE customer_orders
SET exclusions=NULL
WHERE exclusions IN ('','null');

SELECT order_id, exclusions FROM customer_orders ORDER BY order_id;

-- cleaning up fake null values in extras from customer_orders table 
UPDATE customer_orders
SET extras=NULL
WHERE extras IN ('','null');

SELECT order_id, extras FROM customer_orders ORDER BY order_id;


-- in customer_orders table
-- removing extra spaces from extras and exclusion columns
UPDATE pizza_runner.customer_orders
SET exclusions = REPLACE(exclusions, ' ', '')
WHERE exclusions IS NOT NULL;

UPDATE pizza_runner.customer_orders
SET extras = REPLACE(extras, ' ', '')
WHERE extras IS NOT NULL;

SELECT extras FROM customer_orders;

-- Altering pickup_time column in runner_orders table
-- old type: varchar
-- new type: TIMESTAMP
ALTER TABLE runner_orders
ALTER COLUMN pickup_time TYPE TIMESTAMP
USING NULLIF(pickup_time, 'null')::TIMESTAMP;

-- SELECT pickup_time FROM runner_orders;

-- distance values are inconsitent in runner_orders
-- old type: varchar 
-- new type: NUMERIC
ALTER TABLE runner_orders
ALTER COLUMN distance TYPE NUMERIC  
USING NULLIF(REGEXP_REPLACE(distance,'[^0-9.]','','g') ,'')::NUMERIC;
-- now the distance column contains distance in kms


-- SELECT distance FROM runner_orders;

-- duration values are incosistent in runner_orders
-- old type: varchar 
-- new type: NUMERIC
ALTER TABLE runner_orders
ALTER COLUMN duration TYPE INTEGER
USING NULLIF(REGEXP_REPLACE(duration,'[^0-9]','','g'),'')::INTEGER;
-- now the duration column contains duration in minutes


-- SELECT duration FROM runner_orders;

-- cancelation columns have multiple types of null values
-- like, 'null', '', NULL
-- Unify all the nulls
UPDATE pizza_runner.runner_orders
SET cancellation = NULL
WHERE cancellation IN ('', 'null');

SELECT order_id,cancellation FROM runner_orders

-- in customer_orders, 1 row= 1 pizza
-- in runner_orders, 1 row = 1 order

-- giving proper name to pizza
-- this query hasn't performed
-- UPDATE pizza_runner.pizza_names
-- SET pizza_name = 'Meatlovers'
-- WHERE pizza_name = 'Meat Lovers';

SELECT * FROM pizza_names ORDER BY pizza_id;


-- Mixed timeline issues
SELECT r.order_id, (r.pickup_time > c.order_time) foo
FROM customer_orders c
JOIN runner_orders r ON c.order_id=r.order_id;

-- the above query validates that all pickup times are > than order time

-- as per the questions asked in challege
-- we don't need to apply normalization
-- as the columns extras and exclusion in customer_orders table
-- are independent of each other



----------------- SELECT -----------------
SELECT * FROM runners;

SELECT * FROM customer_orders;

SELECT * FROM runner_orders;

SELECT * FROM pizza_names;

SELECT * FROM pizza_recipes;

SELECT * FROM pizza_toppings;




----------------- Case Study Questions -----------------

----------------- A. Pizza Metrics -----------------
-- NOTE: customer_orders is for orders made by customer
-- and runner_orders is for orders delivery

-- One common assumption is that if an order is cancelled
-- its pickup_time will be null
-- otherwise it definitely contains valid value

-- 1. How many pizzas were ordered?
-- customer_orders tells in which order which pizza was added
-- so total records = total pizza ordered
SELECT COUNT(*) as pizzas_ordered
FROM customer_orders;

-- 2. How many unique customer orders were made?
SELECT COUNT(DISTINCT order_id)
FROM customer_orders;


-- 3. How many successful orders were delivered by each runner?
SELECT runner_id, COUNT(distinct order_id) successful_orders
FROM runner_orders
WHERE cancellation IS NULL AND pickup_time IS NOT NULL
GROUP BY runner_id;

-- 4. How many of each type of pizza was delivered?
SELECT c.pizza_id, COUNT(*) 
FROM customer_orders c
JOIN runner_orders r ON c.order_id = r.order_id
WHERE r.cancellation IS NULL
GROUP BY c.pizza_id;
-- remaining: join pizza table to display 0 ordered pizzas

-- 5. How many Vegetarian and Meatlovers were ordered by each customer?
SELECT customer_id, p.pizza_name , COUNT(*)
FROM customer_orders c 
JOIN pizza_names p USING(pizza_id)
WHERE p.pizza_name IN ('Vegetarian', 'Meatlovers')
GROUP BY c.customer_id, p.pizza_name;



-- 6. What was the maximum number of pizzas delivered in a single order?
WITH cte AS (
	SELECT r.order_id, COUNT(*) no_of_pizzas
	FROM customer_orders c
	JOIN runner_orders r USING(order_id)
	WHERE r.cancellation IS NULL AND r.pickup_time IS NOT NULL
	GROUP BY r.order_id
)
SELECT MAX(no_of_pizzas) max_no_of_pizzas_delivered
FROM cte;
--  or we can use 
-- ORDER BY no_of_pizzas DESC LIMIT 1 

-- 7. For each customer, how many delivered pizzas had at least 1 change 
-- and how many had no changes?

-- here we are interpreting change as 
-- addition of some ingredient or removal of some ingredient
-- so if extras or exclusions are not null then its a change
SELECT c.customer_id, 
	SUM((c.exclusions IS NOT NULL OR c.extras IS NOT NULL)::int) change_needed,
	SUM((c.exclusions IS NULL AND c.extras IS NULL)::int) no_change
FROM customer_orders c
JOIN runner_orders r USING (order_id)
WHERE r.cancellation IS NULL
GROUP BY c.customer_id
ORDER BY c.customer_id;


-- 8. How many pizzas were delivered that had both exclusions and extras?

SELECT 
	COUNT(*) exc_and_extras
FROM customer_orders c
JOIN runner_orders r USING (order_id)
WHERE r.cancellation IS NULL 
	AND c.exclusions IS NOT NULL AND c.extras IS NOT NULL
;
-- we can use the same thing we used in 7th query


-- 9. What was the total volume of pizzas ordered for each hour of the day?

-- here there is no mention of delivery so ignoring runner_orders table
-- showing hours in which pizzas were ordered
-- ignoring hours in which there were no orders
-- also grouping is done based on hours
-- and not on the basis of date + hours
SELECT EXTRACT(HOUR FROM order_time) hour_of_day, 
		COUNT(*) pizzas_ordered_per_hour
FROM customer_orders
GROUP BY hour_of_day
ORDER BY hour_of_day;


-- 10. What was the volume of orders for each day of the week?
-- here also we are not showing the day of week
-- in which not a single pizza ordered
-- here also the grouping is done on the basis of day of week and 
-- not on specific day (date)

SELECT TRIM(TO_CHAR(order_time, 'Day')) day_of_week, 
		COUNT(DISTINCT order_id) orders_of_day
FROM customer_orders
GROUP BY day_of_week
ORDER BY day_of_week;


----------------- B. Runner and Customer Experience -----------------

-- 1. How many runners signed up for each 1 week period? 
-- (i.e. week starts 2021-01-01)
-- here 2021-01-01 to 2021-01-07 is 1st week
SELECT (registration_date- DATE '2021-01-01')/7 + 1 week, COUNT(*) runners_signed_up
FROM runners
GROUP BY week
ORDER BY week
;
-- temp = cur_date - 2021-01-01 % 7 

-- 2. What was the average time in minutes 
-- it took for each runner to arrive at the Pizza Runner HQ to pickup the order?
SELECT r.runner_id, ROUND(EXTRACT(EPOCH FROM AVG(r.pickup_time - c.order_time)) / 60,2) avg_minutes
FROM runner_orders r
JOIN (
	SELECT DISTINCT order_id, order_time FROM customer_orders
) c USING(order_id)
WHERE r.cancellation IS NULL AND r.pickup_time IS NOT NULL
GROUP BY r.runner_id
ORDER BY r.runner_id;

-- 3. Is there any relationship between the number of pizzas
-- and how long the order takes to prepare?
-- assumption: we are assuming that if one order is placed then immidiately pizza HQ will start preparing pizzas
-- and also we are assuming that if all pizzas are prepared then immidiately runner will pick them
-- so start time = order_time and end time = pickup time

WITH cnt_time_rel AS (
SELECT order_id, 
		COUNT(*) pizza_cnt,
		ROUND(EXTRACT(EPOCH FROM (r.pickup_time - c.order_time)) / 60,2) prep_time
FROM customer_orders c
JOIN runner_orders r USING (order_id)
WHERE r.pickup_time IS NOT NULL
GROUP BY order_id, r.pickup_time, c.order_time
ORDER BY pizza_cnt
) 
SELECT pizza_cnt,ROUND(AVG(prep_time),2)
FROM cnt_time_rel
GROUP BY pizza_cnt
ORDER BY pizza_cnt;

-- we have first compute the total time and number of pizzas per order
-- we haven't found linear relationship between pizza count and preparation time
-- then we tried average
-- it seem like   less the no. of pizzas, less the average preparation time
-- 			and   more the no. of pizzas, more the average preparation time


-- 4. What was the average distance travelled for each customer?
WITH cte AS (
	SELECT DISTINCT customer_id, order_id FROM customer_orders
)
SELECT customer_id, ROUND(AVG(r.distance),2)
FROM cte c
JOIN runner_orders r USING(order_id)
WHERE r.cancellation IS NULL AND r.pickup_time IS NOT NULL
GROUP BY customer_id
ORDER BY customer_id;

-- 5. What was the difference between the longest and shortest delivery times for all orders?
-- here delivery time refers to duration

-- assumption: delivery time is with respect to runner,
-- meaning that we need to take the duration
-- if it was respect to customer,
-- we had to take duration + (preparation time = pickup_time - order_time)
SELECT 
    MAX(duration) - MIN(duration) AS difference_in_delivery_time
FROM runner_orders
WHERE pickup_time IS NOT NULL;


-- 6. What was the average speed for each runner for each delivery 
-- 	  and do you notice any trend for these values?
-- for each runner for each delivery
SELECT runner_id, 
	order_id,
	ROUND((distance/(duration/60.0)),2) speed_km_per_hour
FROM runner_orders
WHERE duration IS NOT NULL AND distance IS NOT NULL
ORDER BY runner_id, order_id;

-- for each runner (grouped data)
SELECT runner_id, 
	ROUND(AVG(distance/(duration/60.0)),2) speed_km_per_hour
FROM runner_orders
WHERE duration IS NOT NULL AND distance IS NOT NULL
GROUP BY runner_id
ORDER BY runner_id;

-- one thing we can notice 
-- is that as the runners have taken more orders, more they increases their speed

-- 7. What is the successful delivery percentage for each runner?
SELECT runner_id, 
	ROUND(
		(SUM(
			(cancellation IS NULL AND pickup_time IS NOT NULL)::integer
		)/COUNT(*)::numeric) * 100.0
	,2) percentage
FROM runner_orders
GROUP BY runner_id
ORDER BY runner_id;


----------------- C. Ingredient Optimisation -----------------


-- 1. What are the standard ingredients for each pizza?
WITH cte AS (
	SELECT pizza_id, 
		unnest(string_to_array(toppings,', '))::integer topping_id
	FROM pizza_recipes
)
SELECT pn.pizza_name, ARRAY_AGG(topping_name) 
FROM cte pr
JOIN pizza_toppings pt USING (topping_id)
JOIN pizza_names pn USING (pizza_id)
GROUP BY pn.pizza_name;


-- 2. What was the most commonly added extra?
WITH cte AS (
	SELECT unnest(string_to_array(extras,','))::numeric extra
	FROM customer_orders
	WHERE extras IS NOT NULL
),
freq AS (
	SELECT extra, COUNT(*) cnt
	FROM cte 
	GROUP BY extra
)
SELECT extra, cnt
FROM freq
WHERE cnt = (select max(cnt) from freq)

-- 3. What was the most common exclusion?
WITH cte AS (
	SELECT unnest(string_to_array(exclusions,','))::numeric exclusion
	FROM customer_orders
	WHERE exclusions IS NOT NULL
),
freq AS (
	SELECT exclusion, COUNT(*) cnt
	FROM cte 
	GROUP BY exclusion
)
SELECT exclusion, cnt
FROM freq
WHERE cnt = (select max(cnt) from freq)


-- 4. Generate an order item for each record in the customers_orders table in the format of one of the following:
	-- Meat Lovers
	-- Meat Lovers - Exclude Beef (3)
	-- Meat Lovers - Extra Bacon (1)
	-- Meat Lovers - Exclude Cheese(4) , Bacon(1) - Extra Mushroom(6), Peppers (9)

-- SELECT order_id, customer_id, c.pizza_id, c.order_time, 
-- 	CONCAT(
-- 		pizza_name,
-- 		CASE WHEN exclusions IS NOT NULL THEN CONCAT(' - Exclude ',string_to_array(exclusions,','),' ')
-- 		ELSE ''
-- 		END,
-- 		CASE WHEN extras IS NOT NULL THEN CONCAT(' - Extra ',string_to_array(extras,','),' ')
-- 		ELSE ''
-- 		END
-- 	) order_item
-- FROM customer_orders c
-- JOIN pizza_names pn USING(pizza_id)


WITH cte AS (
	SELECT 
	ROW_NUMBER() OVER (ORDER BY customer_id) row_id,
	order_id, customer_id, pizza_id,order_time, exclusions, extras
	FROM customer_orders
),
cteExclusion AS (
	SELECT 
	ROW_NUMBER() OVER (ORDER BY customer_id) row_id,
	unnest(string_to_array(exclusions,',')) exclusion_id
	FROM customer_orders
),
cteExtra AS (
	SELECT 
	ROW_NUMBER() OVER (ORDER BY customer_id) row_id,
	unnest(string_to_array(extras,',')) extra_id
	FROM customer_orders
),
cteExcString AS (
	SELECT row_id, ARRAY_TO_STRING(ARRAY_AGG(pt.topping_name),', ') exclusions
	FROM cteExclusion c
	JOIN pizza_toppings pt
	ON c.exclusion_id::integer = pt.topping_id
	GROUP BY row_id
),
cteExtString AS (
	SELECT row_id, ARRAY_TO_STRING(ARRAY_AGG(pt.topping_name),', ') extras
	FROM cteExtra c
	JOIN pizza_toppings pt
	ON c.extra_id::integer = pt.topping_id
	GROUP BY row_id
),
f_final AS (
	SELECT 
		order_id, customer_id, pizza_id, 
		CONCAT(
			pizza_name,
			CASE 
				WHEN c.exclusions IS NOT NULL 
				THEN CONCAT(' - Exclude ',exc.exclusions)
				ELSE ''
			END,
			CASE 
				WHEN c.extras IS NOT NULL 
				THEN CONCAT(' - Extra ',ext.extras)
				ELSE ''
			END
		) order_item
	FROM cte c
	LEFT JOIN cteExtString ext USING(row_id)
	LEFT JOIN cteExcString exc USING(row_id)
	JOIN pizza_names pn USING(pizza_id)
)
SELECT * FROM f_final
ORDER BY customer_id, order_id;

-- Generate an alphabetically ordered comma separated ingredient list for each pizza order from the customer_orders table and add a 2x in front of any relevant ingredients
-- For example: "Meat Lovers: 2xBacon, Beef, ... , Salami"
-- What is the total quantity of each ingredient used in all delivered pizzas sorted by most frequent first?



----------------- D. Pricing and Ratings -----------------
-- If a Meat Lovers pizza costs $12 and Vegetarian costs $10 and there were no charges for changes - how much money has Pizza Runner made so far if there are no delivery fees?
-- What if there was an additional $1 charge for any pizza extras?
-- Add cheese is $1 extra
-- The Pizza Runner team now wants to add an additional ratings system that allows customers to rate their runner, how would you design an additional table for this new dataset - generate a schema for this new table and insert your own data for ratings for each successful customer order between 1 to 5.
-- Using your newly generated table - can you join all of the information together to form a table which has the following information for successful deliveries?
-- customer_id
-- order_id
-- runner_id
-- rating 
-- order_time
-- pickup_time
-- Time between order and pickup
-- Delivery duration
-- Average speed
-- Total number of pizzas
-- If a Meat Lovers pizza was $12 and Vegetarian $10 fixed prices with no cost for extras and each runner is paid $0.30 per kilometre traveled - how much money does Pizza Runner have left over after these deliveries?



