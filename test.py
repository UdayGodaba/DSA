n = int(input("Enter target: "))
m = int(input("No of primes you can use from starting: "))

a = []
i = 2

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

while len(a) < m:
    if isPrime(i):
        a.append(i)
    i += 1

# dp = [[None for _ in range(n + 1)] for _ in range(m + 1)]

# def f(idx, target):
#     if target == 0:
#         return 0
#     if idx == m:
#         return 1e9
    
#     if dp[idx][target] != None:
#         return dp[idx][target]
    
#     take = 1e9
#     if target >= a[idx]:
#         take = f(idx, target - a[idx]) + 1
#     notTake = f(idx + 1, target)

#     dp[idx][target] = min(take, notTake)
#     return dp[idx][target]
# print(f(0, n))

dp = [[None for _ in range(n + 1)] for _ in range(m + 1)]

for idx in range(m + 1):
    dp[idx][0] = 0
for target in range(1, n + 1):
    dp[m][target] = 1e9

for idx in range(m - 1, -1 , -1):
    for target in range(n + 1):
        take = 1e9
        if target >= a[idx]:
            take = dp[idx][target - a[idx]] + 1
        notTake = dp[idx + 1][target]
        dp[idx][target] = min(take, notTake)

print(dp[0][n])