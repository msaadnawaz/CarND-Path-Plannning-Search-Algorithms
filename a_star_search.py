# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 11:29:36 2018

@author: B51427
"""

# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
# 
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------

grid = [[0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0]]

heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    
    opened = []
    init_pos = [0, 0 + heuristic[init[0]][init[1]]] + init
    opened.append(init_pos)
    goal_achieved = False
    checked = expansion_grid = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    
    expansion_grid = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
    optimal_path = [[' ' for i in range(len(grid[0]))] for j in range(len(grid))]    
    checked[init_pos[2]][init_pos[3]] = 1
    expansion_count = -1
    
    for cell in opened:
        if cell[2:] == goal:
            goal_achieved = True
            path = cell
            expansion_count+=1
            expansion_grid[path[2]][path[3]] = expansion_count
            
    while not(goal_achieved):
        minval = heuristic[init[0]][init[1]] + len(grid) * len(grid[0])
        min_cell = []
        if opened != []:
            print("\nList items:")
            print(opened)
            for cell in opened:
                if cell[1] < minval:
                    minval = cell[1]
                    min_cell = cell
            print("\nTaken items:")
            print(min_cell)
            opened.remove(min_cell)
            expansion_count+=1
            g = min_cell[0]
            f = min_cell[1]
            x = min_cell[2]
            y = min_cell[3]
            expansion_grid[x][y] = expansion_count
            for step in delta:
                if (step[0]+x >= 0) and (step[1]+y >= 0) \
                   and (step[0]+x < len(grid)) and (step[1]+y < len(grid[0])) \
                       and (grid[step[0]+x][step[1]+y]== 0) and (checked[step[0]+x][step[1]+y]== 0):
                           opened.append([g+cost, g+cost+heuristic[step[0]+x][step[1]+y], step[0]+x, step[1]+y])
                           checked[step[0]+x][step[1]+y] = 1
            for cell in opened:
                if cell[2:] == goal:
                    goal_achieved = True
                    path = cell
                    expansion_count+=1
                    expansion_grid[path[2]][path[3]] = expansion_count
        else:
            print("\n**********************")
            print("Expansion Grid:")
            print(expansion_grid)
            print("\n**********************")
            print("FINAL OUTPUT")
            return 'FAIL'
    pos = init
    index = init
    while pos != goal:
        maxval = expansion_grid[pos[0]][pos[1]]    
        for step in delta:
            if (pos[0]+step[0] >=0) and (pos[1]+step[1] >= 0) \
                and (pos[0]+step[0] < len(grid)) and (pos[1]+step[1] < len(grid[0])) \
                and (expansion_grid[pos[0]+step[0]][pos[1]+step[1]] > maxval):
                    index = [pos[0]+step[0],pos[1]+step[1]]
        move = [index[0]-pos[0], index[1]-pos[1]]
        for i in range(len(delta)):
            if move == delta[i]:
                optimal_path[pos[0]][pos[1]] = delta_name[i]
        pos = index
    optimal_path[goal[0]][goal[1]] = '*'
    print("\n**********************")
    print("Expansion Grid:")
    print(expansion_grid)
    print("\n**********************")
    print("Optimal Path:")
    print(optimal_path)
    print("\n**********************")
    print("FINAL OUTPUT")
    return path


print(search(grid,init,goal,cost))