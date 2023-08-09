def fibonacci_iterative(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    return fib_sequence

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
        return fib_sequence

num_terms = int(input("Enter the number of Fibonacci numbers to generate: "))

iterative_fibs = fibonacci_iterative(num_terms)
recursive_fibs = fibonacci_recursive(num_terms)

print("Fibonacci numbers (iterative):", iterative_fibs)
print("Fibonacci numbers (recursive):", recursive_fibs)
