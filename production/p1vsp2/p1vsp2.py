import streamlit as st
import numpy as np
from collections import Counter
from env_games import checkWin


_win_point = 5
X = 1
O = 2
space = 0
mark_space = '🗯'

def boardinit():
    board = np.full((8, 8), space, dtype=str)
    board = board.astype(np.int32)
    
    board_show = np.full((8, 8), mark_space, dtype=str)
    
    return board, board_show

# Define callbacks to handle button clicks.
def handle_click(i, j):
    
    if st.session_state.next_player == X:
        mark = '😀'
    else:
        mark = '🤖'
    
    if not st.session_state.winner:
        # TODO: Handle the case when nobody wins but the game is over!
        st.session_state.board[i, j] = int(st.session_state.next_player)
        st.session_state.board_show[i, j] = mark
        if st.session_state.next_player == X:
            st.session_state.next_player = O
        else:
            st.session_state.next_player = X
            
        
        
        
def show():
    
    st.markdown('<p class="font">👾 Tic Tac Toe</p>', unsafe_allow_html=True)
    
    
    # Initialize state.
    if "board" not in st.session_state:
        
        st.session_state.board, st.session_state.board_show = boardinit()
        st.session_state.next_player = X
        st.session_state.winner = None
        
        
         
    if st.session_state.next_player == X:
        mark = '😀'
    else:
        mark = '🤖'
        
        
    col1, col2, col3, col4  = st.beta_columns(4)
    with col1:
        st.header('Your Turn ' + mark)
        
    with col4:
        restart = st.button('🔄')
        if restart:
            st.session_state.board, st.session_state.board_show = boardinit()
            st.session_state.next_player = X
            st.session_state.winner = None  
        
        
    

    if st.session_state.board_show is not None:
        # Show one button for each field.
        for i, row in enumerate(st.session_state.board_show):
            cols = st.beta_columns([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1
                                    ,0.07, 0.07])
            for j, field in enumerate(row):
                cols[j].button(
                    field,
                    key=f"{i}-{j}",
                    on_click=handle_click,
                    args=(i, j),
                )
        
        winner = checkWin(st.session_state.board)      
        if winner != -1:
            if winner == 1:
                winner = '😀'
            elif winner == 2:
                winner = '🤖'
            elif winner == 0:
                winner = 'Draw'
            st.session_state.winner = winner

        if st.session_state.winner == 'Draw':
            st.info(f"Draw!")
        elif st.session_state.winner:
            st.success(f"Congrats! {st.session_state.winner} won the game! 🎈")


