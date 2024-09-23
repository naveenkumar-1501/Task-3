def find_minimum_element(sorted_list):
    if sorted_list:
        return sorted_list[0]
    else:
        return None
my_sorted_list = [15, 30, 50, 105, 19]
result = find_minimum_element(my_sorted_list)
if result is not None:
    print(f"The minimum element in the sorted list is: {result}")
else:
    print("The list is empty.")
