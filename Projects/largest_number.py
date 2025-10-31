num = int(input("Enter a number(press 0 to stop): "))
largest = num

while num != 0:
    num = int(input("Enter a number(press 0 to stop): "))
    if num > largest:
        largest = num

print(f"The largest number is {largest}.")