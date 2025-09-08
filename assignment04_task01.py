# Task 1: Read a File and Handle Errors

filename = "sample.txt"

try:
    with open(filename, "r") as file:
        print("Reading file content:\n")
        for line_num, line in enumerate(file, start=1):
            print(f"Line {line_num}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
