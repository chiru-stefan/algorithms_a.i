from state import State
import datetime


class Operations():

    def __init__(self, board_side, board_len, initial_state, goal_state=[0, 1, 2, 3, 4, 5, 6, 7, 8]):
        super(Operations, self).__init__()
        print("Ops init state: ", initial_state)
        self.goal_state = goal_state
        self.initial_state = initial_state
        self.nodes_expanded = 0

        self.board_side = board_side
        self.board_len = board_len

        self.goal_node = State
        self.max_frontier_size = 0
        self.max_search_depth = 0

        self.moves = list()
        self.costs = set()
        self.some_states = []

    def set_gn(self, goal_node, max_frontier, max_search_depth):
        self.goal_node = goal_node
        self.max_frontier_size = max_frontier
        self.max_search_depth = max_search_depth


    def expand(self, node):

        self.nodes_expanded += 1

        neighbors = list()

        neighbors.append(State(self.move(node.state, 1), node, 1, node.depth + 1, node.cost + 1, 0))
        neighbors.append(State(self.move(node.state, 2), node, 2, node.depth + 1, node.cost + 1, 0))
        neighbors.append(State(self.move(node.state, 3), node, 3, node.depth + 1, node.cost + 1, 0))
        neighbors.append(State(self.move(node.state, 4), node, 4, node.depth + 1, node.cost + 1, 0))

        nodes = [neighbor for neighbor in neighbors if neighbor.state]

        return nodes


    def expand_bfs(self, node):

        self.nodes_expanded += 1

        neighbors = list()

        neighbors.append(State(self.move(node.state, 4), node, 4, node.depth + 1, node.cost + 1, 0))
        neighbors.append(State(self.move(node.state, 3), node, 3, node.depth + 1, node.cost + 1, 0))
        neighbors.append(State(self.move(node.state, 1), node, 1, node.depth + 1, node.cost + 1, 0))
        neighbors.append(State(self.move(node.state, 2), node, 2, node.depth + 1, node.cost + 1, 0))

        nodes = [neighbor for neighbor in neighbors if neighbor.state]

        return nodes


    def move(self, state, position):

        new_state = state[:]

        index = new_state.index(0)

        if position == 1:  # Up

            if index not in range(0, self.board_side):

                temp = new_state[index - self.board_side]
                new_state[index - self.board_side] = new_state[index]
                new_state[index] = temp

                return new_state
            else:
                return None

        if position == 2:  # Down

            if index not in range(self.board_len - self.board_side, self.board_len):

                temp = new_state[index + self.board_side]
                new_state[index + self.board_side] = new_state[index]
                new_state[index] = temp

                return new_state
            else:
                return None

        if position == 3:  # Left

            if index not in range(0, self.board_len, self.board_side):

                temp = new_state[index - 1]
                new_state[index - 1] = new_state[index]
                new_state[index] = temp

                return new_state
            else:
                return None

        if position == 4:  # Right

            if index not in range(self.board_side - 1, self.board_len, self.board_side):

                temp = new_state[index + 1]
                new_state[index + 1] = new_state[index]
                new_state[index] = temp

                return new_state
            else:
                return None


    def h(self, state):     # Manhattan Distance
        heuristic_function = sum(abs(b % self.board_side - g % self.board_side) + abs(b//self.board_side - g//self.board_side)        # // operator does integer division (i.e. quotient without remainder)
                   for b, g in ((state.index(i), self.goal_state.index(i)) for i in range(1, self.board_len)))
        return heuristic_function


    def backtrace(self):

        current_node = self.goal_node

        while self.initial_state != current_node.state:

            if current_node.move == 1:
                movement = 'Up'
            elif current_node.move == 2:
                movement = 'Down'
            elif current_node.move == 3:
                movement = 'Left'
            else:
                movement = 'Right'

            self.moves.insert(0, movement)
            current_node = current_node.parent


    def export(self, frontier, time, ram):

        self.backtrace()
        file = open("output"+\
            "_".join(str(datetime.datetime.ctime(datetime.datetime.now())).split(' '))[10:19] + ".txt", 'w')

        file.write("path_to_goal: " + str(self.moves))
        file.write("\ncost_of_path: " + str(len(self.moves)))
        file.write("\nnodes_expanded: " + str(self.nodes_expanded))
        file.write("\nfringe_size: " + str(len(frontier)))                  # Look in readme for the frontier explanation
        file.write("\nmax_fringe_size: " + str(self.max_frontier_size))     # Look in readme for the max_frontier_size explanation
        file.write("\nsearch_depth: " + str(self.goal_node.depth))
        file.write("\nmax_search_depth: " + str(self.max_search_depth))
        file.write("\nrunning_time: " + format(time, '.8f'))
        file.write(f"\nmax_ram_usage: {ram}")
        file.close()


    def ret_moves(self):
        self.backtrace()

        return self.moves

