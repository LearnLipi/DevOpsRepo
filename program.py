def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        print(x)
        return (x * factorial(x-1))


num = 3
print("The FACT of", num, "is", factorial(num))