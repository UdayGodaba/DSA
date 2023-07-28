def mergeSort(a):

    if len(a) == 1:
        return a
    mid = len(a)//2
    l = mergeSort(a[:mid])
    r = mergeSort(a[mid:])
        
    return merge(l,r)

def merge(a, b):            #This merges only sorted list

    c =[]
    i=0
    j=0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c

print(mergeSort([10, 14, 28, 11, 7, 16, 30, 50, 25, 18, 28]))
print(mergeSort([4, 2, 6, 5, 1, 3]))
print(mergeSort([4, 2, -6, 5, -1, 3]))
print(mergeSort([4, 1, 3, 2]))