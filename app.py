import streamlit as st

# --- 1. SET PAGE CONFIG ---
st.set_page_config(page_title="PhishCatcher", layout="wide")

# --- 2. CUSTOM CSS (Replicating your HTML Styles) ---
st.markdown("""
    <style>
    .main-title {
        font-size: 32px;
        color: #FF0000;
        text-align: center;
        font-weight: bold;
        text-decoration: none;
    }
    .nav-bar {
        background: linear-gradient(90deg, #ff0066, #6600ff);
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        color: white;
        font-weight: bold;
    }
    .sub-header {
        font-size: 20px;
        color: #FF0000;
        text-align: center;
        font-weight: bold;
        margin: 20px 0;
    }
    .label-red {
        background-color: #FF0000;
        color: #FFFF00;
        padding: 5px;
        font-weight: bold;
        display: block;
    }
    .label-yellow {
        background-color: #FFFF00;
        color: #FF0000;
        padding: 5px;
        font-weight: bold;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. COMMON HEADER (Title & Banner) ---
st.markdown('<p class="main-title">PhishCatcher Client-Side Defense Against Web Spoofing Attacks Using Machine Learning</p>', unsafe_allow_html=True)

# Navigation simulation
st.markdown('<div class="nav-bar">Home | Remote User | Service Provider</div>', unsafe_allow_html=True)

try:
    st.image("assets/Banner.jpg", use_container_width=True)
except:
    st.warning("Please place 'Banner.jpg' in the assets folder.")

st.markdown('<p class="sub-header">Web spoofing, security and privacy, machine learning, web security, browser extension.</p>', unsafe_allow_html=True)

# --- 4. PAGE ROUTING (Login vs Register) ---
page = st.radio("Select Page", ["Login", "Register"], horizontal=True, label_visibility="collapsed")

if page == "Login":
    # --- LOGIN PAGE ---
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try: st.image("assets/login.jpg", width=150)
        except: pass
        
        st.markdown('<p style="font-size: 24px; color: #FF0000; text-align: center;">Login Using Your Account:</p>', unsafe_allow_html=True)
        
        with st.form("login_form"):
            u_name = st.text_input("User Name")
            u_pass = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
            if submitted:
                st.success(f"Welcome {u_name}!")

elif page == "Register":
    # --- REGISTER PAGE ---
    st.markdown('<p class="sub-header">REGISTER YOUR DETAILS HERE !!!</p>', unsafe_allow_html=True)
    
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        
        with c1:
            st.markdown('<span class="label-red">Enter Username</span>', unsafe_allow_html=True)
            st.text_input("User", label_visibility="collapsed")
            
            st.markdown('<span class="label-red">Enter EMail Id</span>', unsafe_allow_html=True)
            st.text_input("Email", label_visibility="collapsed")
            
            st.markdown('<span class="label-red">Enter Gender</span>', unsafe_allow_html=True)
            st.selectbox("Gen", ["Male", "Female"], label_visibility="collapsed")
            
            st.markdown('<span class="label-red">Enter Country Name</span>', unsafe_allow_html=True)
            st.text_input("Country", label_visibility="collapsed")

        with c2:
            st.markdown('<span class="label-yellow">Enter Password</span>', unsafe_allow_html=True)
            st.text_input("Pass", type="password", label_visibility="collapsed")
            
            st.markdown('<span class="label-yellow">Enter Address</span>', unsafe_allow_html=True)
            st.text_area("Addr", height=68, label_visibility="collapsed")
            
            st.markdown('<span class="label-yellow">Enter Mobile Number</span>', unsafe_allow_html=True)
            st.text_input("Mobile", label_visibility="collapsed")
            
            st.form_submit_button("Register")
