import random
import string
password_length = int(input("Enter the  length of the password: "))

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
password = generate_password(password_length)
print("Generated Password:", password)