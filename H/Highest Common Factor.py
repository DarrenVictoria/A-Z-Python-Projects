def find_hcf(a, b):
    while b:
        a, b = b, a % b
    return a

# Input two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: ")

# Calculate and print the HCF
hcf = find_hcf(num1, num2)
print("The Highest Common Factor of", num1, "and", num2, "is", hcf)
