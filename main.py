import argparse
import timeit
import search as s
import psutil
import os

initial_state = []

pid = os.getpid()
p = psutil.Process(pid)

def read(configuration):
    initial_state = []
    data = configuration.split(",")

    for element in data:
        initial_state.append(int(element))

    conf_board_len = len(initial_state)

    conf_board_side = int(conf_board_len ** 0.5)

    return initial_state, conf_board_len, conf_board_side


def main(algorithm=None, board=None):

    if algorithm is None:
        parser = argparse.ArgumentParser()
        parser.add_argument('algorithm')
        parser.add_argument('board')
        args = parser.parse_args()
        bboard = args.board
        algo = args.algorithm
    else:
        bboard = board
        algo = algorithm

    print(bboard)
    print(algo)

    initial_state, board_len, board_side = read(bboard)

    ops_obj = s.Operations(board_side=board_side, board_len=board_len, initial_state=initial_state)

    search_obj = s.Search(initial_state=initial_state, ops_obj=ops_obj)

    function_map = {
        'bfs': search_obj.bfs,
        'dfs': search_obj.dfs,
        'ast': search_obj.ast,
    }

    function = function_map[algo]

    start = timeit.default_timer()

    frontier = function(initial_state)

    stop = timeit.default_timer()

    search_obj.set_goal_node()
    memoryUse = p.memory_info()[0]
    return ops_obj.ret_moves()
    # ops_obj.export(frontier, stop-start, memoryUse/(10**6))



if __name__ == '__main__':
    main()
