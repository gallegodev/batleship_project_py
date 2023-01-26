import random
hit_list = random.sample(range(0, 99), 3)
miss_list = random.sample(range(0, 99), 3)
ship_position_list = random.sample(range(0, 99), 2)

# Name Input for the player

player = input("Whats your name Commander?  \n")


def player_shot():
    attempt = True
    while attempt == True:
        shot = input(f"Commander {player} please enter your guess:\n")
        shot = int(shot)
        if shot < 0 or shot > 99:
            print("PLease Commander enter a number between 0 and 99")
        else:
            attempt = False
            break 

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

hit = hit_list
miss = miss_list
complete = ship_position_list

shot = player_shot()
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