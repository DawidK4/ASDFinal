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

