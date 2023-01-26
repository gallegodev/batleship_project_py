import random
hit_list = random.sample(range(0, 99), 3)
miss_list = random.sample(range(0, 99), 3)
ship_position_list = random.sample(range(0, 99), 2)

# Name Input for the player

player = input("Whats your name Commander?  \n")


def player_shot():
    attempt = True
    while attempt == True:
        try:
            shot = input(f"Commander {player} please enter your guess:\n")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("PLease Commander enter a number between 0 and 99")
            elif shot in guesses:
                print("Commander you already picked this number, please pick another one")
            else:
                attempt = False
                break 
        except:
            print("Incorrect input, please Commander insert a number between 0 to 99\n")
        
    return shot


# Player board
def user_board(hit,miss,complete):
    print("              BATLESHIP!!!              \n")
    print(f"Commander {player} Board\n")
    print("    0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            position = " _ "
            if place in miss:
                position = " x "
            elif place in hit:
                position = " o "
            elif place in complete:
                position = " S "
        
            row = row + position
            place = place + 1
        print(x, "", row)

def check_shot(shot, hit, miss, complete, boat1):
    if shot in boat1:
        boat1.remove(shot)
        if len(boat1) > 0:
            hit.append(shot)
        else:
            complete.append(shot)
    else:
        miss.append(shot)
    return boat1, miss, hit, complete


boat1 = [45,46,47]
hit = []
miss = []
complete = []

guesses = miss + hit + complet
shot = player_shot(guesses)
boat1, hit, miss, complete = check_shot(shot, hit, miss, complete, boat1)
user_board(hit,miss,complete)

print("\n")

# AI Board
# Need to fix random numbers for AI board / they are the same as the player

def ai_board(hit,miss,complete):
    print("Evil Pirate  Board\n")
    print("    0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            position = " _ "
            if place in miss:
                position = " x "
            elif place in hit:
                position = " o "
            elif place in complete:
                position = " S "
        
            row = row + position
            place = place + 1
        print(x, "", row)

hit = hit_list
miss = miss_list
complete = ship_position_list

ai_board(hit,miss,complete)