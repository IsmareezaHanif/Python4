def check_positive_number(num):
    if num < 0:
        raise ValueError("The number must be positive!")
    return num

# Example usage
num = int(input("Enter a number: "))
try:
    check_positive_number(num)
except ValueError as e:
    print(e)