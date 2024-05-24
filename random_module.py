import math
import random

x = int(input("Enter start value for random number in range: "))
y = int(input("Enter stop value for random number in range: "))

print(random.random())  # random number between 0 and 1
print((random.randint(x,y)))  #random number in the range x,y

(random.seed())  #sets current time as seed for random number generation
print(random.random())
(random.seed(x))  #set x as seed for random number generation logic
print(random.random())