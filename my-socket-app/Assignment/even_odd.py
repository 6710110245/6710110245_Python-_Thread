def check_even_odd(number):
    """
    Function to check if a number is even or odd.
    :param number: The number to check (int)
    :return: A string indicating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"
