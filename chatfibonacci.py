#!/usr/bin/env python
def fibonacci_upto(max_value):
    """Generate Fibonacci sequence up to a maximum value."""
    if max_value < 0:
        print("Maximum value must be non-negative.")
        return []
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= max_value:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Example usage
max_val = int(input("Enter the maximum value: "))
print(f"Fibonacci sequence up to {max_val}: {fibonacci_upto(max_val)}")
