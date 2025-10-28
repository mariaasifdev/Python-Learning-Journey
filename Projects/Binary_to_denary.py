binary = input("Enter a binary number: ")  # Getting user input

# initailize variables
denary = 0
position = 0
index = len(binary) - 1

# Using while loop to convert binary to denary
while index >= 0:
    digit = binary[index]

    # checking if digits are valid
    if digit == '1':
        denary = denary + (2 ** position)  # if this condition is true than, this will add 2^position to the denary value

    elif digit == '0':
        pass  # Do nothing, just move to the next digit

    # Let's give a condition, if user put values other than binary
    else:
        denary = -1     # the output of binary convertion shouldn't be negative
        print("Error: Invalid binary number!")
        break

    index -= 1
    position += 1

# Display output
if denary >= 0:
    print(f"Binary {binary} = Denary {denary}")

# binary = 1011
# indexing = 1[0], 0[1], 1[2], 1[3]
# # index -= 1 --> you go from right to left
# # so you read bits as: 1[3], 1[2], 0[1], 1[0]

# position = 1*2**3, 0*2**2, 1*2**1, 1*2**0
# # position += 1 --> powers of 2 increase as we move left to right in the binary
# # but during the loop, position counts upward (0-->3) as index counts downward (3-->0)

# Denary to Binary

# Get denary input from user
denary = int(input("Enter a denary number: "))

# Handle special case
if denary == 0:    # If the number is 0, I already know the binary is just 0 — no need to calculate.
    print("Binary: 0")  # If the condition was true, it simply prints the answer --> Binary: 0
else:
    # Store the original number for display
    original = denary   # Keep a copy of the original number for later display
    binary = ""         # Create an empty string to store the binary digits

    # convert denary to binary using while loop
    while denary > 0:               # Keep looping until number fully divided
        remainder = denary % 2      # Find binary digit (0 or 1)

        # checking remainder
        if remainder == 1:
            binary = "1" + binary    # Take the current binary string and put a 1 at the front of it — because that’s how binary builds up when we divide by 2 repeatedly
        elif remainder == 0:
            binary = "0" + binary

        else:
            print("Error in conversion!")
            break

        # Divide by 2 for next iteration
        denary = denary // 2

# adding space and display output
binary = " ".join(binary)
print(f"Denary {original} = Binary {binary}")


