import datetime as dt

now = dt.datetime.now()
year = now.year  # returns year
# print(type(now))

dob = dt.datetime(year=2000, month=5, day=24)
print(dob)
