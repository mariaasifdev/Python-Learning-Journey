n = int(input("Enter a number: "))
count = 0  # It will count the even numbers

num = 1

while num <= n:
    if num % 2 == 0:
        count += 1
    num += 1

print(f"There is {count} even numbers up to {n}")

