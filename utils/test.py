import math
import time
import matplotlib.pyplot as plt
from app import Board
from connect4 import alphabeta, minimax


def main():
    """
    Function to time the runtime of minimax and abp algorithm
    Plot the results
    
    """
    board = Board(6, 7)

    player = board.PLAYER1

    minimax_data = []
    abp_data = []
    x = [1, 2, 3, 4, 5]
    for i in range(1, 6, 1):

        # measure time for minimax
        start_time = time.time()
        minimax(player, board, i, True)
        minimax_time = time.time() - start_time
        minimax_data.append(minimax_time)

        # measure time for abp
        start = time.time()
        alphabeta(player, board, i, alpha=-math.inf, beta=math.inf)
        abp_time = time.time() - start
        abp_data.append(abp_time)

    print(minimax_data)
    print(abp_data)
    # plot the diagrams
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.plot(x, minimax_data)
    plt.title("Minimax Runtime with Depth")
    plt.xlabel("Depth Limit")
    plt.ylabel("Time Used")
    plt.show()

    plt.rcParams["figure.figsize"] = (10, 6)
    plt.plot(x, abp_data)
    plt.title("Alpha-Beta Pruning Runtime with Depth")
    plt.xlabel("Depth Limit")
    plt.ylabel("Time Used")
    plt.show()

    plt.rcParams["figure.figsize"] = (10, 6)
    plt.plot(x, abp_data, label="ABP")
    plt.plot(x, minimax_data, label="MINIMAX")
    plt.title("Comparison")
    plt.xlabel("Depth Limit")
    plt.ylabel("Time Used")
    plt.show()


if __name__ == "__main__":
    main()
