def bisect_left(arr, x):
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo+hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def bisect_right(arr, x):
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo+hi) // 2
        if x < arr[mid]:
            hi = mid
        else:
            lo = mid + 1
