def main():
    username = input("Create a username - ")
    password = input("Create a password - ")
    password_length = len(password)
    hidden_password = '*' * (password_length - 4)
    formatted_password = password[0:2] + hidden_password + password[-2:]

    print(f'{username.capitalize()}, your password {formatted_password} is {password_length} characters long')


if __name__ == "__main__":
    main()
