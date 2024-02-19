a = "1010"
x = 1
for i in range(-x, -len(a) - 1, -x):
    print(a[i], i, abs(i) % x)
