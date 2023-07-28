# Using Recursion

def minCost(n, cost):
    if n == 0:
        return 0
    l = minCost(n-1, cost) + abs(cost[n] - cost[n-1])
    if n > 1:
        r = minCost(n-2, cost) + abs(cost[n] - cost[n-2])
    else:
        r = 10000   # to compare we need a value so im using some big value so that we can return only l
    return min(l, r)

# Using Memoization        we reduced calling something which is already done      Time : O(n)    Space : O(n) stack space + O(n) dp space

def minCost1(n, cost, dp = {}):
    if n == 0:
        return 0
    
    if dp.get(n, False):
        return dp[n]

    l = minCost1(n-1, cost) + abs(cost[n] - cost[n-1])
    if n > 1:
        r = minCost1(n-2, cost) + abs(cost[n] - cost[n-2])
    else:
        r = float("inf")  # to compare we need a value so im using some big value so that we can return only l
    
    dp[n] = min(l, r)
    return dp[n]

# Using Tabulation           we reduce stack space      Time : O(n)       Space : O(n)

def minCost2(cost, a = []):
    a.append(0)
    for i in range(1, len(cost)):
        l =  a[i - 1] + abs(cost[i] - cost[i-1])
        if i > 1:
            r = a[i-2] + abs(cost[i] - cost[i-2])
        else:
            r = 100000
        a.append(min(l,r))
    return a[-1]


# Still Optimizing Space Space : O(1)
def minCost3(cost):
    prev1, prev2 = 0, 0
    for i in range(1, len(cost)):
        l =  prev1 + abs(cost[i] - cost[i-1])
        if i > 1:
            r = prev2 + abs(cost[i] - cost[i-2])
        else:
            r = 100000
        curr = min(l, r)
        prev2 = prev1
        prev1 = curr
    return curr


cost = [10, 20, 30, 10]
print(minCost(len(cost)-1, cost))
print(minCost1(len(cost)-1, cost))
print(minCost2(cost))
print(minCost3(cost))