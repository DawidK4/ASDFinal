def index_of_min(S, start, end):
    """
    Returns the index of the minimum element in S[start:end].
    """
    mini = start
    for j in range(start + 1, end):
        if S[j] < S[mini]:
            mini = j
    return mini

def swap(S, i, j):
    """
    Swaps elements S[i] and S[j].
    """
    S[i], S[j] = S[j], S[i]

def selection_sort(S):
    """
    Sorts the list S in place using selection sort.
    """
    n = len(S)
    i = 0
    while i < n:
        mini = index_of_min(S, i, n)
        swap(S, i, mini)
        i += 1

def insertion_sort(arr):
    """
    Sorts the list arr in place using insertion sort.
    """
    n = len(arr)
    for next in range(1, n):
        curr = next
        temp = arr[next]
        while curr > 0 and temp < arr[curr - 1]:
            arr[curr] = arr[curr - 1]
            curr -= 1
        arr[curr] = temp

def merge(a1, len1, a2, len2):
    """
    Merges two sorted lists a1 and a2 of lengths len1 and len2.
    Returns a new sorted list containing all elements from a1 and a2.
    """
    result = []
    i = j = 0
    while i < len1 and j < len2:
        if a1[i] < a2[j]:
            result.append(a1[i])
            i += 1
        else:
            result.append(a2[j])
            j += 1
    while i < len1:
        result.append(a1[i])
        i += 1
    while j < len2:
        result.append(a2[j])
        j += 1
    return result

def merge_sort(S, length=None):
    """
    Sorts the list S using merge sort and returns a new sorted list.
    """
    if length is None:
        length = len(S)
    if length <= 1:
        return S[:length]
    m = length // 2
    left = merge_sort(S[:m], m)
    right = merge_sort(S[m:length], length - m)
    return merge(left, len(left), right, len(right))