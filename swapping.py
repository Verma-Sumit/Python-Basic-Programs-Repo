a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print("Your values are a =",a,"b =",b, sep=",")
"""Swapping can be done in two ways,
    
    Lets start with using a third variable too"""
temp = a 
a = b
b = temp
""" We store the value of a in a temporary variable so that it can be used later by b, 
when a stores the value of b and loses its original value"""
print("swapped values:")
print("a = ",a)
print("b = ",b)


#swapping without using a third variable ( using + -)
a = a + b # stored added value of a and b in a
b = a - b # we have to store value of a in b, so we subtracted b from a and stored it in b
a = a - b # we have to store value of b in a, so we subtracted b (which stores value of a now) from a and stored it in a
print("swapped values:")
print("a = ",a)
print("b = ",b)


#swapping without using a third variable ( using * /)
a = a * b # stored multiplied value of a and b in a
b = a / b # we have to store value of a in b, so we divided b from a and stored it in b
a = a / b # we have to store value of b in a, so we divided b (which stores value of a now) from a and stored it in a
print("swapped values:")
print("a = ",a)
print("b = ",b)


#Using XOR
"""The XOR of two numbers x and y returns a number which has all the bits as 1 wherever bits of x and y differ. 
For example XOR of 10 (In Binary 1010) and 5 (In Binary 0101) is 1111 and XOR of 7 (0111) and 5 (0101) is (0010)."""
a = a ^ b
b = a ^ b
a = a ^ b
print("swapped values:")
print("a = ",a)
print("b = ",b)

# Lastly, I would like to tell you that we are using Python!!
# It means we really do not need to do much nuisance like above methods
# we can just take advantage of python's assignment techniques :
a , b = b , a 
print("swapped values:")
print("a = ",a)
print("b = ",b)

#Bye, Happy Coding, Don't forget to connect me on https://www.linkedin.com/in/sumit-verma-tech