# Memoization      Top-Bottom    Time : O(n)       Space : O(n) stack space + O(n) Dict space
def fibo(value, dp = {}):
    
    if value <= 1:
        return value
    
    if dp.get(value, False):
        return dp.get(value)

    dp[value] =  fibo(value - 1) + fibo(value - 2)

    return dp[value]


# Tabulation       Bottom-Top    Time : O(n)  Space : O(n)
def fibo1(value):

    if value <= 1:
        return value
    a = [0, 1]
    for i in range(2, value + 1):
        a.append(a[i-1] + a[i-2])
    return a[-1]

# Still optimization on space for Tabulation        Time : O(n)   Space : O(1)
def fibo2(value):
    
    if value <= 1:
        return value
    prev1, prev2 = 1, 0
    for _ in range(2, value + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return curr

print(fibo(50),fibo1(50),fibo2(50))
print(fibo(4),fibo1(4),fibo2(4))
print(fibo(3),fibo1(3),fibo2(3))
print(fibo(2),fibo1(2),fibo2(2))
print(fibo(1),fibo1(1),fibo2(1))
print(fibo(0),fibo1(0),fibo2(0))