# Counting Sundays
# 171

from datetime import date, timedelta

start_date = date(1901, 1, 1)
end_date = date(2000, 12, 31)
sundays = 0

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

for date in daterange(start_date, end_date):
    if date.weekday() == 6 and date.day == 1: sundays += 1

print(sundays)