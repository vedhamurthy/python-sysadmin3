#!/usr/bin/env python3.6
#import time
from time import localtime, mktime, strftime
#now = time.localtime()
#print(now)
start_time = localtime()
print(f"Timer started at {strftime('%X', start_time)}")

# Wait for user to stop timer
input("Press any key to stop timer ")

stop_time = localtime()
print(f"Timer stopped at {strftime('%X', stop_time)}")
difference = mktime(stop_time) - mktime(start_time)

print(f"Total time: {difference} seconds")
