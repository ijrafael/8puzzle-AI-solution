from search import *

eight_puzzle = EightPuzzle((1, 2, 3, 5, 7, 4, 8, 6, 0))

if __name__ == '__main__':
    #print(eight_puzzle.find_blank_square((1, 2, 3, 4, 5, 7, 8, 9, 0)))
    #print(eight_puzzle.actions((0, 1, 2, 3, 4, 5, 6, 7, 8))) # DOWN, RIGHT
    #print(eight_puzzle.result((0, 1, 2, 3, 4, 5, 6, 7, 8), 'DOWN'))
    #print(eight_puzzle.goal_test((1, 2, 3, 4, 5, 6, 7, 8, 0))) #true
    #print(eight_puzzle.goal_test((4, 8, 1, 6, 0, 2, 3, 5, 7))) #false
    #print(eight_puzzle.check_solvability((0, 1, 2, 3, 4, 5, 6, 7, 8)))
    print(depth_first_graph_search(eight_puzzle, display=True).solution())
    print(breadth_first_graph_search(eight_puzzle, display=True).solution())
    print(astar_search(eight_puzzle, h=None, display=True).solution())

    #print(depth_first_graph_search(eight_puzzle).solution())
    exit()

