import time
import datetime

today = datetime.date.today()
eventday = datetime.date(2026, 2, 13)
dday = abs(today-eventday)

print(today)
print(eventday)
print(dday)
print(dday.days)