import random
hit_list = random.sample(range(0, 99), 3)
miss_list = random.sample(range(0, 99), 3)
ship_position_list = random.sample(range(0, 99), 2)
# Name Input for the player

player = input("Whats your name Commander?  \n")

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

user_board(hit,miss,complete)

print("\n")

# AI Board

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