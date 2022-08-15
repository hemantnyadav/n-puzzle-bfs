from Search_Algorithms import BFS
from time import time

# TODO: get the list size and list from user input
#root = [1, 8, 2, 0, 4, 3, 7, 6, 5]
#root = [7, 5, 3, 0, 1, 6, 4, 8, 2]
n = 3
root = [7, 5, 3, 0, 1, 6, 4, 8, 2]
print("The given state is:", root)

def inv_num(puzzle):
    inv_count = 0
    for i in range(len(puzzle-1)):
        for j in range(i+1,len(puzzle)):
            if((puzzle(i)>puzzle(j)) and puzzle(i) and puzzle(j)):
                inv_count+=1

    return inv_count

def solvable(puzzle):
    inv_counter = inv_num(puzzle)
    if(inv_counter%2 == 0):
        return True
    else:
        return False


if solvable(root):
    print("Solvable, please wait. \n")

    start_time = time()
    BFS_solution = BFS(root, n)

    time_taken = time() - start_time
    print('BFS Solution is ', BFS_solution[0])
    print('Number of explored nodes is ', BFS_solution[1])    
    print('BFS Time:', time_taken , "\n")
