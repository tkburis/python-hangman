import os


def validate_guess(n, guessed):  # returns True if guess is lowercase, 1 character long, and not guessed before
    return True if n.islower() and len(n) == 1 and n not in guessed else False


START_GUESSES = 10
remaining_guesses = START_GUESSES

while True:
    target_word = input("Enter target word: ")

    if not target_word.islower() or not target_word.isalpha():
        print("Make sure this is entirely lowercase and part of the alphabet")
        continue
    else:
        target_word = list(target_word)
        break

current_worked = ["_" if i != " " else " " for i in target_word]
already_guessed = []

# print(current_worked)
os.system('cls' if os.name == 'nt' else 'clear')

while "_" in current_worked and remaining_guesses > 0:
    current_worked_with_spaces = []
    for i, v in enumerate(current_worked):
        current_worked_with_spaces.append(v) if i == 0 else current_worked_with_spaces.append(" " + v)
    print(''.join(current_worked_with_spaces) + " " +
          str(len([i for i in current_worked if i == "_"])) + " letters left to guess")

    current_guess = input("Enter guess: ")

    if validate_guess(current_guess, already_guessed):
        already_guessed.append(current_guess)
        if current_guess in target_word:
            while current_guess in target_word:
                current_index = target_word.index(current_guess)
                target_word[current_index] = "*"
                current_worked[current_index] = current_guess

        else:
            remaining_guesses -= 1
            print("You have " + str(remaining_guesses) + " wrong guesses left")
    else:
        print("Invalid input")

if remaining_guesses == 0:
    print("You ran out of guesses")
else:
    print("Correct! The word was " + ''.join(current_worked))
