import random

correct = random.randint(1, 20)
guasses = 0

guess = 0
while guess != correct:
    guasses += 1
    guess = int(input("Gissa på ett tall mellan 1 och 20: "))
    
    if guess < correct:
      print(f"för litet")
    elif guess > correct:
      print(f"för stort")

    

print("Right Guess!")