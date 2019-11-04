
locations = {
    0: "You are sitting in front of a computer",
    1: "You are standing at the end of a road before a small brick building",
    2: "You are at the top of a hill",
    3: "You are inside a building, a well house for a small stream",
    4: "You are in a valley beside a stream",
    5: "You are in the forest"
}

exits = {
    0: {"Q": 0},
    1: {"W": 2, "E": 3, "N":5, "S": 4, "Q": 0},
    2: {"N": 5, "Q": 0},
    3: {"W": 1, "Q":0},
    4: {"N": 1, "W": 2, "Q": 0},
    5: {"W": 2, "S": 1, "Q": 0}
}

alternativeWords = {
    "Quit": "Q",
    "Go North": "N",
    "North": "N",
    "Move North": "N",
    "Go East": "E",
    "East": "E",
    "Move East": "E",
    "Go South": "S",
    "South": "S",
    "Move South": "S",
    "Go West": "W",
    "West": "W",
    "Move West": "W"
}

loc = 1

while True:
    availableExits = ", ".join(exits[loc].keys())
    direction = input("Available Directions " + availableExits + ": ")
    val = alternativeWords.get(direction)

    if direction in alternativeWords:
        if val in exits[loc]:
            val = exits[loc][val]
            loc = val
        else:
            print("False")
    else:
        if direction in exits[loc]:
            loc = exits [loc][direction]
        else:
            print("You cannot go in that direction")

    if loc == 0:
        break
    print(locations[loc])