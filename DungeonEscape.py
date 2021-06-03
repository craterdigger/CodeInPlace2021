# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random

DEFAULT_NAME = "Wanderer"

# Dungeon dimensions:
SMALL_MIN = 5
SMALL_MAX = 10
MED_MIN = 10
MED_MAX = 15
LRG_MIN = 15
LRG_MAX = 20
START_POINT_X = 1
START_POINT_Y = 1


def game_intro():
    # Scenario intro:
    name = input("Enter your name: ")
    if name == "":
        name = DEFAULT_NAME
    print("Hi, " + name + "! Welcome to the Lost Dungeon!")
    return name


def boundary_set(room_length, room_width):
    # Set the size of the room.
    params = False

    room_size = ""
    while room_size not in ("S", "M", "L"):
        room_size = input("What size do you want your room (S, M, L)? ")

    while not params:
        if room_size == "S":
            room_width = random.randint(SMALL_MIN, SMALL_MAX)
            room_length = random.randint(SMALL_MIN, SMALL_MAX)
            params = True
        elif room_size == "M":
            room_width = random.randint(MED_MIN, MED_MAX)
            room_length = random.randint(MED_MIN, MED_MAX)
            params = True
        else:
            room_width = random.randint(LRG_MIN, LRG_MAX)
            room_length = random.randint(LRG_MIN, LRG_MAX)
            params = True

    # X is length left to right, Y is width, bottom to top.
    print('')
    print("You are in a room " + str(room_length) + " long by " + str(room_width) + " wide.")
    print("The key has been left on a random square.")
    print("Your goal is to find the key and escape ")
    print("the room. Locate the key by moving over ")
    print("it, then proceed to the exit.")

    return room_length, room_width


def key_place(room_length, room_width):
    # Place the key:
    key_loc_x = random.randint(2, room_length)
    key_loc_y = random.randint(2, room_width)
    return key_loc_x, key_loc_y


def exit_place(room_length, room_width):
    # Place the exit:
    # Input values diagnostic:
    exit_loc_x = random.randint(1, room_length)
    exit_loc_y = random.randint(1, room_width)
    # print("Exit loc: " + str(exit_loc_x) + " " + str(exit_loc_y))
    return exit_loc_x, exit_loc_y


def key_locate(player_x, player_y, key_loc_x, key_loc_y, room_length, room_width):
    while player_x != key_loc_x or player_y != key_loc_y:
        print("You are now standing at position: " + str(player_x) + "E, " + str(player_y) + "N.")
        player_move = input("Enter your move (N,S,E,W): ")
        if player_move == "N":
            if player_y + 1 == room_width + 1:
                print("There is a wall blocking your way.")
            else:
                player_y += 1
                print("You take one step North.")
        elif player_move == "S":
            if player_y - 1 == 0:
                print("There is a wall blocking your way.")
            else:
                player_y -= 1
                print("You take one step South.")
        elif player_move == "E":
            if player_x + 1 == room_length + 1:
                print("There is a wall blocking your way.")
            else:
                player_x += 1
                print("You take one step East.")
        elif player_move == "W":
            if player_x - 1 == 0:
                print("There is a wall blocking your way.")
            else:
                player_x -= 1
                print("You take one step West.")
    print("You found the key! Now make your way to the exit.")
    return player_x, player_y


def dungeon_escape(player_x, player_y, exit_loc_x, exit_loc_y, room_length, room_width):
    while player_x != exit_loc_x or player_y != exit_loc_y:
        print("You are now standing at position: " + str(player_x) + ", " + str(player_y) + ".")
        player_move = input("Enter your move (N,S,E,W): ")
        if player_move == "N":
            if player_y + 1 == room_width + 1:
                print("There is a wall blocking your way.")
            else:
                player_y += 1
                print("You take one step North.")
        elif player_move == "S":
            if player_y - 1 == 0:
                print("There is a wall blocking your way.")
            else:
                player_y -= 1
                print("You take one step South.")
        elif player_move == "E":
            if player_x + 1 == room_length + 1:
                print("There is a wall blocking your way.")
            else:
                player_x += 1
                print("You take one step East.")
        elif player_move == "W":
            if player_x - 1 == 0:
                print("There is a wall blocking your way.")
            else:
                player_x -= 1
                print("You take one step West.")


def main():
    # Initialize room dimensions...
    room_length = 0
    room_width = 0
    # Player starts at (1, 1)
    player_x = 1
    player_y = 1

    # Greet player, then set room boundaries and key location...
    name = game_intro()
    room_length, room_width = boundary_set(room_length, room_width)
    key_loc_x, key_loc_y = key_place(room_length, room_width)

    # Diagnostic feedback
    # print("Key loc: " + str(key_loc_x) + ", " + str(key_loc_y))
    print("")
    # First find the key...
    player_x, player_y = key_locate(player_x, player_y, key_loc_x, key_loc_y, room_length, room_width)
    print("")
    # Now create the exit...
    exit_loc_x, exit_loc_y = exit_place(room_length, room_width)
    # Then find the exit...
    dungeon_escape(player_x, player_y, exit_loc_x, exit_loc_y, room_length, room_width)
    print("You found the exit! You are now Sir " + name + " of the Lost Dungeon!")


if __name__ == '__main__':
    main()
