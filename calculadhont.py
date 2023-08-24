#
# CalculaD'Hont
# by EuroNutella
# last updated: 24/08/2023
#
from colorama import init, Fore, Style

init()

# Colors and variables
YELLOW = Fore.YELLOW + Style.BRIGHT
GREEN = Fore.GREEN + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT
BLUE = Fore.BLUE + Style.BRIGHT
RESET = Style.RESET_ALL

parties = []
partVals = []
v = 0 # This will help us find the biggest value later
p = 0 # This will tell us in which position the biggest value is
partSpot = [] # This is where we'll store each party's number of seats

# Defining total number of parties
max_parties = input('How many parties do you want to simulate? ')
max_parties = int(max_parties)

# Adding parties and their votes
for i in range(max_parties):
    party = input(YELLOW +'Insert name of a party: '+ RESET)
    parties.append(party)
    partVal = float(input(BLUE +'Electoral result: '+ RESET))
    partVals.append(partVal)
    partSpot.append(0)

# Defining maximum spots to be assigned
max_spots = int(input('How many spots need to be assigned? '))

# Calculating the spots via the D'Hont formula
for i in range(max_spots):
    v = 0
    for j in range(max_parties):
        if partVals[j] > v:
            v = partVals[j]
            p = j
    partSpot[p] = partSpot[p] + 1
    partVals[p] = partVals[p] / 2

# Printing out results
for i in range(max_parties):
    if partSpot[i] == 0:
        print(RED, parties[i], ": ", partSpot[i], RESET, sep="")
    else:
        print(GREEN, parties[i], ": ", partSpot[i], RESET, sep="")