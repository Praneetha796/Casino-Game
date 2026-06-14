import streamlit as st

from coin_toss import coin_toss
from dice_game import dice_game
from guessing_game import guessing_game
from lottery import lottery
from rock_paper_scissors import rock_paper_scissors
import base64
st.set_page_config(
    page_title="Quantum Casino",
    page_icon="🎰",
    layout="wide"
)
facts=[ "⚛️ A qubit can be 0 and 1 simultaneously.",
    "⚛️ IBM Quantum computers are cloud accessible.",
    "⚛️ Quantum entanglement links distant particles.",
    "⚛️ Shor's algorithm can factor integers efficiently."
    ]
import random
st.sidebar.info(random.choice(facts))
st.sidebar.write("🏆 Achievements")
if "achievements" not in st.session_state:
       st.session_state.achievements=[] 

if "selected_game" not in st.session_state:
    st.session_state.selected_game=None

if "games_played" not in st.session_state:
    st.session_state.games_played=0
if "wins" not in st.session_state:
    st.session_state.wins=0
if "coins" not in st.session_state:
    st.session_state.coins=1000        
if "coins" not in st.session_state:
    st.session_state.coins=1000
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("💰 Coins", st.session_state.coins)
with col2:
    st.metric("🎮 Games Played", st.session_state.games_played)
with col3:
    st.metric("🏆 Wins", st.session_state.wins)   
st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #000000,
        #0a0f1f,
        #111111
    );
}

h1{
    color: gold !important;
}

h2,h3{
    color: white !important;
}

</style>
""", unsafe_allow_html=True)
        

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_image = get_base64("images/casino game.jpg")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:images/casino game.jpg;base64,{bg_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.65);
        z-index: -1;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Quantum Casino")
st.markdown("""
<div style="
padding:30px;
border-radius:20px;
background:rgba(255,215,0,0.1);
border:2px solid gold;
">
<h1 style="color:gold;">🎰 Quantum Casino</h1>
<h3>Powered by Quantum Randomness ⚛️</h3>
</div>
""", unsafe_allow_html=True)



# game = st.sidebar.radio(
#     "🎮 Choose a game",
#     [
#         "🪙 Coin Toss",
#         "🎲 Dice Game",
#         "🎯 Guessing Game",
#         "🎫 Lottery",
#         "✂️ Rock Paper Scissors"
#     ]
# )
# st.markdown("""
# <style>

# [data-testid="stSidebar"]{
#     background-color: #111827;
# }

# </style>
# """, unsafe_allow_html=True)
# st.sidebar.metric("Games Played", 12)
# st.sidebar.metric("Wins", 8)
games=[("🪙 Coin toss", "coin_toss", "icons/coin toss.png"),
       ("🎲 Dice Game", "dice_game", "icons/dice.png"),
       ( "🎯 Guessing Game", "guessing_game", "icons/guessing game.png"),
       ("🎫 Lottery", "lottery", "icons/lottery.png"),
       ("✂️ Rock Paper Scissors", "rps", "icons/rps.png")
       ]
st.markdown("<br>", unsafe_allow_html=True)

for i in range(0, len(games), 2):

    left, col1, col2, right = st.columns([1, 2, 2, 1])

    with col1:
        st.image(games[i][2], width=180)
        if st.button(games[i][0], key=games[i][1]):
            st.session_state.selected_game=games[i][1] 
    if i + 1 < len(games):
        with col2:
            st.image(games[i + 1][2], width=180)
            if st.button(games[i + 1][0], key=games[i + 1][1]):
                st.session_state.selected_game=games[i + 1][1]     
                   
          
     # COIN TOSS
game=st.session_state.get("selected_game")
if game == "coin_toss":

    st.header("🪙 Coin Toss")

    if st.button("Flip Coin", key="flip_coin"):

        st.session_state.games_played += 1

        result = coin_toss()

        if result == "Heads":
            st.success("👑 Heads")
            st.session_state.wins += 1
            st.session_state.coins += 50
        else:
            st.success("🪙 Tails")
            
         
    # DICE GAME
elif game == "dice_game":

    st.header("🎲 Dice Game")

    if st.button("Roll Dice", key="roll_dice"):

        st.session_state.games_played += 1

        value = dice_game()

        dice_faces = {
            1:"⚀", 2:"⚁", 3:"⚂",
            4:"⚃", 5:"⚄", 6:"⚅"
        }

        st.markdown(f"# {dice_faces[value]}")
        st.write("Dice Value:", value)

        if value >= 5:
            st.success("🏆 You Win!")
            st.session_state.wins += 1
            st.session_state.coins += 100

# LOTTERY

elif game == "lottery":

    st.header("🎫 Lottery")

    if st.button("Generate Lottery Numbers"):

        st.session_state.games_played += 1

        numbers = lottery()

        st.success(
            " | ".join(map(str, numbers))
        )

# GUESSING GAME
elif game == "guessing_game":

    st.header("🎯 Guessing Game")

    if "secret" not in st.session_state:
        st.session_state.secret = guessing_game()

    guess = st.number_input(
        "Enter number",
        min_value=1,
        max_value=10,
        value=1
    )

    if st.button("Guess", key="guess_btn"):

        st.session_state.games_played += 1

        if guess == st.session_state.secret:

            st.success("🎉 Correct!")

            st.session_state.wins += 1
            st.session_state.coins += 100

            st.session_state.secret = guessing_game()

        elif guess < st.session_state.secret:
            st.warning("⬇ Too Low")

        else:
            st.warning("⬆ Too High")

# ROCK PAPER SCISSORS
elif game == "rps":

    st.header("✂️ Rock Paper Scissors")

    user_choice = st.selectbox(
        "Choose",
        ["Rock", "Paper", "Scissors"]
    )

    if st.button("Play", key="rps_play"):

        st.session_state.games_played += 1

        computer = rock_paper_scissors()

        st.write("Computer:", computer)

        if user_choice == computer:
            st.info("🤝 Draw")

        elif (
            (user_choice == "Rock" and computer == "Scissors")
            or
            (user_choice == "Paper" and computer == "Rock")
            or
            (user_choice == "Scissors" and computer == "Paper")
        ):

            st.success("🏆 You Win!")

            st.session_state.wins += 1
            st.session_state.coins += 50

        else:
            st.error("💻 Computer Wins!")
   
   

st.divider()

st.caption(
    "Quantum Casino • Powered by Qiskit and Streamlit"
)