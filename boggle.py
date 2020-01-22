# # # # # # #  EX12  # # # # # # #
# ID        : 316138007         &&
# NAME      : Michael Sichenko  && Or Katz
# LOGIN     : m_sich            && orkatz
# COMMENTS  :
# # # # # # # # # # # # # # # #
import tkinter
import Game
import Cube

def game_loop(game):
    # TODO - create cubes
    matrix = game.get_matrix()
    game_cubes = []
    for row in matrix:
        for letter in row:
            cube = Cube(letter)
        game_cubes.append(cube)


game = Game()


if __name__ == '__main__':
    pass
