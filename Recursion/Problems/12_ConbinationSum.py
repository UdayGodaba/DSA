candidates = [2,3,6,7]
target = 7
res = []

def combSum(i, e, res, t, a):
            
    if t == 0:
        res.append(e.copy())
    if t <= 0 or i == len(a):
        return
    combSum(i, e + [a[i]], res, t - a[i], a)
    combSum(i + 1, e, res, t, a)

combSum(0, [], res, target, candidates)
print(res)