import random
hit_list = random.sample(range(0, 99), 3)
miss_list = random.sample(range(0, 99), 3)
ship_position_list = random.sample(range(0, 99), 2)

# Name Input for the player

player = input("Whats your name Commander?  \n")


def player_shot(guesses):
    attempt = "n"
    while attempt == "n":
        try:
            shot = input(f"Commander {player} please enter your guess:\n")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("PLease Commander enter a number between 0 and 99")
            elif shot in guesses:
                print("Commander you already picked this number, try anotehr")
            else:
                attempt = "y"
                break 
        except:
            print("Incorrect input, please Commander insert only numbers")
        
    return shot


# Player board
def user_board(hit, miss, complete):
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


boat1 = [44, 45, 46]
hit = []
miss = []
complete = []

for i in range(10):
    guesses = miss + hit + complete
    shot = player_shot(guesses)
    boat1, hit, miss, complete = check_shot(shot, hit, miss, complete, boat1)
    user_board(hit, miss, complete)

print("\n")

