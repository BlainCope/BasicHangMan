import random
import words
import ASCIIART


def preletterguess(string_list, chosen_word):
    """This function prints out the number of letters in a word"""
    for char in range(len(chosen_word)):
        string_list += '_'
    return string_list


def checkletter(guess, display, chosen_word):
    """This function checks if a letter is within the chosen_word, if it is it adds it to the list"""
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    return display


def listtoString(display_underscore):
    """This function converts the list to a string"""
    newString = ''
    for char in display_underscore:
        newString += char + ' '
    return newString

def randomWord():
    """This function generates a random word from the list"""
    return random.choice(words.word_list)


# Step 1
# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
def main():
    chosen_word = randomWord()
    display = []
    game_end = False
    max_lives = 5
    draw_art = 6

    display_underscore = preletterguess(display, chosen_word)
    ASCIIART.printASCII(draw_art)
    print(f"Letters in word: {listtoString(display_underscore)}")
    while not game_end:
        guess = input("Guess a letter: ").lower()
        if guess in display_underscore:
            ASCIIART.printASCII(draw_art)
            print(f"You've already guessed {guess}, try again!")
            print(f"Letters in word: {listtoString(display_underscore)}")
        elif guess in chosen_word:
            display_underscore = checkletter(guess, display_underscore, chosen_word)
            ASCIIART.printASCII(draw_art)
            print(f"Letters in word: {listtoString(display_underscore)}")
        else:
            max_lives -= 1
            draw_art -= 1
            ASCIIART.printASCII(draw_art)
            print(f"The letter {guess} is not in the word, please try again")
            print(f"Letters in word: {listtoString(display_underscore)}")
        if '_' not in display_underscore:
            game_end = True
            print("Congrats you win!")
        elif max_lives == 0:
            game_end = True
            ASCIIART.printASCII(0)
            print(f"The word was {chosen_word}")
            print("You lose!")


if __name__ == "__main__":
    main()
