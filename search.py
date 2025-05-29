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

def tournament_min_and_second_min(arr):
    """
    Finds the minimum and second minimum element using the tournament method.
    Returns a tuple: (min_value, second_min_value)
    """
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements.")

    # Each element is a tuple: (value, [elements it defeated])
    nodes = [(x, []) for x in arr]

    # Tournament phase: build the tree
    while len(nodes) > 1:
        next_round = []
        for i in range(0, len(nodes), 2):
            if i + 1 < len(nodes):
                # Compare two elements
                if nodes[i][0] < nodes[i+1][0]:
                    winner = (nodes[i][0], nodes[i][1] + [nodes[i+1][0]])
                else:
                    winner = (nodes[i+1][0], nodes[i+1][1] + [nodes[i][0]])
                next_round.append(winner)
            else:
                # Odd element advances automatically
                next_round.append(nodes[i])
        nodes = next_round

    min_value, defeated = nodes[0]
    # Second minimum is the smallest among those defeated by the winner
    second_min_value = min(defeated)
    return min_value, second_min_value