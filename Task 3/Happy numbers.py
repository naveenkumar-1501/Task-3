def is_happy(num):
    seen = set()
    while num != 1:
        num = sum(int(digit) ** 2 for digit in str(num))
        if num in seen:
            return False 
        seen.add(num)
    return True
my_list = [10, 501, 22, 37, 100, 999, 87, 351]
happy_numbers = []
for num in my_list:
    if is_happy(num):
        happy_numbers.append(num)
print("Happy numbers in the list:", happy_numbers)
print("Total happy numbers found:", len(happy_numbers))
