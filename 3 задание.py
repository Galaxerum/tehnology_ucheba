def filter_greater_than(arr, threshold):
    res = []
    for num in arr:
        if num > threshold:
            res.append(num)
    return res


print(filter_greater_than([1, 5, 8, 3, 10], 5))

