import random
hit_list = random.sample(range(0, 99), 3)
miss_list = random.sample(range(0, 99), 3)
# Name Input for the player

player = input("Whats your name Commander?  \n")

# Player board

print("              BATLESHIP!!!              \n")
print(       f"Commander {player} Board         \n")
print("    0  1  2  3  4  5  6  7  8  9")

hit = hit_list
miss = miss_list
place = 0

for x in range(10):
    row = ""
    for y in range(10):
        position = " _ "
        if place in miss:
            position = " X "
        elif place in hit:
            position = " O "
        
        row = row + position
        place = place + 1
    print(x, "", row)

print("\n")

# AI Board

print( "Evil Pirate Board  \n")
print("   0   1   2   3   4   5   6   7   8   9")
for x in range(10):
    print(x," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ ")