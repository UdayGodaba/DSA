a = [1, 2, 4]

def subSeq(i, e, a, l):
    if i == len(a):
        l.append(e)
        return
    subSeq(i + 1, e + [a[i]], a, l)
    subSeq(i + 1, e, a, l)

e = []
l = []
subSeq(0, e, a, l)
print(l)