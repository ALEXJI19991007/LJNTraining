import random


def selection_sort(array):
    if array is None or len(array) == 0:
        return array
    for i in range(0, len(array)):
        smallestIndex = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallestIndex]:
                smallestIndex = j
        array[i], array[smallestIndex] = array[smallestIndex], array[i]
    return array


def bubble_sort(array):
    if array is None or len(array) == 0:
        return array
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


def merge_sort(array):
    if array is None or len(array) == 0:
        return array
    # This is the biggest problem -- the original problem
    merge_sort_helper(array, 0, len(array) - 1)
    return array


def merge_sort_helper(array, left, right):
    if left >= right:
        return
    # Find the middle point
    mid = left + (right - left) // 2
    # Sort left half
    merge_sort_helper(array, left, mid)
    # Sort right half
    merge_sort_helper(array, mid + 1, right)
    # After left and right half are both sorted, we merge them together
    merge_left_and_right(array, left, mid, mid + 1, right)


def merge_left_and_right(array, leftStart, leftEnd, rightStart, rightEnd):
    if leftStart == rightStart:
        return
    initialIndex = leftStart
    buffer = []
    # Merge left and right array into the buffer array
    while leftStart <= leftEnd and rightStart <= rightEnd:
        if array[leftStart] < array[rightStart]:
            buffer.append(array[leftStart])
            leftStart = leftStart + 1
        else:
            buffer.append(array[rightStart])
            rightStart = rightStart + 1
    while leftStart <= leftEnd:
        buffer.append(array[leftStart])
        leftStart = leftStart + 1
    while rightStart <= rightEnd:
        buffer.append(array[rightStart])
        rightStart = rightStart + 1
    # Overwrite original array
    for i in range(0, len(buffer)):
        array[initialIndex] = buffer[i]
        initialIndex = initialIndex + 1


def quick_sort(array):
    if array is None or len(array) == 0:
        return array
    quick_sort_helper(array, 0, len(array) - 1)
    return array


def quick_sort_helper(array, left, right):
    if left >= right:
        return
    partitionIndex = partition(array, left, right)
    # This is the left sub-problem
    quick_sort_helper(array, left, partitionIndex - 1)
    # This is the right sub-problem
    quick_sort_helper(array, partitionIndex + 1, right)


def partition(array, begin, end):
    pivotIndex = random.randint(begin, end)
    array[pivotIndex], array[end] = array[end], array[pivotIndex]
    left = begin
    right = end - 1
    while left <= right:
        if array[left] < array[end]:
            left = left + 1
        else:
            array[left], array[right] = array[right], array[left]
            right = right - 1
    array[end], array[left] = array[left], array[end]
    return left


array_1 = [5, 4, 3, 2, 1, 0]
print(quick_sort(array_1))
