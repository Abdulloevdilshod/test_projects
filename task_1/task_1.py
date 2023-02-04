def in_days():
    days = int(input('Enter days: \n'))
    year = days // 365
    weeks = (days - year * 365) // 7

    days = days - (year * 365) - (weeks * 7)
    return f'Years : {year}\nweeks: {weeks}\ndays: {days}'


print(in_days())
