def sort_list_declarative(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers

# Пример использования:
numbers = [46, 34, 52, 21, 22, 17, 89]
sorted_numbers = sort_list_declarative(numbers)
print("Отсортированный список в порядке убывания:", sorted_numbers)