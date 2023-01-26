# Name Input for the player

player = input("Whats your name Commander?  \n")

# Player board

print("              BATLESHIP!!!              \n")
print(       f"Commander {player} Board         \n")
print("    0  1  2  3  4  5  6  7  8  9")

hit = [21,22,23]
place = 0
for x in range(10):
    row = ""
    for y in range(10):
        position = " _ "
        if place in hit:
            position = " x "
        row = row + position
        place = place + 1
    print(x, "", row)

print("\n")

# AI Board

print( "Evil Pirate Board  \n")
print("   0   1   2   3   4   5   6   7   8   9")
for x in range(10):
    print(x," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ ")