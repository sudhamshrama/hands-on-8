def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_select(arr, low, high, i):
    if low == high:
        return arr[low]

    pivot_index = partition(arr, low, high)
    k = pivot_index - low + 1

    if i == k:
        return arr[pivot_index]
    elif i < k:
        return quick_select(arr, low, pivot_index - 1, i)
    else:
        return quick_select(arr, pivot_index + 1, high, i - k)

# Example usage:
arr = [3, 7, 1, 9, 2, 5, 6, 4, 8]
i = 3
result = quick_select(arr, 0, len(arr) - 1, i)
print(f"The {i}th order statistic in the array {arr} is: {result}")
