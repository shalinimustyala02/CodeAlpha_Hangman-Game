import random

# Unique predefined words (all 5 letters)
words = ["cloud", "robot", "pixel", "frame", "engine"]

secret_word = random.choice(words)
guessed_word = ["_"] * len(secret_word)

lives = 6

print("Welcome to Hangman Game!")
print("Guess the word.\n")

while lives > 0 and "_" in guessed_word:
    print("Word:", " ".join(guessed_word))
    print("Lives left:", lives)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    if guess in guessed_word:
        print("You already guessed this letter.\n")
        continue

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
        print("Correct guess!\n")
    else:
        lives -= 1
        print("Wrong guess!\n")

if "_" not in guessed_word:
    print("You won! The word was:", secret_word)
else:
    print("Game Over! The word was:", secret_word)
