from config_logger import get_logger
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

logger = get_logger()


def insert_records_into_users(json_records):
    conn = psycopg2.connect(
        database=os.getenv('DB_NAME')
        , user=os.getenv('DB_USER')
        , password=os.getenv('DB_PASSWORD')
        , host=os.getenv('DB_HOST')
        , port=os.getenv('DB_PORT')
    )
    new_added_records=0
    try:
        records = [
            (
                item['id'], 
                item['name'], 
                item['email'], 
                f"{item['address'].get('street', '')}, {item['address'].get('city', '')}, {item['address'].get('state', '')}"
            )
            for item in json_records
        ]
        # print(records)
        cur = conn.cursor()
        # insert all records in one batch
        cur.executemany(
            'insert into users(id, name, email, address) values (%s, %s, %s, %s) ON CONFLICT (email) DO NOTHING',
            records  
        )
        conn.commit()
        new_added_records = cur.rowcount
        print(f'{cur.rowcount} user records inserted successfully')

    except Exception as e:
        conn.rollback()
        logger.error(f'Error inserting records: {e}')
    finally:
        cur.close()
        conn.close()

    return new_added_records


def insert_records_into_posts(json_records):
    conn = psycopg2.connect(
        database=os.getenv('DB_NAME')
        , user=os.getenv('DB_USER')
        , password=os.getenv('DB_PASSWORD')
        , host=os.getenv('DB_HOST')
        , port=os.getenv('DB_PORT')
    )
    new_record_count=0
    try:
        cur = conn.cursor()
        records = [
            (
                item['id']
                , item['user_id']
                , item['title']
                , item['body']
            )
            for item in json_records
        ]
        # insert all records in one batch
        # here unique(user_id, title) contraint suggest that one user cannot have multiple blogs with same title
        cur.executemany(
            'insert into posts(id, user_id, title, body) values (%s, %s, %s, %s) ON CONFLICT (user_id, title) DO NOTHING',
            records
        )
        conn.commit()
        new_record_count=cur.rowcount
        print(f'{cur.rowcount} post records inserted successfully')

    except Exception as e:
        conn.rollback()
        logger.error(f'Error inserting records: {e}')
    finally:
        cur.close()
        conn.close()

    return new_record_count


def get_users_posts_count():
    conn = psycopg2.connect(
        database=os.getenv('DB_NAME')
        , user=os.getenv('DB_USER')
        , password=os.getenv('DB_PASSWORD')
        , host=os.getenv('DB_HOST')
        , port=os.getenv('DB_PORT')
    )
    cur = conn.cursor()
    total_users=0
    total_posts=0
    try:
        user_query = 'select count(id) from users'
        post_query = 'select count(id) from posts'
        cur.execute(user_query)
        total_users = cur.fetchone()
        cur.execute(post_query)
        total_posts = cur.fetchone()

    except Exception as e:
        logger.error(f'Error occured while fetching total users or posts: {e}')
        return (None,None)
    finally:
        cur.close()
        conn.close()
    
    return total_users,total_posts

# driver code
# users_records = fetch_data(users_api)
# print('user records fetched successfully')

# # sample record
# print('USER RECORD: ')
# print(users_records.json()[0])
# insert_records_into_users(users_records.json())

# posts_records = fetch_data(posts_api)

# # sampel record
# print('POST RECORD: ')
# print(posts_records.json()[0])
# insert_records_into_posts(posts_records.json())

# total_users,total_posts = get_users_posts_count()
# print(total_users,total_posts)