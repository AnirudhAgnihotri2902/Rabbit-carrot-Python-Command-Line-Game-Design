import random
import os

def createMap():
    path = []
    for i in range(48):
        path.append('-')
    path.append('r')
    path.append('O')
    path.append('c')
    random.shuffle(path)
    return path

def steps():
    print("Press 'a' to move left")
    print("Press 'd' to move right.")
    print("Press 'j' to jump over the hole from left to right and vice versa.")
    print("Press 'p' to pickup the carrot and put the carrot into the hole")

def currIndex(path):
    if 'r' in path:
        return path.index('r')
    elif 'R' in path:
        return path.index('R')

def stepRight(path, index):
    path[index], path[index + 1] = path[index + 1], path[index]
    return path


def stepLeft(path, index):
    path[index], path[index - 1] = path[index - 1], path[index]
    return path


def jumpLeft(path, index):
    path[index], path[index - 2] = path[index - 2], path[index]
    return path


def jumpRight(path, index):
    path[index], path[index + 2] = path[index + 2], path[index]
    return path


def pickLeftCarrot(path, index):
    path[index - 1], path[index] = 'R', '-'
    return path


def pickRightCarrot(path, index):
    path[index + 1], path[index] = 'R', '-'
    return path

def moves(path):
    while True:
        index = currIndex(path)
        command = input().lower()
        if index == 0 and path[index + 1] == 'O':
            if path[index] == 'R':
                if command == 'p':
                    return 'over'
            elif path[index] == 'r':
                if command == 'j':
                    path = jumpRight(path, index)
        elif index == len(path) - 1 and path[index - 1] == 'O':
            if path[index] == 'R':
                if command == 'p':
                    return 'over'
            elif path[index] == 'r':
                if command == 'j':
                    path = jumpLeft(path, index)
        elif index == 0:
            if command == 'd':
                path = stepRight(path, index)
        elif index == len(path) - 1:
            if command == 'a':
                path = stepLeft(path, index)
        elif path.index('O') == 0 and path[path.index('O') + 1] != '-':
            if path[index] == 'R':
                if command == 'p':
                    return 'over'
                elif command == 'd':
                    path = stepRight(path, index)
            elif path[index] == 'r':
                if command == 'd':
                    path = stepRight(path, index)
        elif path.index('O') == len(path) - 1 and path[path.index('O') - 1] != '-':
            if path[index] == 'R':
                if command == 'p':
                    return 'over'
                elif command == 'a':
                    path = stepLeft(path, index)
            elif path[index] == 'r':
                if command == 'a':
                    path = stepLeft(path, index)
        elif path[index - 1] == 'c':
            if command == 'p':
                path = pickLeftCarrot(path, index)
            elif command == 'd':
                path = stepRight(path, index)
        elif path[index + 1] == 'c':
            if command == 'p':
                path = pickRightCarrot(path, index)
            elif command == 'a':
                path = stepLeft(path, index)
        elif path[index - 1] == 'O':
            if path[index] == 'R':
                if command == 'p':
                    return 'over'
                elif command == 'd':
                    path = stepRight(path, index)
            elif path[index] == 'r':
                if command == 'j' and path[index - 2] == '-':
                    path = jumpLeft(path, index)
                elif command == 'j' and path[index - 2] == 'c':
                    path[index - 2], path[index] = 'R', '-'
                elif command == 'd':
                    path = stepRight(path, index)
        elif path[index + 1] == 'O':
            if path[index] == 'R':
                if command == 'p':
                    return 'over'
                elif command == 'a':
                    path = stepLeft(path, index)
            elif path[index] == 'r':
                if command == 'j' and path[index + 2] == '-':
                    path = jumpRight(path, index)
                elif command == 'j' and path[index + 2] == 'c':
                    path[index + 2], path[index] = 'R', '-'
                elif command == 'a':
                    path = stepLeft(path, index)
        else:
            if command == 'a':
                path = stepLeft(path, index)
            elif command == 'd':
                path = stepRight(path, index)
        os.system('cls')
        print(''.join(path))


def main():
    os.system('cls')
    print('WELCOME TO THE GAME')
    steps()
    command = input("Press 's' to start the game\n").lower()
    while True:
        path = createMap()
        os.system('cls')
        print(''.join(path))
        result = moves(path)
        if result == 'over':
            os.system('cls')
            print('GAME OVER')
            yn = input("Do you want to play again. press 'y' for yes and 'n' for no \n").lower()
            if yn == 'y':
                continue
            elif yn == 'n':
                os.system('cls')
                print('Thanks for playing our game')
                break


if __name__ == '__main__':
    main()