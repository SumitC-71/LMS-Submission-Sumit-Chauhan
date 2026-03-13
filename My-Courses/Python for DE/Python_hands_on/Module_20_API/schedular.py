from apscheduler.schedulers.background import BackgroundScheduler
import time

def job():
    print("Running scheduled task")

scheduler = BackgroundScheduler()

# runs daily at 17:06 o'clock
scheduler.add_job(job, 'cron', hour=17,minute=6)

# runs every 10 minutes
scheduler.add_job(job, 'interval', minutes=10)

scheduler.start()

timer = 1
while True:
    try:
        time.sleep(1)
        print(f'counter: {timer}')
        timer += 1
    except KeyboardInterrupt as e:
        print('Job Scheduler ended.')