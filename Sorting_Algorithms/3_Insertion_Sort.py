def Insertion_Sort(a):
    
    for i in range(len(a)-1):
        key_index = i + 1
        for j in range(key_index, 0, -1):
            if a[j - 1] > a[j] and j != 0:
                a[j], a[j-1] = a[j-1], a[j]
    return print(a)

Insertion_Sort([10, 14, 28, 11, 7, 16, 30, 50, 25, 18, 28])
Insertion_Sort([4, 2, 6, 5, 1, 3])
Insertion_Sort([4, 2, -6, 5, -1, 3])