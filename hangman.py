import random
import argparse
import datetime
import os
import sys

# Default in-code word list (5+ words as required by internship)
DEFAULT_WORDS = [
    "python", "hangman", "developer", "keyboard", "function",
    "variable", "boolean", "iterate", "string", "module"
]

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===""",
]

DIFFICULTY_SETTINGS = {
    "easy": 6,    # generous (shows all stages)
    "medium": 5,
    "hard": 4
}

def load_words_from_file(path):
    """Load words from a text file, one word per line. Returns cleaned lowercase list."""
    words = []
    try:
        with open(path, "r", encoding="utf8") as f:
            for line in f:
                w = line.strip().lower()
                if w and w.isalpha():
                    words.append(w)
    except FileNotFoundError:
        print(f"[!] Word file not found: {path} — using built-in list.")
    except Exception as e:
        print(f"[!] Error reading word file {path}: {e} — using built-in list.")
    return words

def choose_word(words):
    """Choose a random word from list."""
    return random.choice(words)

def display_state(word, guessed, wrong_guesses, max_wrong):
    """Print the current game state to the console."""
    wrong_count = len(wrong_guesses)
    # clamp for ascii art index
    art_index = min(wrong_count, len(HANGMAN_PICS) - 1)
    print(HANGMAN_PICS[art_index])
    print("\nWord: ", " ".join([c if c in guessed else "_" for c in word]))
    print(f"Wrong guesses ({wrong_count}/{max_wrong}):", " ".join(sorted(wrong_guesses)))
    print()

def get_guess(already_tried):
    """Get a single-letter guess from the player with validation."""
    while True:
        g = input("Enter one letter: ").strip().lower()
        if g == "":
            print("Please enter a letter.")
            continue
        if len(g) != 1 or not g.isalpha():
            print("Enter exactly one alphabet letter (a-z).")
            continue
        if g in already_tried:
            print("You already tried that letter.")
            continue
        return g

def save_game_log(repo_dir, name, word, guessed, wrong_guesses, result):
    """Save a small text file describing the run. Useful for screenshots evidence."""
    os.makedirs(repo_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(repo_dir, f"hangman_log_{timestamp}.txt")
    try:
        with open(filename, "w", encoding="utf8") as f:
            f.write(f"Player: {name}\n")
            f.write(f"Word: {word}\n")
            f.write(f"Guessed: {', '.join(sorted(guessed))}\n")
            f.write(f"WrongGuesses: {', '.join(sorted(wrong_guesses))}\n")
            f.write(f"Result: {result}\n")
            f.write(f"Time: {timestamp}\n")
        print(f"[+] Saved run log to: {filename}")
    except Exception as e:
        print(f"[!] Could not save log: {e}")

def play_game(words, max_wrong, save_logs=False, player_name="Player"):
    word = choose_word(words)
    guessed = set()
    wrong_guesses = set()

    while True:
        display_state(word, guessed, wrong_guesses, max_wrong)

        # check win
        if all(ch in guessed for ch in word):
            print("🎉 You won! The word was:", word)
            if save_logs:
                save_game_log("logs", player_name, word, guessed, wrong_guesses, "WIN")
            break

        # check lose
        if len(wrong_guesses) >= max_wrong:
            print("☠️ You lost. The word was:", word)
            if save_logs:
                save_game_log("logs", player_name, word, guessed, wrong_guesses, "LOSE")
            break

        guess = get_guess(guessed.union(wrong_guesses))
        if guess in word:
            guessed.add(guess)
            print("Good guess.")
        else:
            wrong_guesses.add(guess)
            print("Wrong guess.")

def parse_args():
    p = argparse.ArgumentParser(description="Hangman game for CodeAlpha internship.")
    p.add_argument("--file", "-f", help="Optional path to words file (one word per line).")
    p.add_argument("--difficulty", "-d", choices=DIFFICULTY_SETTINGS.keys(),
                   default="medium", help="Difficulty level (easy/medium/hard).")
    p.add_argument("--save-logs", action="store_true", help="Save a small log of each run to logs/")
    p.add_argument("--name", "-n", default="Player", help="Your name for the run log.")
    return p.parse_args()

def main():
    args = parse_args()
    words = DEFAULT_WORDS.copy()
    if args.file:
        from_file = load_words_from_file(args.file)
        if from_file:
            words = from_file
    max_wrong = DIFFICULTY_SETTINGS.get(args.difficulty, 5)
    print(f"Starting Hangman — difficulty={args.difficulty} (max wrong={max_wrong}) — words={len(words)}")
    play_game(words, max_wrong, save_logs=args.save_logs, player_name=args.name)

if __name__ == "__main__":
    main()