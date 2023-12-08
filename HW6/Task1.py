def binary_search(arr, element):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == element:
            return mid  
        elif arr[mid] < element:
            left = mid + 1  
        else:
            right = mid - 1  

    return -1  

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 7
result = binary_search(arr, element)
if result != -1:
    print(f"Искомый элемент {element} найден в массиве, его индекс: {result}")
else:
    print(f"Искомый элемент {element} не найден в массиве")