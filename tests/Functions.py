def square(a):
    """
    Square a number

    Parameters:
    a (float): Number to square

    Returns:
    float: square of a
    """
    return a * a


def divide(a, b):
    """
    Divide two numbers

    Parameters:
    a (float): counter
    b (float): denominator

    Returns:
    float: division of a and b
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
