import datetime
current_time = datetime.datetime.now()
print(current_time)

# creating datetime object
custom_time = datetime.datetime(2012, 4, 26, 18 ) # year, month, date, hr, minute, second
print(custom_time)


# computing time differences
now = datetime.datetime.now()
bday = datetime.datetime(2001, 6, 16)
diff = now - bday
print(diff)


# basic datetime object usage
print(datetime.date.today()) # prints today's date
print(datetime.time(12, 0, 0)) # prints noon time


# switching between timezones
from dateutil import tz
utc = tz.tzutc()
local = tz.tzlocal()
print(datetime.utcnow())