import datetime as dt

init = dt.date(1900, 7, 8)
end = dt.date(2000, 12, 31)

count = 0
d = dt.timedelta(days = 7)
while init < end:
    if init.weekday() == 6 and init.day == 1:
        count += 1
        print(init)
    init += d
print(count)

print(dt.date(1998, 11, 1).weekday())