def k_jump(arr, key, k):
    """
    Implements the k-jump (jump search) algorithm.
    Searches for 'key' in sorted array 'arr' using jumps of size 'k'.
    Returns the index of 'key' if found, else -1.
    """
    n = len(arr)
    i = 0

    # Jump in steps of k
    while i < n and arr[i] < key:
        i += k

    # Linear search in the previous block
    left = max(0, i - k)
    right = min(i, n)
    for j in range(left, right):
        if arr[j] == key:
            return j
    return -1

def binary_search(arr, key):
    """
    Implements the binary search algorithm.
    Searches for 'key' in sorted array 'arr'.
    Returns the index of 'key' if found, else -1.
    """
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == key:
            return m
        elif arr[m] > key:
            r = m - 1
        else:
            l = m + 1
    return -1

def linear_search(arr, key):
    """ Implements the linear search algorithm.
    Searches for 'key' in array 'arr'.
    Returns the index of 'key' if found, else -1.
    """             
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1