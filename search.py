from heapq import heappush, heappop, heapify
import itertools
from collections import deque
from ops import *


class Search():

    def __init__(self, initial_state, ops_obj, goal_state=[0, 1, 2, 3, 4, 5, 6, 7, 8]):
        super(Search, self).__init__()
        self.goal_state = goal_state
        self.ops_obj = ops_obj
        self.initial_state = initial_state
        self.max_frontier_size=0; self.goal_node=0; self.max_search_depth=0


    def set_goal_node(self):
        '''
        Sends data back to Operations in order to complete the backtrace
        :return:
        '''
        self.ops_obj.set_gn(self.goal_node, self.max_frontier_size, self.max_search_depth)


    def bfs(self, start_state):
        '''
        In theory is used a 'color' property, here I used containers that took the job of that property - mainly for checking visited / reached / not visited
        :param start_state: usually initial state
        :return: the breadth-first tree (containerized in a deque --- double ended queue)
        '''
        explored, frontier = set(), deque([State(start_state, None, None, 0, 0, 0)])
        print("IN BFS")
        max_n = 0
        while frontier:

            max_n += 1
            node = frontier.popleft()

            explored.add(node.map)
            if node.state == self.goal_state:
                print("Reached goal")
                self.goal_node = node
                return frontier

            neighbors = self.ops_obj.expand_bfs(node)

            for neighbor in neighbors:
                if neighbor.map not in explored:
                    frontier.append(neighbor)
                    explored.add(neighbor.map)

                    if neighbor.depth > self.max_search_depth:
                        self.max_search_depth += 1

            if len(frontier) > self.max_frontier_size:
                self.max_frontier_size = len(frontier)
        print(max_n)    # max tries until crash



# 181440

    def dfs(self, start_state):
        '''
        Searching the vertices first. expand(node) takes the depth neighbors first --- going in left/right after
        Keeps record of visited nodes and max depth and max width (frontier)
        :param start_state: usually initial state
        :return: the path in container<stack>
        '''

        explored, stack = set(), list([State(start_state, None, None, 0, 0, 0)])    # Initialize root node (in literature s node/vertex)

        while stack:

            node = stack.pop()                                  # pop(right) the last element inserted --- stack -> LIFO

            explored.add(node.map)                              # Add the current node to explored set so we can't get in a loop

            if node.state == self.goal_state:                   # If we got to the end -> return the depth-first tree
                self.goal_node = node
                return stack

            neighbors = reversed(self.ops_obj.expand(node))     # expand the current node and reverse the returned list(left-right-up-down  -> down->up... )

            for neighbor in neighbors:                          # check each adjacent vertex
                if neighbor.map not in explored:
                    stack.append(neighbor)                      # add the neighbor into df-tree
                    explored.add(neighbor.map)

                    if neighbor.depth > self.max_search_depth:  # keep track of the max depth --- has no role into computation
                        self.max_search_depth += 1

            if len(stack) > self.max_frontier_size:             # keep track of max_frontier --- has no role into computation
                self.max_frontier_size = len(stack)



    def ast(self, start_state):
        '''
        A-star implementation using priority queue

        :param start_state: usually initial state
        :return: a tree of paths in container<stack>
        '''

        mlen = 0
        explored, heap, heap_entry, counter = set(), list(), {}, itertools.count()

        key = self.ops_obj.h(start_state)

        root = State(start_state, None, None, 0, 0, key)

        entry = (key, 0, root)

        heappush(heap, entry)

        heap_entry[root.map] = entry

        while heap:
            mlen+=1
            node = heappop(heap)

            explored.add(node[2].map)

            if node[2].state == self.goal_state:
                self.goal_node = node[2]
                return heap

            neighbors = self.ops_obj.expand(node[2])

            for neighbor in neighbors:

                neighbor.key = neighbor.cost + self.ops_obj.h(neighbor.state) # f(n) = g(n) + h(n)

                entry = (neighbor.key, neighbor.move, neighbor)

                if neighbor.map not in explored:

                    heappush(heap, entry)

                    explored.add(neighbor.map)

                    heap_entry[neighbor.map] = entry

                    if neighbor.depth > self.max_search_depth:
                        self.max_search_depth += 1

                elif neighbor.map in heap_entry and neighbor.key < heap_entry[neighbor.map][2].key:

                    hindex = heap.index((heap_entry[neighbor.map][2].key,
                                         heap_entry[neighbor.map][2].move,
                                         heap_entry[neighbor.map][2]))

                    heap[int(hindex)] = entry

                    heap_entry[neighbor.map] = entry

                    heapify(heap)   # convert list into heap

            if len(heap) > self.max_frontier_size:
                self.max_frontier_size = len(heap)
        print("A star: ", mlen)
