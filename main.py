import art
import random
print(art.logo)
print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100.")
nums = []
for i in range(2,100):
  nums.append(i)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
guess = random.choice(nums)
#print(guess)
attempts_easy = 10
attempts_hard = 5
if difficulty == "easy":
  print(f"You have {attempts_easy} attempts remaining to guess the number!")
  while attempts_easy > 0:
    guessed = int(input("Make a guess: "))
    attempts_easy-=1
    if guessed > guess:
      print("Too High!\n")
      print(f"You have {attempts_easy} attempts remaining")

    elif guessed < guess:
      print("Too Low!\n")
      print(f"You have {attempts_easy} attempts remaining")
    elif guessed == guess:
      print("Correct!")

    if attempts_easy == 0:
      print("You lose!\nYou have exhausted your attempts.")
elif difficulty == "hard":
  print(f"You have {attempts_hard} attempts remaining to guess the number.")
  while attempts_hard > 0:
    guessed = int(input("Make a guess: "))
    attempts_hard-=1
    if guessed > guess:
      print("Too High!\n")
      print(f"You have {attempts_hard} attempts remaining")

    elif guessed < guess:
      print("Too Low!\n")
      print(f"You have {attempts_hard} attempts remaining")
    elif guessed == guess:
      print("Correct!")

    if attempts_hard == 0:
      print("You lose!\nYou have exhausted your attempts.")
else:
 print("Wrong choice!")
