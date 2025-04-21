# This is main.py file, where the scripts will be run.
from main_functions import *
from check_functions import *

# The user enters from what to what value the array is to be created. Then, the function divides the main array into 2 other arrays, which are divided into even and odd.
start_value = get_valid_int(input("Specify the value from which you want to create an array: "))
end_value = get_larger_than(start_value, get_valid_int(input("Specify the value on which you want to end the array: ")))
print("Let's divide the entered values into even and odd arrays.")

# We returned 2 divided arrays on which we can perform further operations.
even, odd = split_numbers_to_arrays(start_value, end_value)

# Basic operations to check operation
print(f"Added values from an even array: {sum(even)}") 
print(f"Added values from an odd array: {sum(odd)}") 
