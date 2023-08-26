#!/usr/bin/python3


# step 0
hat_list = [1, 2, 3, 4, 5]

# step 1
user_input = int(input("Enter a number: "))
hat_list[2] = user_input

# step 2
del hat_list[-1]

# step 3
print("List length:", len(hat_list))
print(hat_list)
