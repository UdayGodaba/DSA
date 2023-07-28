def calPower(x, n):
    if n == 0:              #Stack height is n
        return 1
    if x == 0:
        return 0
    return x*calPower(x,n-1)

print(calPower(2, 8))
print(calPower(2, 7))

def calPower1(x, n):
    if x == 0:
        return 0
    if n == 1:
        return x            #Stack height log(n)
    if n%2 == 0:
        return calPower1(x, n//2)*calPower1(x, n//2)
    else:
        return x*calPower1(x, n//2)*calPower1(x, n//2)

print(calPower1(-10,4))
print(calPower1(-10,3))