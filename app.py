import streamlit as st
import time

# --- 1. SESSION STATE INITIALIZATION ---
# This checks if the "logged_in" variable exists; if not, it sets it to False.
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- 2. CUSTOM CSS ---
st.markdown("""
    <style>
    .main-title { font-size: 30px; color: #FF0000; text-align: center; font-weight: bold; }
    .nav-bar { background: linear-gradient(90deg, #ff0066, #6600ff); padding: 10px; border-radius: 5px; text-align: center; color: white; margin-bottom: 15px;}
    .sub-header { font-size: 18px; color: #FF0000; text-align: center; font-weight: bold; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGIC FOR PAGE SWITCHING ---

# CASE A: If the user IS logged in, show the Detection Page
if st.session_state.logged_in:
    st.markdown('<p class="main-title">PhishCatcher: URL Detection Dashboard</p>', unsafe_allow_html=True)
    
    # Logout button in the top right
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    st.write("---")
    url_input = st.text_input("Enter URL to scan:", placeholder="e.g., aceexam.in")
    
    if st.button("Check URL"):
        if url_input:
            with st.spinner("Analyzing..."):
                time.sleep(2)
                # Official Website Logic
                official_sites = ["google.com", "aceexam.in", "microsoft.com"]
                is_safe = any(site in url_input.lower() for site in official_sites)
                
                if is_safe:
                    st.success(f"### ✅ Status: Phishing Attack Not Found")
                    st.info(f"The website {url_input} is an Official/Verified domain.")
                else:
                    st.error(f"### 🚨 Status: Phishing Attack Found!")
                    st.warning("Warning: This URL matches malicious phishing patterns.")
        else:
            st.warning("Please enter a URL.")

# CASE B: If the user IS NOT logged in, show Login/Register
else:
    st.markdown('<p class="main-title">PhishCatcher Client-Side Defense Against Web Spoofing</p>', unsafe_allow_html=True)
    st.markdown('<div class="nav-bar">Home | Remote User | Service Provider</div>', unsafe_allow_html=True)
    
    # Optional Banner
    st.info("Insert Banner.jpg here using st.image()")

    choice = st.radio("Action", ["Login", "Register"], horizontal=True)

    if choice == "Login":
        st.markdown('<p class="sub-header">Login Using Your Account:</p>', unsafe_allow_html=True)
        with st.form("login_form"):
            user = st.text_input("User Name")
            pw = st.text_input("Password", type="password")
            submit = st.form_submit_button("Login")
            
            if submit:
                if user == "keerthi" and pw == "123456": # Replace with your logic
                    st.session_state.logged_in = True
                    st.success("Login Successful! Redirecting...")
                    time.sleep(1)
                    st.rerun() # This reloads the script and triggers CASE A
                else:
                    st.error("Invalid Username or Password")

    else:
        st.markdown('<p class="sub-header">Register Your Details:</p>', unsafe_allow_html=True)
        # (Add your registration form code here from previous step)
        st.info("Registration Form goes here.")
