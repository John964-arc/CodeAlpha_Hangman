# CodeAlpha_Hangman
Author: John Kallappagol
Internship: CodeAlpha (Jan 10 - Feb 10)
Task: Hangman (Task 1)

## Description
This project is a fully functional console-based Hangman game developed in Python as part of the CodeAlpha Internship Program (Task 1). The objective of the game is to guess a hidden word by entering one letter at a time before exceeding the maximum number of allowed wrong attempts.
The program randomly selects a word from a predefined internal list or from an optional external words.txt file. The player must correctly identify all letters of the word within a limited number of incorrect guesses. With each wrong attempt, a stage of the Hangman ASCII diagram is displayed, visually representing the player's progress toward losing the game.
The application includes multiple difficulty levels (easy, medium, hard) which dynamically control the number of permitted wrong guesses. It also performs strict input validation to ensure that only valid single alphabetic characters are accepted and prevents repeated guesses.
Additionally, the game supports optional logging of completed matches, storing game results such as the selected word, guessed letters, and win/loss outcome in a log file for verification and record-keeping.
This project demonstrates practical usage of core Python concepts such as loops, conditionals, sets, file handling, functions, randomization, and command-line arguments, making it a clean and beginner-friendly implementation of a classic word-guessing game.

## Key Features
• Random word selection from built-in list or external file
• Difficulty modes (easy, medium, hard)
• ASCII-art based hangman visualization
• Input validation and duplicate guess prevention
• Optional game result logging
• Clean modular function-based design

