# datetime modeule is used to get the current date and time

import datetime as dt

now = dt.datetime.now() 
print(now.weekday()) # 0 is Monday, 1 is Tuesday, 2 is Wednesday, 3 is Thursday, 4 is Friday, 5 is Saturday, 6 is Sunday

date_of_birth = dt.datetime(year=2000, month=9, day=23, hour=5)
print(date_of_birth)