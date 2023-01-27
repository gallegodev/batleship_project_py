from random import randrange


def check_ok(boat, num_used):
    """
    This function checks if number if boat is valid
    """

    for i in range(len(boat)):
        num = boat[i]
        if num in num_used:
            boat = [-1]
            break
        if num < 0 or num > 99:
            boat = [-1]
            break
        elif num % 9 == 0 and i < len(boat) - 1:
            if boat[i+1] % 10 == 0:
                boat = [-1]
                break

    return boat


def check_boat(b, start, direction, num_used):
    """
    This Function generates random number for the boat positions 
    """

    boat = []
    if direction == 1:
        for i in range(b):
            boat.append(start - i*10)
            boat = check_ok(boat, num_used)
    elif direction == 2:
        for i in range(b):
            boat.append(start + i)
            boat = check_ok(boat, num_used)
    elif direction == 3:
        for i in range(b):
            boat.append(start + i*10)
            boat = check_ok(boat, num_used)
    elif direction == 4:
        for i in range(b):
            boat.append(start - i)
            boat = check_ok(boat, num_used)
    return boat


def create_boats():
    num_used = []
    ships = []    
    boats = [5, 4, 3, 3, 2, 2]
    for b in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1, 4)
            print(b, boat_start, boat_direction)
            boat = check_boat(b, boat_start, boat_direction, num_used)
        ships.append(boat)
        num_used = num_used + boat
        print(ships)

    return ships, num_used

"""
Testing if code is generating random positions for the boats properly
Dont forget to ERASE************
"""


def user_board(num_used):
    print("Please destroy the ships of the evil Pirate")
    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            position = " _ "
            if place in num_used:
                position = " h "
            row = row + position
            place = place + 1
        print(x, " ", row)


boats, num_used = create_boats()
user_board(num_used)