# Name - Krisha Hemani
#      - Justin Ha
# Program - Practice
# Date - 02/6/2024
# Module 2 - Hangman
# Purpose - To create a game of hangman

import check_input
import random
from dictionary import words


def display_gallows(num_incorrect):
  print()
  if num_incorrect == 0:
    print("========\n||/    |\n||\n||\n||\n||")
  elif num_incorrect == 1:
    print("========\n||/    |\n||     o\n||\n||\n||")
  elif num_incorrect == 2:
    print("========\n||/    |\n||     o\n||     |\n||\n||")
  elif num_incorrect == 3:
    print("========\n||/    |\n||     o\n||     |\n||    /\n||")
  elif num_incorrect == 4:
    print("========\n||/    |\n||     o\n||     |\n||    / \\\n||")
  elif num_incorrect == 5:
    print("========\n||/    |\n||    \\o\n||     |\n||    / \\\n||")
  elif num_incorrect == 6:
    print("========\n||/    |\n||    \\o/\n||     |\n||    / \\\n||")
  print()


def display_letters(letters):
  for char in letters:
    print(char, end=" ")
  print()


def get_letters_remaining(incorrect, correct):
  remaining_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
  for letters in incorrect + correct:
    if letters in remaining_letters:
      remaining_letters.remove(letters)
  return remaining_letters


def main():
  print("-Hangman-")
  repeat = True
  while repeat:
    word = random.choice(words)
    incorrect_guesses = []
    correct_guesses = ['_', '_', '_', '_', '_']
    num_incorrect = 0
    num_correct = 0

    while num_incorrect < 6 and num_correct < 5:
      print("\nIncorrect sections:", end=" ")
      display_letters(sorted(incorrect_guesses))
      display_gallows(num_incorrect)
      display_letters(correct_guesses)
      print("\nLetters remaining:", end=" ")
      display_letters(
          sorted(get_letters_remaining(incorrect_guesses, correct_guesses)))
      guess = input("\nEnter a letter: ").upper()

      if guess.isalpha():
        if len(guess) != 1:
          print("Invalid input - should be a single letter.")
          continue  
        else:
          if guess in incorrect_guesses or guess in correct_guesses:
            print("You have already used that letter.")
            continue
          if guess in word:
            print("Correct!")
            for i, letter in enumerate(word):
              if letter == guess:
                correct_guesses[i] = guess
                num_correct += 1
          else:
            incorrect_guesses.append(guess)
            num_incorrect += 1
            print("Incorrect!")
      else:
        print("That is not a letter.")

    if num_correct == len(word):
      display_gallows(num_incorrect)
      display_letters(correct_guesses)
      print("\nCongratulations! You won!")
    if len(incorrect_guesses) == 6:
      display_gallows(num_incorrect)
      display_letters(correct_guesses)
      print("\nSorry, you lost!")
    repeat = check_input.get_yes_no("Play again? (Y/N): ")


main()
