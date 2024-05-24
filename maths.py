import math
print("input to math.acos must be in range of [-1,1] else it will give domain error \n also input to math.log must be >0 \n\n")
x = float(input("Enter yout number as integer or fraction: "))
y = float(input("Enter the second value in case you need math.hypot function else input 0 : "))

print(math.pi)   # values of constants pi
print(math.e)    # values of constants e
print(math.sqrt(x))  # square root of x
print(math.factorial(int(x))) # factorial of x
print(math.fabs(x))  # absolute value of float x
print(math.log(x))  #natural log of x (log to the base e)
print(math.log10(x))  # base-10 logarithm of x
print(math.exp(x))  #e raised to x
print(math.trunc(x))  # truncate to integer 
#The trunc function truncates a floating-point number to its integer part by removing the fractional part.
print(math.ceil(x))  # smallest integer >= x
print(math.floor(x))  #largest integer <= x
print(math.modf(x))  # fractional and integer parts of x
print(math.degrees(x))  # radians to degrees
print(math.radians(x))  # degrees to radians
print(math.sin(x))  # sine of x radians
print(math.cos(x))  # cosine of x radians
print(math.tan(x))  # tan of x radians
print(math.sinh(x))  # hyperbolic sine of x
print(math.cosh(x))  #hyperbolic cosine of x
print(math.tanh(x))  #hyperbolic tan of x
print(math.acos(x))  # cos inverse of x, in radians
print(math.asin(x))  # sine inverse of x, in radians
print(math.atan(x)) # tan inverse of x, in radians
print(math.hypot (x, y)) #sqrt( x ^ * x+y^ * y)