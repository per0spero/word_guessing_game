# Here I wanted to create a word guessing game of a secret word. The user will have 1 prompt which could be used throughout the game
# But! It will also have limited number of guesses

print("Welcome to the Word Guessing Game! The secret word is green."
      "\nYou have only 5 guesses...But! You also have 1 prompt which you can use anytime in the game."
      "\nIn order to use the prompt write \"PROMPT\"")

guess_limit = 5
secret_word = "avocado"

guess_count = 0
guess = ""
out_of_guesses = False
out_of_prompt = False


while guess.lower() != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        if guess.upper() == "PROMPT" and not(out_of_prompt):
            print("It is full of omega-3 fatty acids, and it is tasty!")
            guess_count -= 1
            out_of_prompt = True
        elif guess.upper() == "PROMPT" and out_of_prompt:
            print("You are out of prompts!")
            guess_count -= 1
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
       out_of_guesses = True


if out_of_guesses:
    print("You are OUT of guesses :(")
else:
    print("You win! Congratulations!")







