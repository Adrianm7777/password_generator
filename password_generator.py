import secrets
import string

def get_yes_no(prompt):
    while True:
        response = input(prompt).lower()
        if response in ['y', 'n']:
            return response == 'y'
        print("Please enter 'y' or 'n'.")

def get_password_length():
    while True:
        try:
            length = int(input("Enter password length (8-50): "))
            if 8 <= length <= 50:
                return length
            print("Length must be between 8 and 50!")
        except ValueError:
            print("Please enter a valid number!")

def generate_password(length, use_letters, use_digits, use_symbols):
    if not (use_letters or use_digits or use_symbols):
        return None, "Error: At least one character type must be selected!"
    
    chars = ""
    if use_letters:
        chars += string.ascii_letters  
    if use_digits:
        chars += string.digits 
    if use_symbols:
        chars += string.punctuation  
    
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password, None

def save_password(password, description):
    with open("passwords.txt", "a") as file:
        file.write(f"{description}: {password}\n")
    print(f"Saved password for '{description}' to passwords.txt")

def main():
    print("\nSimple Password Generator")
    print("Customize your password and generate a secure random password.")
    
    while True:
        length = get_password_length()
        use_letters = get_yes_no("Include letters (a-z, A-Z)? (y/n): ")
        use_digits = get_yes_no("Include digits (0-9)? (y/n): ")
        use_symbols = get_yes_no("Include symbols (!@#$%)? (y/n): ")
        
        password, error = generate_password(length, use_letters, use_digits, use_symbols)
        if error:
            print(error)
            continue
        
        print(f"\nGenerated Password: {password}")
        
        if get_yes_no("Save this password? (y/n): "):
            description = input("Enter a description (e.g., Email account): ")
            if description.strip():
                save_password(password, description)
            else:
                print("Description cannot be empty! Password not saved.")
        
        if not get_yes_no("Generate another password? (y/n): "):
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()