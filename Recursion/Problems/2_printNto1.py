def printNto1(n):

    if n == 0:
        return
    print(n)
    printNto1(n - 1)

printNto1(5)

#With BackTracking

def printnto1(i, n):
    if i > n:
        return
    printnto1(i + 1, n)
    print(i)

printnto1(1, 5)