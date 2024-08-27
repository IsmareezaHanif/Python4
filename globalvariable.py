
counter = 0

def increment_counter():
    global counter
    counter += 1
    print(f"Global counter: {counter}")

def reset_counter():
    counter = 0 
    print(f"Local counter: {counter}")


increment_counter()
print(f"After increment 1, global counter: {counter}")

increment_counter()
print(f"After increment 2, global counter: {counter}")

increment_counter()
print(f"After increment 3, global counter: {counter}")

reset_counter()
print(f"After reset, global counter: {counter}")

# File and Directory Operations

import os

cwd = os.getcwd()
print(f"Current working directory: {cwd}")

files_and_dirs = os.listdir(cwd)
print(f"Files and directories in {cwd}: {files_and_dirs}")

os.mkdir('test_dir')

os.chdir('test_dir')

new_cwd = os.getcwd()
print(f"New working directory: {new_cwd}")

with open('test_file.txt', 'w') as file:
    file.write('This is a test file.')

os.remove('test_file.txt')
os.chdir('..')
os.rmdir('test_dir')


def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    else:
        return result
    finally:
        print("Division operation completed.")

a = 10
b = 2 

result = divide_numbers(a, b)
if result is not None:
    print(f"The result of dividing {a} by {b} is {result}.")

b = 0 

result = divide_numbers(a, b)
if result is not None:
    print(f"The result of dividing {a} by {b} is {result}.")
