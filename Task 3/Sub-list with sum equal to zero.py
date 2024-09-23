def has_zero_sum_sublist(nums):
    prefix_sum = set()
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum == 0 or current_sum in prefix_sum:
            return True
        prefix_sum.add(current_sum)
    return False
my_list = [4, 2, 3, 1, -6]
result = has_zero_sum_sublist(my_list)
if result:
    print("Yes, there exists a sub-list with a sum of zero.")
else:
    print("No such sub-list found with a sum of zero.")