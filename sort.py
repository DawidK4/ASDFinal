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