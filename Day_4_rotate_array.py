def rotate_left(arr, d):
    n = len(arr)
    d = d % n
    print(d)
    return arr[d:] + arr[:d]
arr = [1, 2, 3, 4, 5]
print(rotate_left(arr, 2))