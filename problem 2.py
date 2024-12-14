def generate_series(a):
    """Generates a series of numbers up to the input number.

    Args:
        a: The input integer.

    Returns:
        A list containing the generated series.
    """

    series = []
    if a <= 0:
        return series  # Handle invalid input

    for i in range(1, a + 1, 2):
        series.append(i)

    return series

# Example usage:
a = int(input("Enter a number: "))
result = generate_series(a)
print(result)