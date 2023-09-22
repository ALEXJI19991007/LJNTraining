import heapq


def find_kth_largest(nums, k):
    num_1 = []
    for i in range(len(nums)):
        num_1.append(-nums[i])
    heapq.heapify(num_1)
    result = 0
    for i in range(k):
        result = heapq.heappop(num_1)
    return -result


def merge_k_sorted_array(array_of_arrays):
    if array_of_arrays is None or len(array_of_arrays) == 0:
        return []
    min_heap = []
    for array in array_of_arrays:
        if len(array) > 0:
            heapq.heappush(min_heap, (array[0], array, 0))
    heapq.heapify(min_heap)
    result = []
    while len(min_heap) > 0:
        top_tuple = heapq.heappop(min_heap)
        # This is the current index we are at the current array
        current_index = top_tuple[2]
        current_array = top_tuple[1]
        if current_index + 1 < len(current_array):
            heapq.heappush(min_heap, (current_array[current_index + 1], current_array, current_index + 1))
        # Add to the result
        result.append(top_tuple[0])
    return result
