def factorial(n: int):
    """How to find n factorial in python"""
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return fact

print(factorial(10))