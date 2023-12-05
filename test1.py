target = 19

def f(idx, target):
    if target == 0:
        return True
    if idx == n:
        return False
    
    if dp[idx][target] != None:
        return dp[idx][target]
    
    take = False
    if target - coins[idx] >= 0:
        take = f(idx + 1, target - coins[idx])
    if take:
        return True
    notTake = f(idx + 1, target)
    if notTake:
        return True

    dp[idx][target] = take or notTake
    return dp[idx][target]

res = []
coins = [1, 4, 10] 
for i in range(1, target + 1):
    n = len(coins)
    dp = [[None for _ in range(target + 1)] for _ in range(n + 1)]
    if f(0, i) == False:
        res.append(i)

print(res)