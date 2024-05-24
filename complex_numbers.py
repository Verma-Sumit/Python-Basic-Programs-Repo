a = (float(input("Enter real part: ")))
b = (float(input("Enter imaginary part: ")))
z = complex(a, b)

print("The complex number is: ",z)
print("Its real part is: ", z.real)
print("Its imaginary part is: ", z.imag)
print("Its conjugate is: ", z.conjugate())

if(type(z)== complex):
    print("You made a complex number")
else:
    print("Not a complex number")
    
