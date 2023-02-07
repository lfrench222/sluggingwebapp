#Number of Bases
bats = int(input("Number of AB's: ")) 
singles = int(input("Number of Singles: "))
dub = int(input("Number of Doubles: ")) * 2
trip = int(input("Number of Triples: ")) * 3
hr = int(input("Number of Home Runs: ")) * 4

#Math Equation
totalbases = (singles + dub + trip + hr)
SLG = (totalbases) / bats
Percent = SLG 

#outputs

print("SLG % : {0}")
