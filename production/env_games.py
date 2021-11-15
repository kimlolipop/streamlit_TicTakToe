import streamlit as st
import numpy as np
from collections import Counter

_win_point = 5
X = 1
O = 2
space = 0

def getMoves(board):
    moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                moves.append((i, j))
#     st.write(board[0][0])
    return moves


## 
def checkRows(board):
    for row in board:
        for i in range(0, len(row)):
            check_list = []
            for j in range(0,_win_point):
                if i <= (len(board)-_win_point):
                    check_list.append(row[i+j])
                # end if
            # next
            
            count = Counter(check_list)
            if count[O] == _win_point:
                return O
            if count[X] == _win_point:
                return X

    return None

def checkDiagonals(board):
    # right Diagonals 
    for idx, row in enumerate(board):
        if idx <= (len(board)-_win_point):
            
            for i in range(len(row)):
                check_list = []
                for j in range(0,_win_point):
                    if i <= (len(board)-_win_point):
                        if j == 0:
                            check_list.append(row[i+j])
                        else:
                            check_list.append(board[idx+j][i+j])
                            
                count = Counter(check_list)

                if count[O] == _win_point:
                    return O
                if count[X] == _win_point:
                    return X

                
    # Left Diagonals           
    for idx, row in enumerate(board):
        if idx <= (len(board)-_win_point):
            
            for i in range(len(row)):
                check_list = []
                for j in range(0,_win_point):
                    if i >= (len(board)-_win_point-1):
                        if j == 0:
                            check_list.append(row[i+j])
                        else:
                            check_list.append(board[idx+j][i-j])
                            
#                 st.write(check_list)            
                count = Counter(check_list)

                if count[O] == _win_point:
                    return O
                if count[X] == _win_point:
                    return X

                
                
                
    return None

def checkWin(board):
    # transposition to check rows, then columns
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
        
    # check Diagonals  
    result = checkDiagonals(board)
    if result:
        return result
    
    # check draw
    if (len(getMoves(board)) == 0):
        # It's a draw
        return 0
    else:
        # Still more moves to make
        return -1
    
