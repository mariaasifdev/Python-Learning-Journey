correct_user_name = "Maria"
correct_password = "Python310"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    user_name = input("Enter a username: ")
    password = input("Enter a password: ")

    if user_name == correct_user_name and password == correct_user_name:
        print("Access granted!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Wrong password! {remaining} attempts remaining.") 

else:
    print("Account Locked!")