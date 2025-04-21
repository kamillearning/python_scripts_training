""" Exercise 1: 
This function script has the task of taking 2 values from the user, which determines in what range the array will be created. 
Then, even and odd numbers will be transferred to separate arrays. """ 

def split_numbers_to_arrays(number_from, number_to):
    even_array = []
    odd_array = []
    main_array = list(range(number_from, number_to + 1))
    for i in main_array:
        if i % 2 == 0:
            even_array.append(i)
        else:
            odd_array.append(i)
    print(f"Even: {even_array}")
    print(f"Odd: {odd_array}")

    return even_array, odd_array
