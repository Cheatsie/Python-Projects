# https://www.soccervista.com/soccer_leagues_ordered_by_number_of_draws.php
#  EVENTUALLY INPUT SOCCER DRAW ACTION AS CSV FILE.
counter = 0

# ALWAYS ENTER SMALLER NUMBER FIRST
def printValues(x, y, listCounter):
    betRatios = [2.15, 3.75]  # RATIO OF THE BETS

    betSolution1 = -(x + y) + (x * betRatios[0])  # X IS SMALL RATIO
    betSolution4 = -(x + y) + (y * betRatios[1])  # Y IS BIG RATIO
    betSolution3 = -(x + y) + (y * betRatios[0])  # Y IS SMALL RATIO
    betSolution2 = -(x + y) + (x * betRatios[1])  # X IS BIG RATIO

    if betSolution1 > 0 and betSolution4 > 0:
        print(str(x) + "$" + " with " + str(betRatios[0]) + "$ and " + str(y) + "$ with " + str(betRatios[1]) + "$ "
                                                                                                                "yields a positive result.")
        sumSolution1AND4 = betSolution1 + betSolution4
        if sumSolution1AND4 >= 0:
            print("You will make: $" + str(round(betSolution1, 2)) + " profit if X is wins bet.")
            print("You will make: $" + str(round(betSolution4, 2)) + " profit if Y is wins bet.")
            print("THIS USED SOLUTION 1")
            print("")

    if betSolution2 > 0 and betSolution3 > 0:
        sumSolution2AND3 = betSolution2 + betSolution3
        if sumSolution2AND3 >= 0:
            print(str(x) + "$ with " + str(betRatios[1]) + "$ and " + str(y) + "$ with " + str(betRatios[0]) + "$ "
                                                                                                               "yields a positive result.")
            print("You will make: " + str(round(betSolution2, 2)) + " profit if Y is wins bet.")
            print("You will make: " + str(round(betSolution3, 2)) + " profit if X is wins bet.")
            print("THIS USED SOLUTION 2")
            print("")

    listCounter += 1
    x += 1  # INCREASE X

    while listCounter < 15:  # ESSENTIAL THAT THIS COUNTER REMAINS HIGH
        return printValues(x, y, listCounter)  # RUN THROUGH X ITERATIONS

# AMOUNT I WOULD SPEND PER BET
dollars = 8
for i in range(dollars):
    printValues(i, i, counter) # MINIMUM OF WHAT'S ADDED TO X

