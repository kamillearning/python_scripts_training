def int_checker(user_input):
    while True:
        try:
            return int(user_input)
        except ValueError:
            user_input = input("Unfortunately, the value is incorrect. Please provide numerical value: ")