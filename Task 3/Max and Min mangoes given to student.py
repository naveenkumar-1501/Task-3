def distribute_mangoes(mangoes, num_students):
    sorted_mangoes = sorted(mangoes)
    n = len(sorted_mangoes)
    min_difference = float('inf') 
    best_distribution = None
    for start in range(n):
        current_distribution = []
        for i in range(num_students):
            bag_index = (start + i) % n
            current_distribution.append(sorted_mangoes[bag_index])
        current_difference = max(current_distribution) - min(current_distribution)
        if current_difference < min_difference:
            min_difference = current_difference
            best_distribution = current_distribution
    
    return best_distribution
mangoes_list = [10, 7, 15, 5, 12]
num_students = 3
result = distribute_mangoes(mangoes_list, num_students)
print("Best distribution:", result)
print("Minimum difference:", max(result) - min(result))
