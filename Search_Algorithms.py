from State import State
from queue import PriorityQueue
from queue import Queue
from queue import LifoQueue

#Breadth-first Search
def BFS(initial_state , n):
    root = State(initial_state)
    if root.test():
        return root.solution()
    frontier = Queue()
    frontier.put(root)
    explored = []
    
    while not(frontier.empty()):
        current_node = frontier.get()
        #print(current_node.state)
        explored.append(current_node.state)
        
        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)
    return