import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        return "✅ Strong Password!",feedback
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", feedback
    else:
        return("❌ Weak Password - Improve it using the suggestions above."), feedback

st.title ("🔒 Password Strength Checker")

password = st.text_input ("Enter your password:", type = "password" )

if st.button("Check Strength"):
    if password:
        result, feedback = check_password_strength(password)
        st.subheader(result)
        for suggestion in feedback:
            st.write(suggestion)
    else:
        st.warning("⚠️ Please enter a password to check.")



