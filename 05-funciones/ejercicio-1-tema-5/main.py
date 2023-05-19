def check_leap_year(year):
    return not year % 4 and (year % 100 or not year % 400)


input_year = int(input("Type a year: "))


print("It's a leap year" if check_leap_year(input_year) else "It isn't a leap year")
