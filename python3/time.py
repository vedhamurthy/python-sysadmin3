#!/usr/bin/env python3.6
import time
#now = time.localtime()
#print(now)
start_time = time.localtime()
print(f"Timer started at {time.strftime('%X', start_time)}")

# Wait for user to stop timer
input("Press any key to stop timer ")

stop_time = time.localtime()
print(f"Timer stopped at {time.strftime('%X', stop_time)}")
difference = time.mktime(stop_time) - time.mktime(start_time)

print(f"Total time: {difference} seconds")
