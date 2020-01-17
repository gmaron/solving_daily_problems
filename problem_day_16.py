# You run an e-commerce website and want to record the last N order ids in a log. 
# Implement a data structure to accomplish this, with the following API:

#    record(order_id): adds the order_id to the log
#    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

# You should be as efficient with time and space as possible.

from random import randrange

log = []

def record(order_id):
    log.append(order_id)

def get_last(i):
    return log[i-1]



for i in range(10):
    record(randrange(10))
    


print("Log", log)
print("get_last(9)", get_last(9))
print("get_last(8)", get_last(8))