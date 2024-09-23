def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
numbers = [10, 501, 22, 37, 100, 19, 87, 351]
prime_numbers = [ ]
for num in numbers:
    if is_prime(num):
        prime_numbers.append(num)

print("Prime numbers:", prime_numbers)
