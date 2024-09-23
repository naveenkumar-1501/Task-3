def find_first_non_repeating(nums):
    frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1
    for num in nums:
        if frequency_map[num] == 1:
            return num
    return None
my_list = [2, 4, 2, 6, 4, 6, 0]
result = find_first_non_repeating(my_list)
if result is not None:
    print(f"The first non-repeating element is: {result}")
else:
    print("No non-repeating elements found in the list.")

