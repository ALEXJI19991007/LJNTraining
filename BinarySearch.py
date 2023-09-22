def classical_binary_search(array, target):
    if array is None or len(array) == 0:
        return -1
    left = 0
    right = len(array) - 1
    while left <= right:
        midIndex = left + (right - left) // 2
        if array[midIndex] == target:
            return midIndex
        elif array[midIndex] < target:
            left = midIndex + 1
        else:
            right = midIndex - 1
    return -1


def first_occurrence(array, target):
    if array is None or len(array) == 0:
        return -1
    left = 0
    right = len(array) - 1
    while left < right - 1:
        midIndex = left + (right - left) // 2
        if array[midIndex] == target:
            right = midIndex
        elif array[midIndex] < target:
            left = midIndex + 1
        else:
            right = midIndex - 1
    if array[left] == target:
        return left
    if array[right] == target:
        return right
    return -1


def last_occurrence(array, target):
    if array is None or len(array) == 0:
        return -1
    left = 0
    right = len(array) - 1
    while left < right - 1:
        midIndex = left + (right - left) // 2
        if array[midIndex] == target:
            left = midIndex
        elif array[midIndex] < target:
            left = midIndex + 1
        else:
            right = midIndex - 1
    if array[right] == target:
        return right
    if array[left] == target:
        return left
    return -1


def closest_in_sorted_array(array, target):
    if array is None or len(array) == 0:
        return -1
    left = 0
    right = len(array) - 1
    while left < right - 1:
        midIndex = left + (right - left) // 2
        if array[midIndex] == target:
            return midIndex
        elif array[midIndex] < target:
            left = midIndex
        else:
            right = midIndex
    if abs(array[left] - target) < abs(array[right] - target):
        return left
    return right


def search_in_sorted_matrix(matrix, target):
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        return [-1, -1]
    row = len(matrix)
    col = len(matrix[0])
    left = 0
    right = row * col - 1
    while left <= right:
        midIndex = left + (right - left) // 2
        midRow = midIndex // col
        midCol = midIndex % col
        if matrix[midRow][midCol] == target:
            return [midRow, midCol]
        elif matrix[midRow][midCol] < target:
            left = midIndex + 1
        else:
            right = midIndex - 1
    return [-1, -1]


def k_closest_elements(array, target, k):
    result = []
    if len(array) == 0 or k == 0:
        return result
    closestIndex = closest_in_sorted_array(array, target)
    result.append(array[closestIndex])
    left = closestIndex - 1
    right = closestIndex + 1
    count = 1
    while count < k and (left >= 0 or right <= len(array) - 1):
        if left >= 0 and (right > len(array) - 1 or abs(array[left] - target) < abs(array[right] - target)):
            result.append(array[left])
            left = left - 1
        else:
            result.append(array[right])
            right = right + 1
    return result


array_1 = [1, 2, 4, 5, 7, 8, 9]
target_1 = 4
print(classical_binary_search(array_1, target_1))
