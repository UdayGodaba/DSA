def Selection_Sort(a):

    for i in range(len(a)-1):
        min_index = i
        for j in range(i+1, len(a)):
            if a[min_index] > a[j]:
                min_index = j                                       #in this complexity is O(n**2)
        a[i], a[min_index] = a[min_index], a[i]
    return print(a)

Selection_Sort([10, 14, 28, 11, 7, 16, 30, 50, 25, 18, 28])
Selection_Sort([4, 2, 6, 5, 1, 3])
Selection_Sort([4, 2, -6, 5, -1, 3])
Selection_Sort([4,3,-2,1])
