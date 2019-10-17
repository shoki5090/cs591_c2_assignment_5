def multiply_string_nums (num1,num2):
    """Takes two string numbers and multiply and return the product in string"""
    # convert to int using helper method below
    num1_int = str_to_int(num1)
    num2_int = str_to_int(num2)
    # using f string to convert back to string
    ret = f"{num1_int*num2_int}"
    return ret

def str_to_int (num_string) :
    """Takes a number in string and returns number in int"""
    value_dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    num_int = 0
    # iterate per digit to compute int version
    for digit_char in num_string:
        num_int = 10 * num_int + value_dict[digit_char]

    return num_int

user_input1, user_input2 = input("Enter two numbers to multiply: ").split()
print(multiply_string_nums(user_input1,user_input2))
