------------------------ Case Study #5 ------------------------

DROP TABLE IF EXISTS data_mart.weekly_sales;
CREATE TABLE dbo.weekly_sales (
  "week_date" VARCHAR(7),
  "region" VARCHAR(13),
  "platform" VARCHAR(7),
  "segment" VARCHAR(4),
  "customer_type" VARCHAR(8),
  "transactions" INTEGER,
  "sales" INTEGER
);

-- Loading data into database
--BULK INSERT dbo.weekly_sales
--FROM 'C:\Users\aman.rajput\Downloads\data_mart.csv'
--WITH (
--    FIRSTROW = 2,
--    FIELDTERMINATOR = ',',
--    ROWTERMINATOR = '0x0A',   -- handles \n correctly, works for most CSVs
--    KEEPNULLS,
--    FORMAT = 'CSV'
--);
-- CREATE SCHEMA data_mart;

SELECT name FROM sys.schemas;

ALTER SCHEMA data_mart TRANSFER dbo.weekly_sales;


SELECT COUNT(*) FROM weekly_sales; -- 17116 rows

SELECT * FROM data_mart.weekly_sales
ORDER BY week_date
OFFSET 0 ROWS FETCH FIRST 5 ROWS ONLY;

SELECT MIN(week_date) min_date, MAX(week_date) max_date
FROM data_mart.weekly_sales;
-- getting strange response

SELECT distinct segment FROM data_mart.weekly_sales;

SELECT distinct region FROM data_mart.weekly_sales;

SELECT distinct customer_type FROM data_mart.weekly_sales;

EXEC sp_help 'data_mart.weekly_sales';

SELECT * FROM data_mart.weekly_sales where segment = 'null';


------------------------ 1. Data Cleansing Steps ------------------------

--BEGIN TRANSACTION;


create table data_mart.clean_weekly_sales(
					"region" varchar(13),
					"platform" varchar(7),
					"segment" varchar(4),
					"customer_type" varchar(8),
					"transactions" int,
					"sales" int,
					week_date date,
					week_number int,
					month_number int,
					calendar_year int,
					age_band varchar(20),
					demographic varchar(20),
					avg_transaction double precision
				);
SELECT * FROM data_mart.clean_weekly_sales;

--truncate table data_mart.clean_weekly_sales;
--drop table if exists data_mart.clean_weekly_sales;

INSERT INTO data_mart.clean_weekly_sales
SELECT 
	region, platform, segment, customer_type, "transactions", sales,
	CONVERT(date,week_date,3) as week_date,
	DATEPART(week,CONVERT(date,week_date,3)) as week_number,
	DATEPART(month,CONVERT(date,week_date,3)) as month_number,
	DATEPART(year,CONVERT(date,week_date,3)) as calendar_year,
	(CASE 
		WHEN SUBSTRING(segment,2,1) = '1' THEN 'Young Adults'
		WHEN SUBSTRING(segment,2,1) = '2' THEN 'Middle Aged'
		WHEN SUBSTRING(segment,2,1) IN ('3','4') THEN 'Retirees'
		ELSE 'unknown'
	END) age_band,
	(CASE
		WHEN SUBSTRING(segment,1,1) = 'C' THEN 'Couples'
		WHEN SUBSTRING(segment,1,1) = 'F' THEN 'Families'
		ELSE 'unknown'
	END) demographic,
	ROUND((sales * 1.0) / NULLIF(transactions,0), 2) avg_transaction
FROM data_mart.weekly_sales;


--ROLLBACK TRANSACTION;
--COMMIT TRANSACTION;

------------------------ 2. Data Exploration ------------------------
--1. What day of the week is used for each week_date value?
SELECT distinct DATENAME(weekday, week_date)
FROM data_mart.clean_weekly_sales;

-- ans: Monday

--2. What range of week numbers are missing from the dataset?
-- assumption: we not considering year over hear
-- if we want years than we need to join all_weeks cte with all_years 
WITH all_weeks AS (
    SELECT 1 AS wk
    UNION ALL
    SELECT wk + 1
    FROM all_weeks
    WHERE wk < 53
)
SELECT 
	wk missing_weeks
FROM all_weeks x
WHERE NOT EXISTS (
	SELECT 1 FROM data_mart.clean_weekly_sales i
	WHERE x.wk = i.week_number
)


-- ans: it seems like weeks 1 to 12 are not there in any of year 2018, 2019 or 2020

--3. How many total transactions were there for each year in the dataset?
SELECT calendar_year, SUM(CAST(transactions AS bigint)) total_transactions
FROM data_mart.clean_weekly_sales
GROUP BY calendar_year;


--4. What is the total sales for each region for each month?
-- in the question we have only asked about region and month so we are grouping only these two
-- but in real life if we want to distinguish then we should also group with year
select region, month_number, sum(cast(sales as bigint)) total_sales
from data_mart.clean_weekly_sales 
group by region, month_number;

--5. What is the total count of transactions for each platform
select platform, sum(cast(transactions as bigint)) total_transactions
from data_mart.clean_weekly_sales
group by platform;

--6. What is the percentage of sales for Retail vs Shopify for each month?
SELECT
    month_number,
    ROUND(
        100.0 * SUM(CASE WHEN platform = 'Retail' THEN sales ELSE cast(0 as bigint) END)
        / SUM(cast(sales as bigint)), 2
    ) AS retail_percentage,

    ROUND(
        100.0 * SUM(CASE WHEN platform = 'Shopify' THEN sales ELSE cast(0 as bigint) END)
        / SUM(cast(sales as bigint)), 2
    ) AS shopify_percentage

FROM data_mart.clean_weekly_sales
GROUP BY month_number
ORDER BY month_number;


--7. What is the percentage of sales by demographic for each year in the dataset?
select 
	demographic, calendar_year, 
	sum(cast(sales as bigint)) * 100.0
	/ (select sum(cast(sales as bigint)) from data_mart.clean_weekly_sales i where i.calendar_year=o.calendar_year and demographic != 'unknown') as percentage
from data_mart.clean_weekly_sales o
where demographic != 'unknown'
group by demographic, calendar_year
order by calendar_year;

--8. Which age_band and demographic values contribute the most to Retail sales?
WITH cte AS (
	select
		age_band, demographic, sum(cast(sales as bigint)) sum_of_sales
	from data_mart.clean_weekly_sales
	where platform='Retail' and demographic != 'unknown'
	group by age_band, demographic
)
select * from cte
where sum_of_sales = (select max(sum_of_sales) from cte);

--9. Can we use the avg_transaction column to find the average transaction size for each year for Retail vs Shopify? If not - how would you calculate it instead?
select calendar_year, 
	sum(case when platform='Retail' then cast(sales as bigint) else 0 end)*1.0
	/ nullif(sum(case when platform='Retail' then cast(transactions as bigint) else 0 end),0)
	as retail_avg_transaction_size,
	sum(case when platform='Shopify' then cast(sales as bigint) else 0 end)*1.0
	/ nullif(sum(case when platform='Shopify' then cast(transactions as bigint) else 0 end),0)
	as shopify_avg_transaction_size
from data_mart.clean_weekly_sales
group by calendar_year
order by calendar_year;

------------------------ 3. Before & After Analysis ------------------------
--This technique is usually used when we inspect an important event and want to inspect the impact before and after a certain point in time.

--Taking the week_date value of 2020-06-15 as the baseline week where the Data Mart sustainable packaging changes came into effect.

--We would include all week_date values for 2020-06-15 as the start of the period after the change and the previous week_date values would be before

--Using this analysis approach - answer the following questions:

-- What is the total sales for the 4 weeks before and after 2020-06-15? What is the growth or reduction rate in actual values and percentage of sales?
with cte as (
	select sum(case when week_date<'2020-06-15' and  week_date between dateadd(week,-4,'2020-06-15') and cast('2020-06-15' as date) then cast(sales as bigint) else cast(0 as bigint) end) as four_weeks_before,
			sum(case when week_date>'2020-06-15' and week_date between '2020-06-15' and dateadd(week,4,'2020-06-15')then cast(sales as bigint) else cast(0 as bigint) end) as four_weeks_after
	from data_mart.clean_weekly_sales
)
select four_weeks_after, four_weeks_before, 
		(four_weeks_after - four_weeks_before)*1.0
		/ nullif(four_weeks_before,0) growth_rate,
		(four_weeks_after - four_weeks_before)*100.0
		/ nullif(four_weeks_before,0) growth_percentage
from cte
-- it seems like there is a reduction of 0.46% in sales in 4 weeks in year 2020

-- What about the entire 12 weeks before and after?
with cte as (
	select sum(
				case 
					when week_date<'2020-06-15' and  week_date >= dateadd(week,-12,'2020-06-15') 
					then cast(sales as bigint) else cast(0 as bigint) 
				end
			) as twelve_weeks_before,
			sum(
				case 
					when week_date>'2020-06-15' and week_date <= dateadd(week,12,'2020-06-15')
					then cast(sales as bigint) else cast(0 as bigint) 
				end
			) as twelve_weeks_after
	from data_mart.clean_weekly_sales
)
select twelve_weeks_after, 
		twelve_weeks_before, 
		(twelve_weeks_after - twelve_weeks_before)*1.0
		/ nullif(twelve_weeks_before,0) growth_rate,
		(twelve_weeks_after - twelve_weeks_before)*100.0
		/ nullif(twelve_weeks_before,0) growth_percentage
from cte

-- there is a reduction of 10.18% in growth in the span of 12 weeks in year 2020

-- How do the sale metrics for these 2 periods before and after compare with the previous years in 2018 and 2019?
drop function before_after_analysis
create function before_after_analysis(@pivot_date date, @week_span int)
returns table
as 
return 
	with cte as (
		select sum(
					case 
						when week_date<@pivot_date and  week_date >= dateadd(week,-@week_span,@pivot_date) 
						then cast(sales as bigint) else cast(0 as bigint) 
					end
				) as twelve_weeks_before,
				sum(
					case 
						when week_date>@pivot_date and week_date <= dateadd(week,@week_span,@pivot_date)
						then cast(sales as bigint) else cast(0 as bigint) 
					end
				) as twelve_weeks_after
		from data_mart.clean_weekly_sales
	)
	select twelve_weeks_after, 
			twelve_weeks_before, 
			(twelve_weeks_after - twelve_weeks_before)*1.0
			/ nullif(twelve_weeks_before,0) growth_rate,
			(twelve_weeks_after - twelve_weeks_before)*100.0
			/ nullif(twelve_weeks_before,0) growth_percentage
	from cte
-- for the 12 weeks of span
select 2018 as year,* from before_after_analysis('2018-06-15',12)
union all
select 2019 as year,* from before_after_analysis('2019-06-15',12)
union all
select 2020 as year,* from before_after_analysis('2020-06-15',12);

-- for the 4 weeks of span
select 2018 as year,* from before_after_analysis('2018-06-15',4)
union all
select 2019 as year,* from before_after_analysis('2019-06-15',4)
union all
select 2020 as year,* from before_after_analysis('2020-06-15',4);



------------------------ 4. Bonus Question ------------------------
-- Which areas of the business have the highest negative impact in sales metrics performance in 2020 for the 12 week before and after period?

--region
with cte as (
	select region, sum(
				case 
					when week_date<'2020-06-15' and  week_date >= dateadd(week,-12,'2020-06-15') 
					then cast(sales as bigint) else cast(0 as bigint) 
				end
			) as twelve_weeks_before,
			sum(
				case 
					when week_date>'2020-06-15' and week_date <= dateadd(week,12,'2020-06-15')
					then cast(sales as bigint) else cast(0 as bigint) 
				end
			) as twelve_weeks_after
	from data_mart.clean_weekly_sales
	where calendar_year=2020 and region is not null
	group by region
)
select region,
		twelve_weeks_after, 
		twelve_weeks_before, 
		(twelve_weeks_after - twelve_weeks_before)*1.0
		/ nullif(twelve_weeks_before,0) growth_rate,
		(twelve_weeks_after - twelve_weeks_before)*100.0
		/ nullif(twelve_weeks_before,0) growth_percentage
from cte
order by growth_percentage
offset 0 rows fetch first 1 rows only;

-- highest negative impact on sales
--ASIA	1450392199	1637244466	-0.11412606417690588	-11.412606417690588


--platform
with cte as (
	select platform, sum(
				case 
					when week_date<'2020-06-15' and  week_date >= dateadd(week,-12,'2020-06-15') 
					then cast(sales as bigint) else cast(0 as bigint) 
				end
			) as twelve_weeks_before,
			sum(
				case 
					when week_date>'2020-06-15' and week_date <= dateadd(week,12,'2020-06-15')
					then cast(sales as bigint) else cast(0 as bigint) 
				end
			) as twelve_weeks_after
	from data_mart.clean_weekly_sales
	where calendar_year=2020 and platform is not null
	group by platform
)
select platform,
		twelve_weeks_after, 
		twelve_weeks_before, 
		(twelve_weeks_after - twelve_weeks_before)*1.0
		/ nullif(twelve_weeks_before,0) growth_rate,
		(twelve_weeks_after - twelve_weeks_before)*100.0
		/ nullif(twelve_weeks_before,0) growth_percentage
from cte
order by growth_percentage
offset 0 rows fetch first 1 rows only; 

-- highest negative impact on sales
-- Retail	6184374449	6906861113	-0.10460419750444169	-10.460419750444169

--age_band
with cte as (
	select age_band, sum(
				case 
					when week_date<'2020-06-15' and  week_date >= dateadd(week,-12,'2020-06-15') 
					then cast(sales as bigint) else cast(0 as bigint) 
				end
			) as twelve_weeks_before,
			sum(
				case 
					when week_date>'2020-06-15' and week_date <= dateadd(week,12,'2020-06-15')
					then cast(sales as bigint) else cast(0 as bigint) 
				end
			) as twelve_weeks_after
	from data_mart.clean_weekly_sales
	where calendar_year=2020 and age_band is not null and age_band <> 'unknown'
	group by age_band
)
select age_band,
		twelve_weeks_after, 
		twelve_weeks_before, 
		(twelve_weeks_after - twelve_weeks_before)*1.0
		/ nullif(twelve_weeks_before,0) growth_rate,
		(twelve_weeks_after - twelve_weeks_before)*100.0
		/ nullif(twelve_weeks_before,0) growth_percentage
from cte
order by growth_percentage
offset 0 rows fetch first 1 rows only; 

-- highest negative impact on sales
-- Middle Aged	1047640798	1164847640	-0.10061989051203297	-10.061989051203297


--demographic
with cte as (
	select demographic, sum(
				case 
					when week_date<'2020-06-15' and  week_date >= dateadd(week,-12,'2020-06-15') 
					then cast(sales as bigint) else cast(0 as bigint) 
				end
			) as twelve_weeks_before,
			sum(
				case 
					when week_date>'2020-06-15' and week_date <= dateadd(week,12,'2020-06-15')
					then cast(sales as bigint) else cast(0 as bigint) 
				end
			) as twelve_weeks_after
	from data_mart.clean_weekly_sales
	where calendar_year=2020 and demographic is not null and demographic <> 'unknown'
	group by demographic
)
select demographic,
		twelve_weeks_after, 
		twelve_weeks_before, 
		(twelve_weeks_after - twelve_weeks_before)*1.0
		/ nullif(twelve_weeks_before,0) growth_rate,
		(twelve_weeks_after - twelve_weeks_before)*100.0
		/ nullif(twelve_weeks_before,0) growth_percentage
from cte
order by growth_percentage
offset 0 rows fetch first 1 rows only; 

-- highest negative impact on sales
-- Families	2096951469	2328329040	-0.09937494530412247	-9.937494530412247

--customer_type
with cte as (
	select customer_type, sum(
				case 
					when week_date<'2020-06-15' and  week_date >= dateadd(week,-12,'2020-06-15') 
					then cast(sales as bigint) else cast(0 as bigint) 
				end
			) as twelve_weeks_before,
			sum(
				case 
					when week_date>'2020-06-15' and week_date <= dateadd(week,12,'2020-06-15')
					then cast(sales as bigint) else cast(0 as bigint) 
				end
			) as twelve_weeks_after
	from data_mart.clean_weekly_sales
	where calendar_year=2020 and customer_type is not null
	group by customer_type
)
select customer_type,
		twelve_weeks_after, 
		twelve_weeks_before, 
		(twelve_weeks_after - twelve_weeks_before)*1.0
		/ nullif(twelve_weeks_before,0) growth_rate,
		(twelve_weeks_after - twelve_weeks_before)*100.0
		/ nullif(twelve_weeks_before,0) growth_percentage
from cte
order by growth_percentage
offset 0 rows fetch first 1 rows only; 

-- highest negative impact on sales
-- Guest	2292350880	2573436301	-0.10922571539492711	-10.922571539492711

--Do you have any further recommendations for Danny’s team at Data Mart or any interesting insights based off this analysis?












---------------------------------- ROUGH work ----------------------------------


--select sysdatetime();

--SELECT DATEADD(week, 1, '2024-08-31');

--SELECT DATETRUNC(month, '2021-08-23');

--SELECT CURRENT_TIMESTAMP; 

--SELECT YEAR('2021-12-09');

--SELECT datepart(week,'2021-12-17');

--SELECT CHARINDEX('@', 'sumit@gmail.com');

--SELECT value
--FROM STRING_SPLIT('A,B,C,D', ',');

--select format(cast('2021-01-01' as date), 'yy/MM');

--select datename(WEEKDAY, '2021-01-01')   -- returns the day like sunday, monday etc.

