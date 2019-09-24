import time

epoch_time = time.time()
seconds_in_day = 24*60*60
seconds_in_hour = 60*60
second_in_minute = 60
days_passed = epoch_time // seconds_in_day

epoch_time = epoch_time % seconds_in_day
hours_passed = int(epoch_time // seconds_in_hour)
epoch_time = epoch_time % seconds_in_hour
minutes_passed = int(epoch_time // second_in_minute)
epoch_time = epoch_time % second_in_minute
seconds_passed = int(epoch_time)

print("Days since epoch:  " + str(int(days_passed)))
print("Current time is:  " + str(hours_passed) + ":" + str(minutes_passed) + ":" + str(seconds_passed))

