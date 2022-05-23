# Example 1

def exampleRecusrion(n):
    if n < 1:
        print('n<1. Terminate')
    else:
        exampleRecusrion(n-1)
        print(n)


# exampleRecusrion(4)


# Example 2: power of 2

# approach 1: Iteration:

def powerTwo(n):
    i = 0
    power = 1
    while i < n:
        power = power*2
        i = i+1
    return power


# print(powerTwo(0))

# approach 2: recursion:

def powerTowRecusrion(n):
    if n == 0:
        return 1
    else:
        return 2*powerTowRecusrion(n-1)


# print(powerTowRecusrion(4))

# Example 3: factorial of a number

# solution:

def factorial(n):
    assert n >= 0 and int(
        n) == n, 'The number must be a positive integer only!'
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


# print(factorial(-4))

# Example 4: Fibonacci Number:


def fibonacci(n):
    assert int(n) == n and n >= 0, 'The number must be a positive integer only!'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# print(fibonacci(8))


# Interview Questions:

# 1. find the sum of digits of a positive integer number using recursion:

# Solution:

def sumPositiveInteger(n):
    assert n >= 0 and int(n) == n, 'the number must be a positive integer!'
    if n == 0:
        return n
    else:
        return n % 10 + sumPositiveInteger(int(n/10))


# print(sumPositiveInteger(-5765))

# 2. Calculate power of a number using recursion:

# soluntion:

def powerOfNumber(b, n):
    assert int(n) == n and n >= 0, 'the number must be a positive integer!'
    if n == 0 and b != 0:
        return 1
    else:
        return b*powerOfNumber(b, n-1)


# print(powerOfNumber(8, 2))

# 3. How to find the GCD (Greatest Common Divisor) of two numbers using recursion?

def GCD(x, y):
    assert int(y) == y and int(
        x) == x, 'x and y must be an integer'

    if x < 0:
        x = -1*x
    if y < 0:
        y = -1*y
    if y == 0:
        return x
    else:
        return GCD(y, x % y)


# print(GCD(-18, -48))

# 4. How to convert a number from Decimal to Binary using recursion:


def decTobinary(n):
    assert n >= 0, 'n must be a positive integer'
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decTobinary(int(n/2))


print(decTobinary(156))
