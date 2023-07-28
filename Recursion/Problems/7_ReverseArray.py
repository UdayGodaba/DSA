a = [1,2,3,4,5]
b = [1,2,3,4]

def revArray(a, i, j):           # Reversing using two pointers

    if i >= j:
        print(a)
        return
    a[i], a[j] = a[j], a[i]
    revArray(a, i+1, j-1)

revArray(a, 0, len(a) - 1)
revArray(b, 0, len(b) - 1)

a = [1,2,3,4,5]
b = [1,2,3,4]

def revArray1(a, i):             #  Only using single pointer
    
    if i >= len(a)-i-1:
        print(a)
        return
    a[i] ,a[len(a)-1-i] = a[len(a)-i-1], a[i]
    revArray1(a, i+1)

revArray1(a, 0)
revArray1(b, 0)