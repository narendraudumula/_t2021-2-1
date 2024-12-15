# t2021-2-1
problem1.py

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")


# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")

    
problem2.py

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


problem3.py

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


problem4.py

elements = [1, 2, 3, 2, 1, 3, 2, 1, 1, 4, 5, 4, 4]
counts = {}
for element in elements:
    if element in counts:
        counts[element] += 1
    else:
        counts[element] = 1

for element, count in counts.items():
    print(element, ":", count)
