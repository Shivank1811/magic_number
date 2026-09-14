import streamlit as st
import random

# --- Your original function ---
def check_guess(guess_number, secret_number):
    if secret_number == guess_number:
        return "YOU WIN"
    elif abs(secret_number - guess_number) <= 5:
        return "JUST CLOSE"
    elif abs(secret_number - guess_number) > 5:
        return "YOU CLOCK IT BRO BUT SORRY IT IS NOT A MAGIC NUMBER"

# --- Webpage Setup ---
st.title("The Magic Number Game 🎯")

# Streamlit's way of remembering variables between clicks
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)

# --- User Input ---
# Creates a clean number input box on the webpage
guess_number = st.number_input("Hey let's begin! Enter your guess:", min_value=1, max_value=200, step=1)

# --- The "Submit" Button ---
if st.button("Check My Guess"):
    
    # Your developer exit code! We'll use it to manually reset the game.
    if guess_number == 111:
        st.info("Developer override: Game reset successfully.")
        st.session_state.secret_number = random.randint(1, 100)
        
    else:
        # Run your logic using the saved secret number
        result = check_guess(guess_number, st.session_state.secret_number)
        
        # Display the result with colored message boxes
        if result == "YOU WIN":
            st.success(f"{result}! The magic number was {st.session_state.secret_number}.")
            st.balloons() # Streamlit adds celebratory balloons!
            
            # Generate a new number for the next round
            st.session_state.secret_number = random.randint(1, 100)
            
        elif result == "JUST CLOSE":
            st.warning(result)
        else:
            st.error(result)



