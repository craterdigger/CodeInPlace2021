# CodeInPlace2021
My final project for Code in Place 2021. It's a one-room escape room.
The user is greeted, and after entering a name, is prompted to select
a size for the dungeon. Following that, the user is placed in-game,
with instructions to locate a key using simple directional commands
of NSEW, for the cardinal compass directions.

If the user attempts to pass through a wall, a message lets them know
they are blocked. There is no need to explicitly pick up the key, which
has been randomly placed on a floor tile. The user is awarded the key
when they navigate to the tile where it resides.

With the key in hand, the user is tasked to navigate to the exit. As
with the key, the exit is randomly assigned to a tile. The user exits the
dungeon simply by navigating to the door. The door location is not 
generated until the key is located, preventing the user from being 
confused by finding an unopenable door.

Many thanks to the Code in Place 2021 team for all their hard work in
making Python accessible to so many!
