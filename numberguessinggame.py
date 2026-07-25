import random

secret = random.randint(1, 50)
attempts = 5
won = False

while attempts > 0:
    guess = int(input("Guess the number(1-50): "))
    if guess == secret:
        print("Congratulations! You've guessed the number!")
        won = True
        break
    difference = abs(secret - guess)
    if difference <= 3:
        print("🔥🔥 Hot")
    elif difference <= 7:
        print("🌡️ Warm")
    elif difference <= 15:
        print("🧊 Cold")
    else:
        print("❄️ Freezing")

    attempts -= 1

print("Lives:",end="")
for i in range(attempts):
    print("❤️", end="")
if not won:
    print("\n🩻🩻 Game over! The number was {secret}")
    
