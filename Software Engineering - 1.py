import random
import string

def generate_password(length, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected")

    return ''.join(random.choices(characters, k=length))

def main():
    try:
        length = int(input("Enter the length of the password: "))
        include_options = [
            ("uppercase letters", True),
            ("lowercase letters", True),
            ("digits", True),
            ("special characters", True)
        ]
        for option, flag in include_options:
            flag_str = input(f"Include {option}? (yes/no): ").lower()
            if flag_str == 'no':
                include_options.remove((option, flag))
        password = generate_password(length, *map(lambda x: x[1], include_options))
        print("Generated Password:", password)
    except ValueError as ve:
        print("Error:", ve)

main()
