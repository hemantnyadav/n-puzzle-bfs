# n-puzzle-bfs
Implementation of n-puzzle game

Note: Link here is a good reference for practice:
[Link text Here](http://cs.tru.ca/~mlee/comp2680/Software/board_game.html)
1. Input initial state as list L
2. Check if given L it is solvalbe
    - This can be done using "number of inversions should be even"
    - functions used for this are solvable and inv_num
3. Appy BFS as follows
    - Add initial state to Q(FIFO queue)
    - Explore all possible move from first state in Q and compare it with goal
    - if goal is matched return
    - else check Q for next state for exploration 

# Steps to run this code



