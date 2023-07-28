def merge(a, b):

    c = []
    i = 0
    j = 0
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

def mergeSort(a):

    if len(a) == 1:
        return a
    mid = len(a)//2
    l = mergeSort(a[:mid])
    r = mergeSort(a[mid:])

    return merge(l, r)

print(mergeSort([4, 1, 3, 2]))