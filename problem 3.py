def generate_series(a):
    """Generates a series of numbers based on the input 'a'.

    Args:
        a: The input integer.

    Returns:
        A list of numbers in the generated series.
    """

    series = []
    if a <= 1:
        series.append(1)
        return series

    for i in range(1, a + 1, 2):
        series.append(i)

    return series

# Example usage:
a = int(input("Enter the value of a: "))
result = generate_series(a)
print(result)