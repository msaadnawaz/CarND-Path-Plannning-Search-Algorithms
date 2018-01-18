# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 14:26:17 2018

@author: B51427
"""

# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
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
    init_pos = [0] + init
    opened.append(init_pos)
    goal_achieved = False
    checked = expansion_grid = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    
    expansion_grid = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
    optimal_path = [[' ' for i in range(len(grid[0]))] for j in range(len(grid))]    
    checked[init_pos[1]][init_pos[2]] = 1
    expansion_count = -1
    
    for cell in opened:
        if cell[1:] == goal:
            goal_achieved = True
            path = cell
            expansion_count+=1
            expansion_grid[path[1]][path[2]] = expansion_count
            
    while not(goal_achieved):
        minval = len(grid) * len(grid[0])
        min_cell = []
        if opened != []:
            print("\nList items:")
            print(opened)
            for cell in opened:
                if cell[0] < minval:
                    minval = cell[0]
                    min_cell = cell
            print("\nTaken items:")
            print(min_cell)       
            opened.remove(min_cell)
            expansion_count+=1
            expansion_grid[min_cell[1]][min_cell[2]] = expansion_count
            for step in delta:
                if (step[0]+min_cell[1] >= 0) and (step[1]+min_cell[2] >= 0) \
                   and (step[0]+min_cell[1] < len(grid)) and (step[1]+min_cell[2] < len(grid[0])) \
                       and (grid[step[0]+min_cell[1]][step[1]+min_cell[2]]== 0) and (checked[step[0]+min_cell[1]][step[1]+min_cell[2]]== 0):
                           opened.append([min_cell[0]+cost, step[0]+min_cell[1], step[1]+min_cell[2]])
                           checked[step[0]+min_cell[1]][step[1]+min_cell[2]] = 1
            for cell in opened:
                if cell[1:] == goal:
                    goal_achieved = True
                    path = cell
                    expansion_count+=1
                    expansion_grid[path[1]][path[2]] = expansion_count
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