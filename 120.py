date = 8
day = 0

if date % 7 == day:
    print("yes")


# for i in range(12):
#     if day % 7 == 0:
#         print(i)



days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
day_of_week = 1
count_sundays = 0

for year in range(1901, 2001):
    for month in range(12):
        if day_of_week == 0:
            count_sundays += 1
        days = days_in_month[month]
        if month == 1:
            if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                days = 29
        day_of_week = (day_of_week + days) % 7

print(count_sundays)






