def find_duplicates(list1, list2, list3):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    common_elements = set1 & set2 & set3
    return common_elements
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 2]
list3 = [5, 6, 3, 8, 2]
duplicates = find_duplicates(list1, list2, list3)
if duplicates:
    print("Common elements found:", duplicates)
else:
    print("No common elements among the lists.")
