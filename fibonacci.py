#Problem: Write a function to generate the first n numbers in the Fibonacci sequence.

def fibonacci(n):
    fib = [0, 1]
    for i in range(2,n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

print(fibonacci(10))
