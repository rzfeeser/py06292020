#!/usr/bin/python3
"""
Jeopardy Game
"""

# import a library to make an HTTP request
import requests

def main():
    # prompt for initials
    player = input("Type in your initials: ")
    rounds = input("How many rounds would you like to play? ")
    playerscore = 0 # a counter for the player's score

    # make a request to http://jservice.io/api/random
    zresp = requests.get(f"http://jservice.io/api/random?count={rounds}")

    # strip off JSON from the 200 respons
    listofquestions = zresp.json()

    # run the game by looping over the results
    for jquestion in listofquestions:
        # print(jquestion, end="\n\n")  # this would print out every dictionary
        # each time through the loop pose the question to the player
        print(f"Alex Says: {jquestion['question']}")
        playeranswer = input(f"\tType your Answer --> ({jquestion['answer']}") # capture the user's input

        # user can response by typing input be sure to normalize to lowercase
        if playeranswer.lower() == jquestion['answer'].lower():
            print(f"Alex Says: Thats right, you add {jquestion['value']} to your score")
            # alter playerscore counter, increase by the question's point value
            playerscore = playerscore + jquestion.get('value', 1000)
        else:
            print(f"Alex Says: Oh, not quite right! The answer we were looking for was {jquestion['answer']}")


    # after 10 rounds, show the player's score
    print(f"Alex Says: Okay! Let's see how you did.\nLooks like your score is {playerscore}")

    # if their score is higher than any of those in highscore.txt, ask for and then write out the player's INITIALS, and their score, to highscore.txt. Be sure to only track the top 10 most high scores!
    with open("jeopardyhighscores.txt") as jhs:
        highscorelist = jhs.readlines()
    
    # sort the data taken from the file
    highscorelist.sort()

    for score in highscorelist:
        if playerscore > int(score.rstrip("\n")):
            print("looks like a high score!")
            highscorelist.remove(score)
            highscorelist.append(str(playerscore))
            break

    with open("jeopardyhighscores.txt", "w") as jhs:
        for score in highscorelist:
            jhs.write(score.rstrip("\n")+"\n")

if __name__ == "__main__":
    main()
