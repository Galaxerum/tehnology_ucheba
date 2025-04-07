def find_min_max(arr):
    if not arr:
        return None, None
    min_val = max_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val


print(find_min_max([3, 1, 4, 1, 5, 9]))