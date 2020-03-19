import random

moves = ["F", "B", "U", "D", "L", "R"]
direction = ["'", "2", ""]
length = random.randrange(20, 26)

def scramble_gen():
    scramble = [0] * length
    for i in range(len(scramble)):
        scramble[i] = [0] * 2
    return scramble

def scramble_replace(ar):
    for i in range(len(ar)):
        ar[i][0] = random.choice(moves)
        ar[i][1] = random.choice(direction)
    return ar

def valid(ar):
    for i in range(1, len(ar)):
        while ar[i][0] == ar[i - 1][0]:
            ar[i][0] = random.choice(moves)
    for i in range(2, len(ar)):
        while ar[i][0] == ar[i - 2][0] or ar[i][0] == ar[i - 1][0]:
            ar[i][0] = random.choice((moves))
    return ar

def join(ar):
    final = []
    for i in range(len(ar)):
        final.append(str(ar[i][0])+ str(ar[i][1]))
    text = "  ".join(final)
    return text

def call():
    s = scramble_replace(scramble_gen())
    scramble = join(valid(s))
    return scramble