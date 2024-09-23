def find_triplet_with_sum(nums, target_sum):
    n = len(nums)
    nums.sort()
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target_sum:
                return [nums[i], nums[left], nums[right]]
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1
    return None
my_list = [10, 20, 30, 9]
target_value = 59
result = find_triplet_with_sum(my_list, target_value)
if result:
    print(f"The triplet with sum {target_value} is: {result}")
else:
    print("No such triplet found in the list.")

