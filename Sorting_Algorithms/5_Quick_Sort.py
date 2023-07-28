def pivot(a, pivot_index, end_index):

    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if a[i] < a[pivot_index]:
            swap_index += 1
            a[swap_index], a[i] = a[i], a[swap_index]
    a[pivot_index], a[swap_index] = a[swap_index], a[pivot_index]

    return swap_index

def quickSortHelper(a, left, right):
    if left < right:
      pivot_index = pivot(a, left, right)
      quickSortHelper(a, left, pivot_index -1)
      quickSortHelper(a, pivot_index + 1, right)

    return a

def quickSort(a):
    
    return quickSortHelper(a, 0, len(a) - 1)

print(quickSort([10, 14, 28, 11, 7, 16, 30, 50, 25, 18, 28]))
print(quickSort([4, 2, 6, 5, 1, 3]))
print(quickSort([4, 2, -6, 5, -1, 3]))
print(quickSort([4, 1, 3, 2]))