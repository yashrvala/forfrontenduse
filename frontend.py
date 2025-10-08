import requests
import streamlit as st
import time

st.title("Mobile/Web App Cost Estimator Bot By Teqto Infotech!!💻")
st.write("Want an estimate for a mobile app or web application? I’ll ask a few quick questions. Give me Proper Response i will Give you Proper Outcome!!🤖")

app_type = st.selectbox("Platform?", ["iOS native", "Android native", "Cross-platform (Flutter/React Native)", "Progressive Web App", "Web app"])

user_type = st.selectbox("Who will use this app?", ["Internal", "Customers", "Both"])

user_estimate = st.selectbox("Estimated number of users in year 1?", ["0–1k", "1k–10k", "10k–100k", "100k+"])

auth_type = st.selectbox("Do you need user accounts and roles?", ["Yes — roles: admin/editor/user", "Simple login", "No"])

numof_screens = st.selectbox("How many core screens?", ["1–5", "6–15", "16–30", "30+"])
wireframes = st.file_uploader("Upload wireframes or designs (optional)")

features = st.multiselect("Core features", ["Authentication", "Social login", "Push notifications", "Offline mode", "Geolocation", "In-app payments",
     "Camera", "AR", "Chat", "Video calls", "Real-time updates (Websockets)", "Reporting dashboards", "Admin panel"]
)

backend = st.radio("Do you need a custom backend & API?", ["Yes", "Use existing", "Serverless"])

integrations = st.multiselect("Third-party services & integrations", ["CRM", "Payment gateways", "Firebase", "AWS", "Google Maps", "Twilio", "Analytics"])

store_support = st.radio("Need store publishing support?", ["Yes — we can publish", "No — we’ll publish"])

qa = st.radio("Need manual QA / automated tests / both?", ["Manual", "Automated", "Both"])

maintenance = st.radio("Expect to scale rapidly? Need 24/7 support?", ["Yes", "No"])

timeline = st.selectbox("Timeline?", ["< 1 month", "1–3 months", "3–6 months", "6+ months"])
budget_range = st.selectbox("Budget range?", ["< $5k", "$5k–$15k", "$15k–$50k", "$50k+"])

#contact information
st.subheader("📇 Contact Information")

name = st.text_input("Full Name ")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number (optional)")

# if not name or not email:
#     st.warning("Please enter your name and email to receive your estimate.")

st.subheader("🧾 Summary & Preliminary Estimate")

if st.button("Get Estimate"):
    payload = {
        "app_type": app_type,
        "user_type": user_type,
        "user_estimate": user_estimate,
        "auth_type": auth_type,
        "numof_screens": numof_screens,
        "features": features,
        "backend": backend,
        "integrations": integrations,
        "store_support": store_support,
        "qa": qa,
        "maintenance": maintenance,
        "timeline": timeline,
        "budget_range": budget_range
    }

    # Call Flask API
    backend_url = "https://appcost-backendd.onrender.com/estimate"  

for i in range(10):
    try:
        response = requests.post(backend_url, json=payload, timeout=10)  
        response.raise_for_status()  
        data = response.json()
        st.markdown(data.get("estimate", "No estimate returned."))
        st.info(data.get("explanation", ""))
        break
    except requests.exceptions.RequestException as e:
        st.warning(f"Waiting for backend... ({i+1}/10) | Error: {e}")
        time.sleep(2)
    except ValueError:
        st.warning(f"Invalid response from backend. Retrying... ({i+1}/10)")
        time.sleep(2)
else:
    st.error("Backend not responding. Please try again later.")
