def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                # Обмен элементов, если текущий элемент меньше следующего
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# Пример использования:
numbers = [46, 34, 52, 21, 22, 17, 89]
sort_list_imperative(numbers)
print("Отсортированный список в порядке убывания:", numbers)