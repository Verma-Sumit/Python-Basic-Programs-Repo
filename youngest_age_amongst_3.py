#This program finds youngest person amongst three persons
A = int(input("Enter age of first person (A): "))
B = int(input("Enter age of second person (B): "))
C = int(input("Enter age of third person (C): "))
if A <= B and A <= C:
    print("A is youngest")
elif B <= A and B <= C:
    print("B is youngest")
else:
    print("C is youngest")