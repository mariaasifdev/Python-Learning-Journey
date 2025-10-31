num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10  # here, i add iteration and it removes the last digit from num. 1234, 123, 12, 1, 0

print(f"Reversed: {reversed_num}")