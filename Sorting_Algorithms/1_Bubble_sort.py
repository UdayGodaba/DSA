def Bubble_sort(a):
    for i in range(len(a) - 1):
        x = 1
        for j in range(len(a) - x):             # in this we find max first and O(n**2)
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j] 
        x += 1
    return print(a)


Bubble_sort(a = [10, 14, 28, 11, 7, 16, 30, 50, 25, 18, 28])
Bubble_sort(a = [4, 2, 6, 5, 1, 3])
Bubble_sort(a = [4, 2, -6, 5, -1, 3])
