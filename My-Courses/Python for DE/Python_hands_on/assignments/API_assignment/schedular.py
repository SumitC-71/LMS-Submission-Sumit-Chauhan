from db_client import insert_records_into_posts, get_users_posts_count
from api_client import fetch_data
from config_logger import get_logger
from apscheduler.schedulers.background import BackgroundScheduler
import time
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
logger = get_logger()

# scheduled job to fetch and insert new posts every 10 minutes
def job():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # fetching data from /posts end-point
    post_records = fetch_data(os.getenv('POSTS_API_URL'))
    
    if post_records:
        # insert posts and get count of new records added
        new_posts = insert_records_into_posts(post_records.json())
        # get total users and posts in DB
        total_users, total_posts = get_users_posts_count()
        # print summary report
        print(f"\n{'='*50}")
        print(f"SUMMARY REPORT - {timestamp}")
        print(f"{'='*50}")
        print(f"Total Users: {total_users[0]}")
        print(f"Total Posts: {total_posts[0]}")
        print(f"New Posts Added: {new_posts}")
        print(f"{'='*50}\n")
        
        # log to file
        logger.info(f"Scheduled execution at {timestamp}. Added {new_posts} new posts.")
    else:
        logger.error(f"Failed to fetch posts at {timestamp} - API returned None")

# initialize scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(job, 'interval', seconds=10)
scheduler.start()

print("Scheduler started. Running scheduled task every 10 minutes...")

# keep application running indefinitely
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    scheduler.shutdown()
    print("Scheduler stopped.")
