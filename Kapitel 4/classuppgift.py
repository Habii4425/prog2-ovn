import random

guess = 0
correct = random.randint(1, 20)
while guess != correct:
    guess = int(input("Gissa på ett tall: "))
    
    if guess < correct:
      print(f"för litet")
    elif guess > correct:
      print(f"för stort")

print("Right Guess!")