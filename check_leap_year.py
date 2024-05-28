year = int(input("Enter a year: "))

if year % 4 == 0:         # % is arithmetic operator that gives remainder
    print(str(year)+" is a leap year! :-)")
else:
    print(str(year) + " isn't a leap year :-(")
