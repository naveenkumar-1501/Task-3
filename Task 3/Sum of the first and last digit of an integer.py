def sum_of_first_and_last_digit(number):
    num_str = str(number)
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    total_sum = first_digit + last_digit
    return total_sum
user_number = int(input("Enter an integer: "))
result = sum_of_first_and_last_digit(user_number)
print(f"Sum of first and last digit: {result}")
