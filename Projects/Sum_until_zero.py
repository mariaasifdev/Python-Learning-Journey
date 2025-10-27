total = 0

while True:
    num = int(input("Enter a number (press 0 to stop): "))

    if num == 0:   # if we wanted to stop the loop, we gonna press 0 to meet this condition, so that loop will break and exit
        break

    total += num   # it's an iteration, which will keep adding our numbers
    print(f"Current sum: {total}")   # this loop will run until we press 0

print(f"Final sum: {total}")  # after pressing 0, this will run as a final input
