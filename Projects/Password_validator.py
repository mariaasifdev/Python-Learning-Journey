correct_password = "Python310"
max_attempts = 3
attempts = 0

while attempts < max_attempts:     # this condition will run until attempts are less than 3(max_attempts)
    password = input("Enter a password: ")

    if password == correct_password:   
        print("Acess Granted!")      # if we enter the right password, this will run as a final input and than the loop will break/exit
        break
    else:
        attempts += 1    # that's iteration, it will add our each attempt to previous one
        remaining = max_attempts - attempts
        print(f"Wrong password! {remaining} attempts remaining.")   # it will keep running until, we maxed out the max_attempts
else:
    print("Account locked!") # this will run as final output, when we run out of attempts