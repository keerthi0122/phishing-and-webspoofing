import streamlit as st
import time

# --- 1. Logic Function ---
def check_url_status(url):
    # Clean the URL to check the domain (e.g., "https://google.com/login" -> "google.com")
    url = url.lower().replace("https://", "").replace("http://", "").split('/')[0]
    
    # Define your "Official" safe websites
    official_websites = [
        "google.com", 
        "microsoft.com", 
        "amazon.com", 
        "facebook.com", 
        "aceexam.in",    # Adding the site from your screenshot
        "github.com"
    ]
    
    # Logic: If it's in the official list, it's NOT a phishing attack
    if url in official_websites:
        return "Not Found"
    else:
        return "Found"

# --- 2. Streamlit UI ---
st.title("Phishing Detection App")

url_input = st.text_input("Enter URL to scan:", placeholder="e.g., google.com or fake-site.net")

if st.button("Check"):
    if url_input:
        with st.status("Scanning website...", expanded=False) as status:
            time.sleep(1.5) # Simulate processing
            result = check_url_status(url_input)
            status.update(label="Scan Complete!", state="complete")

        # --- 3. Displaying the Result based on your requirement ---
        st.write("---")
        if result == "Not Found":
            st.success("### ✅ Status: Phishing Attack Not Found")
            st.info(f"The website **{url_input}** is verified as an official domain.")
        else:
            st.error("### 🚨 Status: Phishing Attack Found!")
            st.warning(f"The website **{url_input}** is flagged as a potential fake or malicious site.")
    else:
        st.warning("Please enter a URL first.")
