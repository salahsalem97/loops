# NO.1 Reverse the tuple
tuple1 = (10, 20, 30, 40, 50)

def Reverse(tuples):
    new_tuple = tuples[::-1]
    return new_tuple
print(Reverse(tuple1))

# *************************************
#  NO2Access value 20 from the tuple


tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

print(tuple1[1][1])


# ****************************
# NO 3 Unpack the tuple into 4 variables


tuple1 = (10, 20, 30, 40)

a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)

