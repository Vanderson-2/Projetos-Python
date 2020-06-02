import schedule
import time

def to_do():
    print('test')

schedule.every(10).seconds.do(to_do)

while 1:
    schedule.run_pending()
    time.sleep(1)