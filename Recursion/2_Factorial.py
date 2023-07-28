def fact(value):
    
    if value == 1:
        return value
    if value == 0:
        return value + 1
    return value*fact(value - 1)

print(fact(5))
print(fact(4))
print(fact(3))
print(fact(2))
print(fact(1))
print(fact(0))