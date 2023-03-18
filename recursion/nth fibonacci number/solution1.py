def fib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fib(n-1)+fib(n+1)
# O(2^n) time | O(n) space