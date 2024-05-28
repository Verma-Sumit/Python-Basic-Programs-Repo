"""Program to get radius and centre of circle input from user along with a coordinate 
and check weather it lies inside, outside or on the circle."""

import math
h,k = map(int,input("Enter the coordinates of center of the circle seperated by a space: ").split())
r = int(input("Enter the radius of circle: "))
x,y = map(int,input("Enter the coordinates of point to be checked, seperated by a space: ").split())

distance = math.sqrt((x - h) * (x - h) + (y - k) * (y - k)) #distance between center and point 

if distance < r :
    print("Point is inside the circle")
elif distance == r:
    print("Point is on the circle")
else:
    print("Point is outside the circle")


# # The above code will give error due to the comparison distance == r in the if statement.
"""When dealing with floating-point numbers, 
it's generally not a good idea to check for equality due to potential precision issues.
In this case, the distance calculated using math.sqrt() 
might result in a floating-point number that is not exactly equal to r, 
even though logically it should be considered as being on the circle.
To fix this, you can use a tolerance level for the comparison. 
Instead of checking for equality, you can check if the absolute difference between 
distance and r is less than a small value, like 1e-9 for instance, 
which accounts for small differences due to floating-point precision.
Here's the modified code:"""

# import math

# h, k = map(int, input("Enter the coordinates of center of the circle separated by a space: ").split())
# r = int(input("Enter the radius of circle: "))
# x, y = map(int, input("Enter the coordinates of point to be checked, separated by a space: ").split())

# distance = math.sqrt((x - h) ** 2 + (y - k) ** 2)  # distance between center and point

# tolerance = 1e-9
# if abs(distance - r) < tolerance:
#     print("Point is on the circle")
# elif distance < r:
#     print("Point is inside the circle")
# else:
#     print("Point is outside the circle")
