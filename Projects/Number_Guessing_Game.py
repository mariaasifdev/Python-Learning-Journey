import random   # it's a built-in module
secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1  # an iteration, keep adding our attempts attempts

    if guess == secret_number:
        print(f"Correct! You got it in {attempts} attempts.")
        break  # if the condition met, the loop break here.
    elif guess < secret_number:
        print("Too low!") # or else keep givig us this, whenever we enter lower number
    else:
        print("Too High!") 
