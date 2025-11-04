# Take input from user
char = input("Enter a character: ")

# Check if it's an alphabet
if char.isalpha():
    print(f"'{char}' is an alphabet letter.")
else:
    print(f"'{char}' is NOT an alphabet letter.")