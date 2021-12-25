# -------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "Who is the class incharge of b7 batch students?: ": "A",
 "which is the easiest language to learn ?": "B",
 "Python is tributed to which comedy group?: ": "C",
 "When did INDIA got independence?: ": "A",
 "Which batch is best in KCG COLLEGE OF TECHNOLOGY?:":"B"
}

options = [["A. Dr.Poorani", "B. Dr.Nalini", "C. Dr.Lakshmipathy", "D. Dr.Lakshmi"],
          ["A. C", "B. Python", "C. C++", "D. Java"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. 1947","B. 1950", "C. 1945", "D. 1999"],
           ["A. B1","B. B7","C. B2","D. B10"]]

new_game()

while play_again():
    new_game()

print("Byeeeeee!")

# -------------------------
