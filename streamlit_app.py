import streamlit as st
import requests
from datetime import datetime, date, time

API_URL = "http://localhost:8000/insight"

st.set_page_config(
    page_title="Astrological Insight Generator",
    page_icon="🔮",
    layout="centered"
)

st.title("🔮 Astrological Insight Generator")
st.write("Get your daily personalized astrological reading.")

st.markdown("---")

# ===== INPUT FORM ===== #
with st.form("insight_form"):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Your Name", placeholder="Name")
        birth_date = st.date_input("Birth Date",min_value=date(1900, 1, 1),
        max_value=date.today())

    with col2:
        birth_time = st.time_input("Birth Time (optional)", value=time(12, 0))
        birth_place = st.text_input("Birth Place", placeholder="Birth location")

    language = st.selectbox(
        "Language",
        ["en", "hi"],
        index=0,
        format_func=lambda x: "English" if x == "en" else "Hindi"
    )

    date_for = st.date_input("Insight for Date", value=date.today(),min_value=date(1900, 1, 1),
        max_value=date.today())

    submitted = st.form_submit_button("✨ Generate Astrological Insight")

# ===== API CALL ===== #
if submitted:
    if not name:
        st.error("Please enter your name.")
        st.stop()

    payload = {
        "name": name,
        "birth_date": birth_date.isoformat(),
        "birth_time": birth_time.strftime("%H:%M"),
        "birth_place": birth_place,
        "language": language,
        "date_for": date_for.isoformat()
    }

    with st.spinner("Generating your personalized insight..."):
        try:
            res = requests.post(API_URL, json=payload)

            if res.status_code != 200:
                st.error(f"Error: {res.json().get('detail', 'Unknown error')}")
            else:
                data = res.json()

                st.markdown("---")
                st.subheader(f"♌ Zodiac: **{data['zodiac']}**")

                st.success(data["insight"])

                st.caption(f"Language: {data['language'].upper()}")
                st.caption(f"Date For: {data['date_for']}")
                st.caption(f"Personalization Score: {data['personalization_score']:.2f}")

        except Exception as e:
            st.error(f"Could not reach API: {e}")

