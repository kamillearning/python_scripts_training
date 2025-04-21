# Check if type is int.
def get_valid_int(user_input):
    while True:
        try:
            return int(user_input)
        except ValueError:
            user_input = input("Unfortunately, the value is incorrect. Please provide numerical value: ")

# Check if second value is larger than first value.
def get_larger_than(min_value, user_value):
    while True:
        if user_value > min_value:
            return user_value
        else:
            user_value = get_valid_int(input("Second value must be larger than the first one. Try again: "))
