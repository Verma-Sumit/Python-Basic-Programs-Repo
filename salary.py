# WAP to input basic salary of an employee and calculate TA,
# DA, HRA and Net Salary as per the criteria given below:
# Basic Sal       TA(%) DA(%) HRA(%)
# above 10000      75   50     40
# 8000 – 9999      50   40     30
# 5000 – 7999      30   20     10
# <5000            NIL  NIL    NIL
# Net Salary= Basic Sal + TA + DA + HRA
sal = float(input("Hey! What's your basic salary? ::"))
ta=0
da=0
hra=0
if sal > 10000:
    ta = 75/100 * sal
    da = 50/100 * sal
    hra = 40/100 * sal
elif sal>=8000 and sal<10000:
    ta = 50/100 * sal
    da = 40/100 * sal
    hra = 30/100 * sal
elif sal>=5000 and sal<8000:
    ta = 30/100 * sal
    da = 20/100 * sal
    hra = 10/100 * sal
else:
    ta=0
    da=0
    hra=0
fsal=sal+ta+da+hra
print("Your full salary, TA, DA, HRA are:", fsal,ta,da,hra, sep=",")
10000
