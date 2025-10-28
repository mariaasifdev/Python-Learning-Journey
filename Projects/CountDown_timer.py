import time

countdown = int(input("Enter countDown in seconds: "))

while countdown > 0:
    print(f"Time remaining: {countdown} seconds!")
    time.sleep(1)
    countdown -= 1

print("Time's Up!")