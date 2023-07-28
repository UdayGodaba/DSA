def printSum(n, sum):   #Using Parametrised Recursion
    
    if n == 0:
        print(sum)
        return
    sum += n
    printSum(n - 1, sum)

printSum(9, 0)

def printSum1(n):   # Using Functional Recursion

    if n == 0:
        return 0
    return n + printSum1(n - 1)

print(printSum1(9))