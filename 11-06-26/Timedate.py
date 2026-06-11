# Date and Time Module in Python

import datetime
now = datetime.datetime.now()
print(now)

# Current date Only

today = datetime.date.today()
print(today)

# Custom Date

custom = datetime.date(2025,12,12)
print(custom)

#Access Year, month, Day

today = datetime.date.today()
print("Year:",today.year)
print("Month:",today.month)
print("Day:",today.day)

#strtime()

now = datetime.datetime.now()

formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print(formatted)

# date difference

d1 = datetime.date(2002, 12, 1)
d2 = datetime.date(2026, 6, 11)

difference = d2 - d1
print(difference.days)


# 2. Time module in Python
'''
    - working with system time
    - delays in programme
    - measuring execution time
'''

# import time module

import time

current = time.time()
print(current)
# it returns seconds from January 1 1970.

# Pause programme using sleep()

print("Start Programme")
time.sleep(30)
print("Programme ends after 3 seconds")


# current local time
local = time.localtime()
print(local)


# Froamte time
current = time.strftime("%H:%M:%S")
print(current)


# Measure exicution time
start = time.time()

for i in range(1000000):
    pass

end = time.time()

print("Exicution Time:", end - start)


# Display current Date and Time
from datetime import datetime, timedelta

now = datetime.now()
print(now)

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hours:", now.hour)
print("Minutes:", now.minute)
print("Seconds:", now.second)



# datetime.utcnow()
'''return current utc time'''
print(datetime.utcnow())



obj = datetime.strptime(date, "%Y-%m-%d") 
print(obj)

#  timedelta

today = datetime.now()

future = today + timedelta(days=5)
print(future)

# replace()

now = datetime.now()

new_date = now.replace(year=2030)
print(new_date)



now = datetime.now()
print(now.weekday())



print(now.isoweekday())


# ctime()

print(now.ctime())



now = datetime.now()
print(now.timestamp())



s = 174986300
print(datetime.fromtimestamp(s))


# Python Time Module Methods

# 1. time()
# 2. ctime()
# 3. sleep()
# 4. localtime()

# 5. gmtime()
print(time.gmtime())



t = time.localtime()
print(time.mktime(t))


t = time.localtime()
print(time.asctime(t))



print(time.monotonic())
