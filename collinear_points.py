# this program checks wheather three given coordinates lie on straight line or not 
x2, y2 = map(int,input("enter value of x2 and y2 seperated by space: ").split())  # note , between int and input that's required for map() function
x1, y1 = map(int,input("enter value of x1 and y1 seperated by space: ").split())  # split() and map() function helps in taking two inputs at a time
x3, y3 = map(int,input("enter value of x3 and y3 seperated by space: ").split())

if ((y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)):
    print("Points are collinear.")
else:
    print("Points aren't collinear.")