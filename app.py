import streamlit as st
import time

# --- 1. Simulation Function (Replace this with your ML model later) ---
def is_phishing(url):
    # This simulates a delay for "Checking..."
    time.sleep(2) 
    # Dummy logic: if url contains "google", it's safe; otherwise, alert.
    if "google" in url.lower():
        return False
    return True

# --- 2. UI Layout ---
st.title("Phishing Detection App")

url_input = st.text_input("Enter URL", placeholder="example.com")

if st.button("Check"):
    if url_input:
        # Show a status message while processing
        with st.status("Checking URL...", expanded=True) as status:
            result = is_phishing(url_input)
            
            if result:
                st.error(f"⚠️ ALERT: {url_input} is likely a PHISHING site!")
            else:
                st.success(f"✅ SUCCESS: {url_input} appears to be SAFE.")
            
            status.update(label="Check Complete!", state="complete", expanded=False)
    else:
        st.warning("Please enter a URL first.")
