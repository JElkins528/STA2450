#Write a function that will take an integer and return a list of its proper factors
factor = []
def find_factors(x):
    """
    Calculates the Factors of an entered integer

    Parameters:
    A number: An entered integer

    Returns:
    The factors of the integer: A list of integers
    """
    for i in range(1,x):
        if x % i == 0:
            factor.append(i)
    return factor

#Write another function that will take an integer and return a string that states if the integer is abundant, deficient, or perfect
def number_type(x):
    """
    Identifies number as being abundant, deficient, or perfect

    Parameters:
    A number: An entered integer

    Returns:
    Type of number: a string telling user if their number is abundant, deficient, or perfect
    """
    factor.clear()
    find_factors(x)
    if sum(factor) == x:
        print(f"The integer {x} is a perfect number")
    elif sum(factor) < x:
        print(f"The integer {x} is a deficient number")
    elif sum(factor) > x:
        print(f"The integer {x} is an abundant number")


#Write a third function that will take an integer and finds any perfect numbers that are less than that integer and returns a list of those perfect numbers
#If there are no perfect numbers less than that integer, then print a string to the console stating so
perfect_numbers = []
def find_perf(x):
    """
    Finds all perfect numbers less than an entered integer

    Parameters:
    A number: An entered integer

    Returns:
    A list of perfect numbers: A list of integers
    """
    number_list = list(range(1, x+1))
    for n in number_list:
        factor.clear()
        find_factors(n)
        if sum(factor) == n:
            perfect_numbers.append(n)
    if len(perfect_numbers) == 0:
        print("There are no perfect numbers less than this integer")
    else:
        return perfect_numbers

#Example
y = int(input("Enter an integer: "))
print(find_factors(y))
number_type(y)
print(find_perf(y))





