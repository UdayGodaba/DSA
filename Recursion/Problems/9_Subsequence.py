a = [3, 1, 2]
e = []
sub_list = []

def subSeq(i, e, a, sub_list):

    if i == len(a):
        sub_list.append(e.copy())
        return
    e.append(a[i])
    subSeq(i+1, e, a, sub_list)
    e.pop()
    subSeq(i+1, e, a, sub_list)

subSeq(0, e, a, sub_list)
print(sub_list)