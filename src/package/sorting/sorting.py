def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                 min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def insertion_sort(array):
    n = len(array)
    def helper(array,n):
        if n <= 1:
            return
        helper(array, n-1)
        j = n-1
        while j >= 1 and array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            j -= 1
        return array
