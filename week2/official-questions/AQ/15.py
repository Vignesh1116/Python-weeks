# On what day of the week were you born? If you don't know the answer to this, use the calendar library to get the answer.

import calendar

year = int(input())
month = int(input())
day = int(input())

print(calendar.day_name[calendar.weekday(year, month, day)])
