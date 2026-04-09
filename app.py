import streamlit as st
import time

# --- Dummy ML Function ---
def is_phishing(url):
    time.sleep(1) # Simulating processing time
    # This logic is for testing; replace with your actual model logic
    if "google.com" in url.lower() or "microsoft.com" in url.lower():
        return False
    return True

st.title("Phishing Detection App")
url_input = st.text_input("Enter URL")

if st.button("Check"):
    if url_input:
        with st.spinner('Analyzing URL...'):
            result = is_phishing(url_input)
            
            # Creating a clean container for the result
            st.write("---")
            if result:
                st.error("### 🚨 Phishing Attack Detected: YES")
                st.info("This URL matches patterns found in malicious sites.")
            else:
                st.success("### ✅ Phishing Attack Detected: NO")
                st.info("This URL appears to be safe.")
    else:
        st.warning("Please enter a URL first.")
