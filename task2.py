def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] == x:
            return (iterations, arr[mid])
        elif arr[mid] < x:
            low = mid + 1
        else:  # arr[mid] > x
            upper_bound = arr[mid]
            high = mid - 1

    return (iterations, upper_bound)


# Приклад
arr = [2.2, 4.5, 4.7, 11.3, 39.8]
x = 5.5
result = binary_search(arr, x)

if result[1] is not None:
    print(f"Iterations: {result[0]}, Upper bound: {result[1]}")
else:
    print(
        f"Iterations: {result[0]}, Upper bound not found (x is greater than all elements or array is empty)"
    )
