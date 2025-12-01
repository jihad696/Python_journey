import datetime


Date = datetime.date(2021, 6, 25)
dateNow = datetime.date(2021, 8, 10)

print(f"Days From {Date} To {dateNow} Is => {(dateNow - Date).days} Days")

# ============

# 2#

DateNow = datetime.datetime(1982, 10, 25)

print(DateNow)
print(DateNow.strftime("%a"))
print(DateNow.strftime("%A"))
print(DateNow.strftime("%b"))
print(DateNow.strftime("%B"))

print(DateNow.strftime("%d %B %Y"))
print(DateNow.strftime("%d, %B, %Y"))
print(DateNow.strftime("%d/%B/%Y"))
print(DateNow.strftime("%d - %B - %Y"))
print(DateNow.strftime("%B - %Y"))
