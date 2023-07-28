import re


def fibo(n):
    if n == 1 or n == 0:
        return n
    return fibo(n -1) + fibo(n-2)

n = int(input("Enter a number to print Fibonacci Series : "))

for i in range(n+1):
    print(fibo(i))