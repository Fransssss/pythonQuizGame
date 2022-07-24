# Quiz game
# -----------------
def new_game():
    list_user_guess = []
    score_correct_guest = 0
    question_num = 1

    for key in questions:
        print("\n--------------------")
        print(key)                                     # print out the question  # key is the question
        for i in options[1 - question_num]:
            print(i)                                   # print options after each question
        user_guess = input("choice: ").upper()         # make user input as upper case
        list_user_guess.append(user_guess)             # list all user choice/answer
        score_correct_guest += check_answer(questions.get(key),
                                            user_guess)  # pass the correct answer and user input to check answer, question.get() get the associated value for each question
        question_num += 1                               # to go the next option

    display_score(score_correct_guest, list_user_guess) # display score after the game


# -----------------
def check_answer(answer, user_guess):
    if answer == user_guess:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0


# -----------------

def display_score(correct_guess, list_user_guess):
    print("\n--------------------")
    print("Result")
    print("--------------------")
    print("Correct answer: ", end=" ")                # end= " " - display all correct answer in one line (no new line)
    for key in questions:                             # display correct answer
        print(questions.get(key), end=" ")            # end=" " -display all guesses in one line (no new line)
    print("\nYour guesses: ", end=" ")                # display user's guesses
    for i in list_user_guess:
        print(i, end=" ")

    score = int((correct_guess / len(questions)) * 100)
    print("\nTotal score: " + str(score) + "%")


# -----------------
def play_again():
    response = input("\nWould you like to play again (y/n): ").upper()       # make user input to upper case
    if response == "Y":
        return True
    elif response == "N":
        return False
    else:
        print("\n[ Invalid input ]")


# -----------------
questions = {"\n1. Color of the sun: ": "A",
             "\n2. Color of rainbow: ": "B",
             "\n3. Color of leave: ": "C"}  # dictionary

options = [["A. Red", "B. Yellow", "C. Black"],
           ["A. Red,Yellow,Green", "B. Blue, Dark, Green", "C. Yellow Pink, Gray"],
           ["A. Black", "B, Gold", "C. Green"]]  # list of lists

new_game()

while  play_again():
    new_game()

print("\n== Good Game ==")
