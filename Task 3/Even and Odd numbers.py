numbers = [10, 501, 22, 37, 100, 999, 87, 351]
even_numbers = [i for i in numbers if i%2==0]
odd_numbers =  [i for i in numbers if i%2!=0]
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)