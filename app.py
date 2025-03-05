import streamlit as st
import re
import random
import string
from streamlit_extras.let_it_rain import rain

# Common weak passwords list
weak_passwords = {"password", "123456", "qwerty", "abc123", "password123", "admin", "letmein", "welcome"}

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🟠 Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🟡 Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🔵 Include at least one special character (!@#$%^&*).")
    
    if password.lower() in weak_passwords:
        score = 1  # Force weak rating
        feedback.append("⚠️ This password is too common. Choose a more unique one.")
    
    return score, feedback


def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")
st.title("🔐 Password Strength Meter")
st.subheader("Check your password security & get suggestions!")

password = st.text_input("Enter your password:", type="password")

if password:
    score, feedback = check_password_strength(password)
    

    st.markdown("### Password Strength")
    st.progress(score / 4)
    
    if score == 4:
        st.success("✅ Strong Password!")
        rain(emoji="🎉", font_size=30, falling_speed=5, animation_length="5")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider improving it.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions below.")
    
    # Show feedback
    for tip in feedback:
        st.write(f"- {tip}")

if st.button("🔄 Generate Strong Password"):
    strong_password = generate_strong_password()
    st.info(f"🔑 Suggested Password: `{strong_password}`")
    

    st.code(strong_password, language="")