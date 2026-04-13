import random
import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
    
#create wordlists
with open("possible_words.txt", "r") as f:
    possible = f.readlines()
    possible = [line.strip().upper() for line in possible]
with open("allowed_words.txt", "r") as f:
    allowed = f.readlines()
    allowed = [line.strip().upper() for line in allowed]

#choose word
def create_answer():
    answer = random.choice(possible).upper()
    return answer

#check letters
def check_letters(guess, guesses, correct_answers, answer):
    check = ""
    if answer == guess:
        check = answer
        correct_answers += 1
    elif answer in guesses:
        check = "     "
    else:
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                check += guess[i]
            elif guess[i] in answer:
                check += guess[i].lower()
            else: check += "-"
    check += "\t"
    return check,correct_answers

#wordle
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def play_octordle():
    clear_terminal()
    print("\n\n--------------------\nLet's play octordle!\n--------------------\n")
    again = "y"
    while again != "n":
        #answers
        answer1 = create_answer()
        answer2 = create_answer()
        answer3 = create_answer()
        answer4 = create_answer()
        answer5 = create_answer()
        answer6 = create_answer()
        answer7 = create_answer()
        answer8 = create_answer()
        answer_list = [answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8]
        correct_answers = 0
        guesses = []
        guess = ""
        checks = ""
        for attempt in range(14):
            if correct_answers < 8:
                #guess
                guess = input("ur word: ").upper()
                while len(guess) != 5 or guess not in allowed:
                    guess = input("enter valid 5 letter word :").upper()
                guesses.append(guess)
                check1,correct_answers = check_letters(guess,guesses,correct_answers,answer1)
                check2,correct_answers = check_letters(guess,guesses,correct_answers,answer2)
                check3,correct_answers = check_letters(guess,guesses,correct_answers,answer3)
                check4,correct_answers = check_letters(guess,guesses,correct_answers,answer4)
                check5,correct_answers = check_letters(guess,guesses,correct_answers,answer5)
                check6,correct_answers = check_letters(guess,guesses,correct_answers,answer6)
                check7,correct_answers = check_letters(guess,guesses,correct_answers,answer7)
                check8,correct_answers = check_letters(guess,guesses,correct_answers,answer8)
                checks += check1+check2+check3+check4+check5+check6+check7+check8+"\n"
                print(checks) 
                unused = ""
                for letter in alphabet:
                    if all(letter not in word for word in guesses):
                        unused += letter 
                print(f"Unchecked letters: {unused}")
            else: break
        if correct_answers < 8:
            print(f"\nYou lost!\nThe correct words were {answer_list}\n")
        else: 
            print(f"You won in {attempt}/14 guesses")
        again = input("Want to play again? (y/n) ")
        clear_terminal()
        if again != "n":
            print("\n\n-----------------\nLet's play again!\n-----------------\n")
    

play_octordle()
