temp = a 
# a = b
# b = temp
# """ We store the value of a in a temporary variable so that it can be used later by b, 
# when a stores the value of b and loses its original value"""
# print("swapped values:")
# print("a = ",a)
# print("b = ",b)


# #swapping without using a third variable ( using + -)
# a = a + b # stored added value of a and b in a
# b = a - b # we have to store value of a in b, so we subtracted b from a and stored it in b
# a = a - b # we have to store value of b in a, so we subtracted b (which stores value of a now) from a and stored it in a
# print("swapped values:")
# print("a = ",a)
# print("b = ",b)


# #swapping without using a third variable ( using * /)
# a = a * b # stored multiplied value of a and b in a
# b = a / b # we have to store value of a in b, so we divided b from a and stored it in b
# a = a / b # we have to store value of b in a, so we divided b (which stores value of a now) from a and stored it in a
# print("swapped values:")
# print("a = ",a)
# print("b = ",b)