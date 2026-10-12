import random

import streamlit as st

MIN_NUMBER = 1
MAX_NUMBER = 100


# --- Game logic ---
def check_guess(guess, secret):
    """Compare a guess with the secret number and return (outcome, message)."""
    if guess == secret:
        return "win", "YOU WIN"

    direction = "higher" if guess < secret else "lower"
    if abs(secret - guess) <= 5:
        return "close", f"JUST CLOSE! Go a little {direction}."
    return "miss", f"Not the magic number, bro. Go {direction}."


def new_game():
    """Pick a fresh secret number and clear the scoreboard."""
    st.session_state.secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    st.session_state.guesses = []
    st.session_state.last_result = None
    st.session_state.won = False
    st.session_state.celebrate = False


def submit_guess():
    """Runs when the player presses the button (or Enter in the box)."""
    guess = int(st.session_state.guess_input)
    outcome, message = check_guess(guess, st.session_state.secret_number)
    st.session_state.guesses.append(guess)
    st.session_state.last_result = (outcome, message)
    if outcome == "win":
        st.session_state.won = True
        st.session_state.celebrate = True


# Streamlit reruns this whole file on every click, so game state lives in session_state
if "secret_number" not in st.session_state:
    new_game()

state = st.session_state

# --- Webpage ---
st.title("The Magic Number Game 🎯")
st.write(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}. Can you find it?")

if state.won:
    tries = len(state.guesses)
    word = "try" if tries == 1 else "tries"
    st.success(f"YOU WIN! The magic number was {state.secret_number}. You got it in {tries} {word}.")
    if state.celebrate:
        st.balloons()
        state.celebrate = False
    st.button("Play again", on_click=new_game, type="primary")

else:
    # A form lets the player press Enter instead of clicking the button
    with st.form("guess_form"):
        st.number_input(
            "Hey let's begin! Enter your guess:",
            min_value=MIN_NUMBER,
            max_value=MAX_NUMBER,
            step=1,
            key="guess_input",
        )
        st.form_submit_button("Check My Guess", on_click=submit_guess)

    if state.last_result:
        outcome, message = state.last_result
        if outcome == "close":
            st.warning(message)
        else:
            st.error(message)

    if state.guesses:
        history = "  ·  ".join(
            f"{g} {'⬆️' if g < state.secret_number else '⬇️'}" for g in state.guesses
        )
        st.caption(f"Guesses so far ({len(state.guesses)}): {history}")

    st.button("New game", on_click=new_game)
