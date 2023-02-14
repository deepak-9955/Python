import random  # import random library

import json  # import json library

''' to create json file
    try block is for not to show error on 
    second or third so on time run this game
    and initialize the score with zero at first time
'''
user = 0
computer = 0
firstTime = 1


def showScore():
    with open('sample.json', 'r') as openfile:
        json_score = json.load(openfile)

        print("Highest Score")
        global user, computer
        user = json_score['user']
        computer = json_score['computer']

        print("User : ", json_score['user'])
        print("Computer : ", json_score['computer'])
        return json_score['firsttime']


if firstTime:
    print()
else:
    firstTime = showScore()

if firstTime:
    try:
        dictionary = {

            "user": 0,
            "computer": 0,
            "firsttime": 1
        }

        # Serializing json
        json_object = json.dumps(dictionary, indent=3)

        # Writing to sample.json
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
    finally:
        print()


# This function for showing

print('Winning rules of the game ROCK PAPER SCISSORS are :\n' + "Rock Beats Scissors -> Rock wins \n" +
      "Scissors Beats Paper -> Scissor wins \n" + "Paper Beats Rock -> Paper wins \n")
r = True

result = ""

while r:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    choice = int(input("Enter your choice :"))
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please '))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print('User choice is \n', choice_name)
    print('Now its Computers Turn....')

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'rocK'
    elif comp_choice == 2:
        comp_choice_name = 'papeR'
    else:
        comp_choice_name = 'scissorR'

    print("Computer choice is:- ", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)
    if choice == comp_choice:
        print('Its a Draw', end="")
        result = "DRAW"

    if (choice == 1 and comp_choice == 2):
        print('paper wins =>', end="")
        result = 'papeR'
    elif (choice == 2 and comp_choice == 1):
        print('paper wins =>', end="")
        result = 'Paper'

    if (choice == 1 and comp_choice == 3):
        print('Rock wins =>\n', end="")
        result = 'Rock'
    elif (choice == 3 and comp_choice == 1):
        print('Rock wins =>\n', end="")
        result = 'rocK'

    if (choice == 2 and comp_choice == 3):
        print('Scissors wins =>', end="")
        result = 'scissoR'
    elif (choice == 3 and comp_choice == 2):
        print('Scissors wins =>', end="")
        result = 'Scissors'

    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == choice_name:
        user += 1
        print("<== User wins ==>")
    else:
        computer += 1
        print("<== Computer wins ==>")
    print("Do you want to play again? (Y/N)")

    ans = input()
    if ans == 'n' or ans == 'N':
        r = False

dictionary = {
    "user": user,
    "computer": computer,
    "firsttime": 0
}
json_object = json.dumps(dictionary, indent=2)
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)


# updateScore(dictionary)
showScore()
print("Thanks for playing")
