from apscheduler.schedulers.background import BackgroundScheduler
import time

def job():
    print("Running scheduled task")

scheduler = BackgroundScheduler()

scheduler.add_job(job, 'interval', seconds=10)

scheduler.start()

timer = 1
while True:
    time.sleep(1)
    print(f'counter: {timer}')
    timer += 1