# safeah Hammosh
# Encoder function
def encode_password(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password



# Main function
def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode_password(password)
            print(f"Your password has been encoded and stored!")
        elif choice == "2":
            encoded_password = input("Please enter the encoded password: ")
            original_password = decode_password(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
        elif choice == "3":
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()
