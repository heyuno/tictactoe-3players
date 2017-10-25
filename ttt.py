import random
from enum import Enum


class Player(Enum):
    FIRST = 'O'
    SECOND = 'X'
    THIRD = '-'


def game_intro():
    print("\n\n\t\t\t---------------------------------------------")
    print("\t\t\t    ~Welcome to 3 player Tic Tac Toe Game~   ")
    print("\t\t\t---------------------------------------------")
    print("\t\t\t      Each Player has a different symbol     ")
    print("\t\t\t             (X) or (-) or (O)               ")
    print("\t\t\t  Place your symbol in any line of 3 to win\n")


def game_init(grid_values, grid_size, current_player):
    """
    Init the game
    Params:
        grid_values: list
            The grid's value
        grid_size: int
            The grid size
        current_player: Player
            The current player
    Return:
        None
    """
    # Show the grid
    show_game(grid_values, grid_size)
    print(f"\n\t\t\t '{current_player.value}' has been chosen to go first")


def show_game(grid_values, grid_size):
    """
    Show the grid to console
    Params:
        grid_values: list
            The grid's value
        grid_size: int
            The grid size
    Return:
        None
    """
    print("\n")
    print('     ', end='')
    for i in range(grid_size):
        # Print the top row indicate the horizontal index
        print('  ' + str(i + 1) + '   ', end='')
    for i in range(grid_size):
        print()
        print('    ' + '------' * grid_size + '-')
        print(' ' + str(i + 1) + (' |' if i > 8 else '  |'), end='')
        for j in range(grid_size):
            print('  ' + str(grid_values[i][j]) + '  |', end='')

    print()
    # The bottom line
    print('    ' + '------' * grid_size + '-')


def chose_first_player():
    """
    Randomly chose the player who will make first step
    """
    index = random.randrange(len(list(Player)))
    return list(Player)[index]


def next_player(current_player):
    """
    Chose next player
    Params:
        current_player: Player
            The current player
    Return:
        next_player: Player
            The next player who will play next step
    """
    if current_player == Player.FIRST:
        return Player.SECOND
    elif current_player == Player.SECOND:
        return Player.THIRD
    return Player.FIRST


def play(current_player, grid_values, grid_size):
    """
    Game playing
    Params:
        grid_values: list
            The grid's value
        grid_size: int
            The grid size
        current_player: Player
            The current player
    Return:
        None
    """
    free_squares = grid_size * grid_size
    while True:
        print(f"\n\t\t\tYour turn: '{current_player.value}'")
        while True:
            try:
                row = input("Select row to place    : " +
                            current_player.value + " : ")
                col = input("Select column to place : " +
                            current_player.value + " : ")
                slot_x = (int)(row) - 1
                slot_y = (int)(col) - 1
                if slot_x in range(0, grid_size) and slot_y in range(0, grid_size):
                    if slot_free(grid_values, slot_x, slot_y):
                        grid_values[slot_x][slot_y] = current_player.value
                        break
                    else:
                        print("\n**Someone already took that slot**\n")
                else:
                    print(
                        f'\n**PLease only enter between (1 - {grid_size}) as indicated on grid**\n')

            except ValueError:
                print("\n**ERROR** Please enter INTEGER!!**\n")

        show_game(grid_values, grid_size)
        check_for_winner(grid_values, grid_size)

        free_squares -= 1
        if free_squares == 0:
            print("\n**Game Over** No Winners and No space left\n")
            break

        if check_for_winner(grid_values, grid_size):
            print("\n\t\t\t**Winner Winner Winner**!!\n")
            print("\n\t\t\tCongratulation '" +
                  current_player.value + "' WON!!!")
            break
        # this is for changing players turn by turn
        current_player = next_player(current_player)


def check_straight(grid_values, grid_size):
    """
    Check if there are 3 adjacent same 'symbol' s on same row/column
    Params:
        grid_values: list
            The grid's value
        grid_size: int
            The grid size
        current_player: Player
            The current player
    Return:
        True: If there are 3 adjacent same 'symbol' s on same row/column
        None: Otherwise
    """
    # 'O', 'X', '-
    symbols = [p.value for p in Player]
    for x in range(0, grid_size):
        for n in range(0, grid_size - 2):
            for symbol in symbols:
                # Check if 3 same 'symbol's  are adjacent in one column
                vertical_matching = grid_values[x][n] \
                    == grid_values[x][n + 1] \
                    == grid_values[x][n + 2] == symbol

                if vertical_matching:
                    return True

                # Check if 3 same 'symbol's  are adjacent in one row
                horizontal_matching = grid_values[n][x] \
                    == grid_values[n + 1][x] \
                    == grid_values[n + 2][x] == symbol

                if horizontal_matching:
                    return True


def check_diagonal_line(grid_values, grid_size):
    """
    Check if there are 3 adjacent same 'symbol' s on  same diagonal line
    Params:
        grid_values: list
            The grid's value
        grid_size: int
            The grid size
    Return:
        True: If there are 3 adjacent same 'symbol' s on same diagonal line
        None: Otherwise
    """
    # 'O', 'X', '-
    symbols = [p.value for p in Player]
    for x in range(0, grid_size - 2):
        for y in range(0, grid_size - 2):
            for symbol in symbols:
                if grid_values[y][x] == grid_values[y + 1][x + 1] == grid_values[y + 2][x + 2] == symbol:
                    return True

    for x in range(2, grid_size):
        for y in range(0, grid_size - 2):
            for symbol in symbols:
                if grid_values[x][y] == grid_values[x - 1][y + 1] == grid_values[x - 2][y + 2] == symbol:
                    return True


def check_for_winner(grid_values, grid_size):
    if check_straight(grid_values, grid_size) or check_diagonal_line(grid_values, grid_size):
        return True


def slot_free(grid_values, x, y):
    return True if grid_values[x][y] == ' ' else False


def get_grid_size_from_user():
    while True:
        try:
            grid_size = input('Please enter the grid size (5 - 10): ')
            grid_size = int(grid_size)
            if 5 <= grid_size <= 10:
                return grid_size
        except ValueError:
            print("\n**ERROR** Please enter INTEGER!!**\n")


def main():
    game_intro()
    grid_size = get_grid_size_from_user()
    # Initialize grid values are ' '
    # Grid is a square with size grid_size x grid_size
    grid_values = [[' ' for i in range(grid_size)] for i in range(grid_size)]
    current_player = chose_first_player()
    game_init(grid_values, grid_size, current_player)
    play(current_player, grid_values, grid_size)


if __name__ == '__main__':
    main()
