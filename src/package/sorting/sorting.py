def selection_sort(A):
    for i in range(len(A)):
        min_index = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_index]:
                 min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A

def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

def insertion_sort(A):
    for i in range(1, len(A)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < A[j] :
                A[j + 1] = A[j]
                j -= 1
        A[j + 1] = key

def merge_sort(A):
    def helper(A, start, end):
        if start >= end:
            return
        mid = (start + end)//2
        helper(A, start, mid)
        helper(A, mid+1, end)
        i = start
        j = mid + 1
        aux = []
        while i <= mid and j <= end:
            if A[i] <= A[j]:
                aux.append(A[i])
                i += 1
            else:
                aux.append(A[j])
                j += 1
        while i <= mid:
            aux.append(A[i])
            i += 1
        while j <= end:
            aux.append(A[j])
            j += 1
        A[start:end+1] = aux
        return A
    return helper(A, 0, len(A) - 1)
