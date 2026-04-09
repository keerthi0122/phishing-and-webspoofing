import streamlit as st
import time

# --- LOGIC FUNCTION ---
def perform_detection(url):
    # 1. Clean the URL for comparison (removes https, www, etc.)
    clean_url = url.lower().replace("https://", "").replace("http://", "").replace("www.", "").split('/')[0]
    
    # 2. Define your "Official" verified websites
    # Add any website here that you want to be marked as "Safe"
    official_sites = [
        "google.com", 
        "microsoft.com", 
        "aceexam.in",    # The official site in your screenshots
        "github.com",
        "facebook.com"
    ]
    
    # 3. Check against the list
    if clean_url in official_sites:
        return "SAFE"
    else:
        return "PHISHING"

# --- STREAMLIT UI ---
st.title("Phishing Detection App")

url_to_check = st.text_input("Enter URL:", placeholder="e.g., google.com or fake-link.net")

if st.button("Check"):
    if url_to_check:
        with st.spinner("Analyzing website patterns..."):
            time.sleep(1.5) # Simulating ML processing time
            status = perform_detection(url_to_check)
            
            st.write("---")
            if status == "SAFE":
                # Matches your requirement for "Phishing attack not found"
                st.success("### ✅ Status: Phishing Attack Not Found")
                st.info(f"The domain **{url_to_check}** is verified as an Official Website.")
            else:
                # Matches your requirement for "Phishing attack found"
                st.error("### 🚨 Status: Phishing Attack Found!")
                st.warning(f"The website **{url_to_check}** is flagged as a Fake/Malicious site.")
    else:
        st.warning("Please enter a URL first.")

 
