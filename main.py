year=int(input("Enter a year:"))

def leap_function(year):
    if (year%4==0 and year%400==0 or year%100!=0):
        return True
    else:
        return False


if (leap_function(year)):
    print("Year is leap year")
else:
    print("Year is not leap Year")

