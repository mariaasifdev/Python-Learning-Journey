num = int(input("Enter a number: "))
factorial = 1
counter = num

while counter > 0:
    factorial *= counter
    counter -= 1

print(f"Factorial of {num} is {factorial} ")