# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
import datetime
import time
def job_scheduler(f, n):

    n = n/1000 # transform to milliseconds

    while(1):
        time.sleep(n)
        f.__call__()

def f():
    print(datetime.datetime.now())

job_scheduler(f, 5)