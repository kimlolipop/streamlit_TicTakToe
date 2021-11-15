import p1vsp2
import PlayerVsBot
import streamlit as st

BtnStyle = """
<style>
div.stButton > button:first-child {
    background-color: #6C4D94;
    color:#6C4D94;
    
}

div.stButton > button:hover {
    background-color: #00ff00;
    color:#ff0000;
    }
    
</style>"""

TicTacToe = """ <style> .font {font-size:50px ; font-family: 'Cooper Black'; color: #FF9633;} </style> """

st.markdown(BtnStyle, unsafe_allow_html=True)
st.markdown(TicTacToe, unsafe_allow_html=True)



add_selectbox = st.sidebar.radio(
    "How would you like to be contacted?",
    ("Player1 vs Player2", "Player vs Tic Tak Toe(Ai)")
)


if add_selectbox == "Player1 vs Player2":
    p1vsp2.show()
    
elif add_selectbox == "Player vs Tic Tak Toe(Ai)":
    PlayerVsBot.show()
    
    