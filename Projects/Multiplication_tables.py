# Ask how many tables to print
count = int(input("How many multiplication tables? "))
i = 1

while i <= count:
    num = int(input(f"Enter number {i} : "))
    print(f"\n--- Table of {num} ---")

    for j in range(1, 11):
        print(f"{num} X {j} = {num * j}")
    i += 1