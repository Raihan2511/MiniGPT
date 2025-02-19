import streamlit as st
from backend.auth.authentication import verify_password
from backend.models.database import get_db
from backend.models.user import User
from sqlalchemy.orm import Session

def show():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        db: Session = next(get_db())
        user = db.query(User).filter(User.username == username).first()
        
        if user and verify_password(password, user.password):
            st.session_state["authenticated"] = True
            st.success("Login successful! You can now chat.")
        else:
            st.error("Invalid username or password")
