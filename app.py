import streamlit as st
import time

# Initialize session state for login tracking
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    # --- PAGE ROUTING ---
if st.session_state.logged_in:
    # --- MAIN PHISHING DETECTION PAGE ---
    st.title("Phishing Detection App")
    
    # Logout option
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    url_input = st.text_input("Enter URL", placeholder="aceexam.in")
    
    if st.button("Check"):
        if url_input:
            with st.status("Checking URL...", expanded=True) as status:
                time.sleep(2) # Simulate processing
                # Example logic: replace with your ML model
                if "google" in url_input.lower() or "aceexam.in" in url_input.lower():
                    st.success(f"✅ Phishing Attack Not Found for {url_input}")
                else:
                    st.error(f"🚨 Phishing Attack Found for {url_input}")
                status.update(label="Check Complete!", state="complete")

else:
    # --- LOGIN & REGISTER PAGES ---
    # (Insert your Title, Nav-bar, and Banner code here)
    
    page = st.radio("Navigation", ["Login", "Register"], horizontal=True)

    if page == "Login":
        st.markdown('<p style="color:red; font-size:24px;">Login Using Your Account:</p>', unsafe_allow_html=True)
        with st.form("login_form"):
            user = st.text_input("User Name")
            pw = st.text_input("Password", type="password")
            if st.form_submit_button("Login"):
                if user == "keerthi": # Add your actual validation here
                    st.session_state.logged_in = True
                    st.success("Login Successful!")
                    time.sleep(1)
                    st.rerun() # This triggers the switch to the Detection Page
                else:
                    st.error("Invalid credentials")

    elif page == "Register":
        # Insert your two-column registration form here
        st.info("Registration Page Content")

 
