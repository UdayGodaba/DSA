def print1toN(i, n):
    if i > n:
        return
    print(i)
    print1toN(i + 1, n)

print1toN(1,5)

# with BackTracking

def print1ton(i):

    if i == 0:
        return
    print1ton(i - 1)
    print(i)

print1ton(5)