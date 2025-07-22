def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

# Example usage
limit = 100  # Set the limit for Fibonacci numbers
for number in fibonacci(limit):
    print(number,"\t", end="")
