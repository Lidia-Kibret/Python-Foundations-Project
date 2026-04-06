import math  # Import math module to use square root function

# Function to check if a number is prime
def is_prime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    
    # Loop from 2 to square root of n
    # math.sqrt(n) gives the square root
    # int(...) converts it to an integer
    # +1 ensures the range includes the last number
    for i in range(2, int(math.sqrt(n)) + 1):
        
        # If n is divisible by i, then it is not prime
        if n % i == 0:
            return False
    
    # If no divisor is found, the number is prime
    return True


# Ask user to enter a number
num = int(input("Enter a number: "))

# Check if the number is prime and print the result
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")