def fib(value):
    a = [0, 1]
    for i in range(2, value + 1):
        a.append(a[i - 1] + a[i - 2])
    return a[-1] if value != 0 else 0

def recFib(value):
    if value <= 1:
        return value
    return recFib(value - 1) + recFib(value - 2)

def recFibUsingDP(value, dp = {}):
    if value <= 1:
        return value
    
    res = dp.get(value, None)

    if res is not None:
        return res

    dp[value] = recFibUsingDP(value - 1) + recFibUsingDP(value - 2)

    return dp[value]
    


print(fib(0), recFib(0))
print(fib(5), recFib(5))
print(fib(7), recFib(7))
print(fib(10), recFib(10))
print(fib(15), recFib(15))
print(fib(40), recFibUsingDP(40))