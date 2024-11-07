import sys, random, time, bext

WIDTH, HEIGHT = bext.size()
WIDTH -= 1

NUMBER_OF_NAMES = int(input("number of bouncing texts:\n"))  # (!) Try changing this to 1 or 100.
NAME = input("text:\n")
COLORS = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
TRAIL=(True if input("has trail(True of False):")=="True" else False)

UP_RIGHT   = "ur"
UP_LEFT    = "ul"
DOWN_RIGHT = "dr"
DOWN_LEFT  = "dl"
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

COLOR = "color"
X = "x"
Y = "y"
DIR = "direction"


def main():
    bext.clear()

    names = []
    for i in range(NUMBER_OF_NAMES):
        names.append({COLOR: random.choice(COLORS),
                    X: random.randint(1, WIDTH - 4),
                    Y: random.randint(1, HEIGHT - 4),
                    DIR: random.choice(DIRECTIONS)})
        if names[-1][X] % 2 == 1:
            names[-1][X] -= 1

    cornerBounces = 0
    while True:
        if not TRAIL:bext.clear()
        for name in names:
            bext.goto(name[X], name[Y])
            print("   ", end="")
            
            originalDirection = name[DIR]
            
            if name[X] == 0 and name[Y] == 0:
                name[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif name[X] == 0 and name[Y] == HEIGHT - 1:
                name[DIR] = UP_RIGHT
                cornerBounces += 1
            elif name[X] == WIDTH - 3 and name[Y] == 0:
                name[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif name[X] == WIDTH - 3 and name[Y] == HEIGHT - 1:
                name[DIR] = UP_LEFT
                cornerBounces += 1
            
            elif name[X] == 0 and name[DIR] == UP_LEFT:
                name[DIR] = UP_RIGHT
            elif name[X] == 0 and name[DIR] == DOWN_LEFT:
                name[DIR] = DOWN_RIGHT
            
            elif name[X] == WIDTH - 3 and name[DIR] == UP_RIGHT:
                name[DIR] = UP_LEFT
            elif name[X] == WIDTH - 3 and name[DIR] == DOWN_RIGHT:
                name[DIR] = DOWN_LEFT
            
            elif name[Y] == 0 and name[DIR] == UP_LEFT:
                name[DIR] = DOWN_LEFT
            elif name[Y] == 0 and name[DIR] == UP_RIGHT:
                name[DIR] = DOWN_RIGHT
            
            
            elif name[Y] == HEIGHT - 1 and name[DIR] == DOWN_LEFT:
                name[DIR] = UP_LEFT
            elif name[Y] == HEIGHT - 1 and name[DIR] == DOWN_RIGHT:
                name[DIR] = UP_RIGHT
            
            if name[DIR] != originalDirection:
                name[COLOR] = random.choice(COLORS)


            if name[DIR] == UP_RIGHT:
                name[X] += 2
                name[Y] -= 1
            elif name[DIR] == UP_LEFT:
                name[X] -= 2
                name[Y] -= 1
            elif name[DIR] == DOWN_RIGHT:
                name[X] += 2
                name[Y] += 1
            elif name[DIR] == DOWN_LEFT:
                name[X] -= 2
                name[Y] += 1
        
        bext.goto(5, 0)
        bext.fg("white")
        print(f"corner bounces:{cornerBounces}", end="")
        
        for name in names:
            # Draw the names at their new location:
            bext.goto(name[X], name[Y])
            bext.fg(name[COLOR])
            print(NAME, end="")
            
        bext.goto(0, 0)
        sys.stdout.flush()
        time.sleep(0.1)


#start
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        bext.clear()
        print()
        try:
            import art
            art.tprint("Bouncing Text by twels")
        except:
            print("Bouncing text by twels22")
        sys.exit()