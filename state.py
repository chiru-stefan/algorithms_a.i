
class State:

    def __init__(self, state, parent, move, depth, cost, key):

        self.state = state

        self.parent = parent

        self.move = move

        self.depth = depth

        self.cost = cost

        self.key = key

        if self.state:
            self.map = ''.join(str(e) for e in self.state)

    def __eq__(self, other):
        assert isinstance(other, State), "Can't compare items of different classes"
        return self.map == other.map

    def __lt__(self, other):
        assert isinstance(other, State), "Can't compare items of different classes"
        return self.map < other.map
