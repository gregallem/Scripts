#!/usr/bin/env python
def fibonacci_terms(n):
    """Generate Fibonacci sequence with n terms."""
    if n <= 0:
        print("Number of terms must be positive.")
        return []
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

# Example usage
num_terms = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence with {num_terms} terms: {fibonacci_terms(num_terms)}")
