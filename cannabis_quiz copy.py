print("----------------------------")
print("----------------------------")
print("      CANNABIS TRIVIA       ")
print("----------------------------")

#-----------------

def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input ("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)
#-----------------

def check_answer(answer, guess):
    if answer == guess:
        print ("SMOKIN!")
        return 1
    else:
        print ("You dropped the joint! :(")
        return 0
#-----------------


def display_score(correct_guesses, guesses):
    print("----------------------------")
    print("RESULTS")
    print("----------------------------")
    print("Answers: ", end = " ")
    for i in questions:
        print(questions.get(i), end = " ")
    print()

    print("Guesses: ", end = " ")
    for i in guesses:
        print((i), end = " " )
    print()
    score = (correct_guesses/len(questions)) * 100
    print("Your score is: " + str(score) + "%")

#-----------------

def play_again():
    response = input ("Do you want to try again?: (Yes or No): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False

#-----------------

questions = {
    "Is cereal milk an indica or sativa dominant hybrid? ": "C",
    "Do STIIIZY pods work with 510 thread (circular) batteries? " : "D",
    "How many milligrams are in a 10 pack of gummy edibles? " : "A",
    "How many grams are in an ounce of flower (weed)? " : "B",
}

options = [["A: Indica", "B: 50/50",  "C: Sativa", "D: idk bro I just smoke it"],
          ["A: Yes", "B: idk bro I just smoke it", "C: What's a STIIIZY pod", "D: No"],
          ["A: 100 mg", "B: 1,000 mg", "C: Idk bro I just eat them", "D: 10,000 mg"],
          ["A: Idk bro I just buy the pack", "B: 28g", "C: 30g", "D: 20g"],
]

new_game()
while play_again():
    new_game()
print("Later bro!")