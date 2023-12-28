logo = """ 
   _____                      _   _            _   _                 _                
  / ____|                    | | | |          | \ | |               | |               
 | |  __ _   _  ___ ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __  
 | | |_ | | | |/ _ / __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ | '__| 
 | |__| | |_| |  __\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __| |    
  \_____|\__,_|\___|___|___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|    
                                             
"""   
import random


print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

number = random.randint(0,100)
print(number)
def easy():
  lives = 10
  print("You have 10 attempts remaining to guess a number.")
  game_over = False
  while not game_over:
    guess = int(input("Make a guess: "))
    if guess > number:
      print("Too high.")
      lives -= 1
      print(f"You have {lives} attempts remaining to guess the number")
      if lives == 0:
        print("You've run out of guesses, you lose.")
        game_over = True
    elif guess < number:
      print("Too low.")
      lives -= 1
      print(f"You have {lives} attempts remaining to guess the number")
      if lives == 0:
        print("You've run out of guesses, you lose.")
        game_over = True
    elif guess == number:
      print(f"You got it! answer was {number}")
      game_over = True

  
def hard():
  lives = 5
  print("You have 5 attempts remaining to guess a number.")
  game_over = False
  while not game_over:
    guess = int(input("Make a guess: "))
    if guess > number:
      print("Too high")
      lives -= 1
      print(f"You have {lives} attempts remaining to guess the number")
      if lives == 0:
        print("You've run out of guesses, you lose.")
        game_over = True
    elif guess < number:
      print("Too low")
      lives -= 1
      print(f"You have {lives} attempts remaining to guess the number")
      if lives == 0:
        print("You've run out of guesses, you lose.")
        game_over = True
    elif guess == number:
      print(f"You got it! answer was {number}")
      game_over = True


if difficulty == "easy":
  easy()
else:
  hard()






#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

