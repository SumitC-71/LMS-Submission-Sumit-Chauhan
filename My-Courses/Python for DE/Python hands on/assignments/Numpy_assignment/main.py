from logger_config import setup_logger, task_logger
import pandas as pd
import os
from datetime import datetime
import time

logger = setup_logger()

def task1_data_loading(filename):
    # filename = 'employees.csv'
    if not os.path.exists(filename):
        logger.error("File %s does not exist", filename)
        raise FileNotFoundError(f"{filename} not found")

    df = pd.read_csv(filename, parse_dates=['Joining_Date'], dayfirst=True)

    if df.empty:
        logger.warning("Dataset is empty!")

    logger.info("Dataset schema:\n%s", df.dtypes)

    logger.info("Dataset sample:\n%s", df.head())

    logger.info("Total Records: %d", len(df))

    logger.info("Missing values:\n%s", df.isnull().sum())

    return df


def task2_data_cleaning(df):
    # filename='employees.csv'
    # df = pd.read_csv(filename, parse_dates=['Joining_Date'], dayfirst=True)

    # logger.info("Starting Data Cleaning")

    # missing values
    logger.info("Missing values:\n%s", df.isnull().sum())

    # Age
    age_median = df['Age'].median()
    df['Age'] = df['Age'].fillna(age_median)
    logger.info("Missing Age values replaced with median: %s", age_median)

    # Salary
    salary_mean = df['Salary'].mean()
    df["Salary"] = df['Salary'].fillna(salary_mean)
    logger.info("Missing Salary values replaced with mean: %s", salary_mean)

    before = len(df)
    df = df.drop_duplicates(subset=['Employee_ID'])
    after = len(df)

    logger.info("Removed %d duplicate records", before - after)


    # column naming seems fine from my side
    df.columns = df.columns.str.lower().str.replace(' ','_')
    print(df.columns)
    logger.info("Column names standardized")


    # seems fine from my side
    # df["Age"] = df['Age'].astype('int64')
    
    df = df.astype({
        "employee_id": "int64",
        "name": "string",
        "age": "int64",
        "department": "string",
        "salary": "float64",
        "joining_date": "datetime64[ns]",
        "resigned": "bool"
    })
    logger.info("Datatypes standardized")

    logger.info("Standardized columns and datatypes: \n%s",df.dtypes)

    return df

def task3_data_manipulation(df):
    # filename='employees.csv'
    # df = pd.read_csv(filename, parse_dates=['Joining_Date'], dayfirst=True)

    # filtering data based on: (age > 25 OR salary > 40000) AND not resigned
    before = len(df)
    df = df[
        ((df["age"] > 25) | (df["salary"] > 40000)) &
        (df["resigned"] == False)
    ]

    after = len(df)
    logger.info(f"Filtered employees where (age > 25 OR salary > 40000) AND not resigned. Records before: {before}, after: {after}")

    # adding new column YearsInCompany
    today = pd.Timestamp.today()
    df['YearsInCompany'] = (today - df['joining_date']).dt.days // 365

    logger.info(f"YearsInCompany column added, example:\n{df['YearsInCompany'].head(5)}") 

    return df

def task4_analysis(df):
    # filename='employees.csv'
    # df = pd.read_csv(filename, parse_dates=['Joining_Date'], dayfirst=True)

    # logger.info('Dataframe sample: \n%s',df.head(5))

    logger.info('unique departments %s', df['department'].unique())
    logger.info('Department-wise average salary \n%s', df.groupby('department')['salary'].agg(['mean']))
    logger.info('Department-wise median age \n%s', df.groupby('department')['age'].agg(['median']))

    logger.info('IT departments salaries before increment: \n%s',df.loc[df['department'] == 'IT','salary'].head(5))

    # salary increment of 10% to employees of IT department
    df.loc[df['department']=='IT','salary'] += df.loc[df['department']=='IT','salary'] * 0.1

    logger.info('IT departments salaries after increment: \n%s',df.loc[df['department'] == 'IT','salary'].head(5))

    return df

def task5_export(df):
    # filename='employees.csv'
    # df = pd.read_csv(filename, parse_dates=['Joining_Date'], dayfirst=True)
    # renaming 


    # sorting of dataset
    df.sort_values(by='joining_date',ascending=False,inplace=True)
    logger.info('Dataset sorted based on joining date: \n%s',df.loc[:,:].head(5))

    # keeping only necessary columns
    final_dataset = df.loc[:,['employee_id','name','age','department','salary','YearsInCompany']]
    logger.info('Final dataset sample: \n%s',final_dataset.loc[:,:].head(5))

    # data loading to json file
    final_dataset.to_json('employees.json',indent=4,orient='records')
    logger.info('Data Loaded Successfully')

    return df

def main(filename):
    # task-1
    task_logger('Data loading','start')
    try: 
        df = task1_data_loading(filename)
    except Exception as e:
        logger.exception('Error: %s',e)
        return
    finally:
        task_logger('Data loading',status='end')
    
    # task-2
    task_logger('Data Cleaning','start')
    try:
        df = task2_data_cleaning(df)
    except Exception as e:
        logger.exception('Error: %s',e)
        return
    finally:
        task_logger('Data Cleaning','end')

    # task-3
    task_logger('Data manipulation','start')
    try:
        df = task3_data_manipulation(df)
    except Exception as e:
        logger.exception('Error: %s',e)
        return
    finally:
        task_logger('Data manipulation','end')

    # task-4
    task_logger('Data analysis','start')
    try:
        df = task4_analysis(df)
    except Exception as e:
        logger.exception('Error: %s',e)
        return
    finally:
        task_logger('Data analysis','end')

    # task-5
    task_logger('Data export','start')
    try:
        df = task5_export(df)
    except Exception as e:
        logger.exception('Error: %s',e)
        return
    finally:
        task_logger('Data export','end')

    '''
    '''

main('employees.csv')