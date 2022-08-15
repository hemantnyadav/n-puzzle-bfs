from State import State
from queue import PriorityQueue
from queue import Queue
from queue import LifoQueue

#Breadth-first Search
def BFS(initial_state , n):
    root = State(initial_state,None, None, 0, 0)
    if root.test():
        return root.solution()
    frontier = Queue()  #Queue of states to be verified for solution and explored
    frontier.put(root)  # Add initial state
    explored = []       # Empty list of explored noded  
    
    while not(frontier.empty()):
        current_node = frontier.get()
        explored.append(current_node.state)
        print(current_node.state)
        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)
    return