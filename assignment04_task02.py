# Task 2: Write and Append Data to a File

filename = "output.txt"

# Step 1: Write user input to the file
text_to_write = input("Enter text to write to the file: ")
with open(filename, "w") as file:
    file.write(text_to_write + "\n")
print(f"Data successfully written to {filename}.")

# Step 2: Append additional data
text_to_append = input("Enter additional text to append: ")
with open(filename, "a") as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.")

# Step 3: Read and display final content
print(f"\nFinal content of {filename}:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())
