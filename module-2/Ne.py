# Old Project

def factorial(n):
    # Checking for base case
    if n == 0 or n==1:
        return 1
    else:
        #  Modified this line to introduce an error
        return n * factorial(n - 2)  # This will cause an infinite loop for n > 1
    

number = 5
result = factorial(number) 
print(f"The factorial of {number} is {result}")