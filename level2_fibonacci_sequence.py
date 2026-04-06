# Function to generate Fibonacci sequence
def fibonacci(n):
    sequence = []          # Create an empty list to store the sequence
    a, b = 0, 1            # Initialize the first two Fibonacci numbers
    for i in range(n):     # Loop n times to generate n terms
        sequence.append(a) # Add the current number to the sequence
        a, b = b, a + b    # Update a and b for next term (next = sum of previous two)
    return sequence        # Return the full Fibonacci sequence

# Ask user for number of terms
terms = int(input("Enter number of terms: "))

# Print the Fibonacci sequence
print("Fibonacci sequence:", fibonacci(terms))