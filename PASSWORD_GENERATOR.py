import random
import string

# Get desired password length from user
password_length = int(input("Enter the desired length of the password: "))

# Define character sets for password complexity
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

# Combine all character sets for comprehensive password possibilities
all_characters = letters + numbers + symbols

# Generate the password using random.choices for weighted randomness
password = ''.join(random.choices(all_characters, k=password_length))

# Display the generated password
print("Your generated password is:", password)