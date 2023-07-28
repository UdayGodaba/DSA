a = [1,2,1]
e = []
s = 3

def subSeqSum(i, e, a, s):

    if i == len(a):
        if sum(e) == s:
            print(e)
        return
    e.append(a[i])
    subSeqSum(i+1, e, a, s)
    e.pop()
    subSeqSum(i+1, e, a, s)

subSeqSum(0, e, a, s)

#want to stop printing subsequences even we found one subsequence
print("We are printing only one subsequence which is satisfied first and we stop from there")

a = [1,2,1]
e = []
s = 3

def subSeqSum1(i, e, a, s):

    if i == len(a):
        if sum(e) == s:
            print(e)
            return True
        return False
    e.append(a[i])
    if subSeqSum1(i+1, e, a, s):
        return True
    e.pop()
    if subSeqSum1(i+1, e, a, s):
        return True
    return False

subSeqSum1(0, e, a, s)

#printing how many subsequences satisfy sum condition

print('Printing how many subsequences satisfy sum condition')

a = [1,2,1]
e = []
s = 3

def subSeqSum(i, e, a, s):

    if i == len(a):
        if sum(e) == s:
            return 1
        return 0
    e.append(a[i])
    l = subSeqSum(i+1, e, a, s)
    e.pop()
    r = subSeqSum(i+1, e, a, s)
    return l + r

print(subSeqSum(0, e, a, s))