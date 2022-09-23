# question NO. 1//  Display numbers from a list using a loop
from unittest import result


numbers = [12, 75, 150, 180, 145, 525, 50]
result = []

for i in numbers:
    if i >= 500:
        break

    if i % 5 == 0 and i <= 150:
        result.append(i)
    else:
        continue
print(result)


# ***********************************
# 2_ Use else block to display a message “Done” after successful execution of for loop
for i in range(5):
    print(i)
else:
    print("Done!")

# *************************************
# 3_Reverse a given integer number

# Ask for enter the number from the use
number = int(input("Enter the integer number: "))
revs_number = 0

while (number > 0):
    remainder = number % 10
    revs_number = (revs_number * 10) + remainder
    number = number // 10

# Display the result
print(revs_number)


# *******************************************

