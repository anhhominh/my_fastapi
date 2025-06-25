import schedule
import time

def job():
    print("I'm a scheduled job!")

# Schedule the job to run daily at a specific time
schedule.every().day.at("10:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)