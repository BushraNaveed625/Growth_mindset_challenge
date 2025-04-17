import streamlit as st
import random
import pandas as pd
from datetime import datetime

quotes = [
    "Mistakes are proof that you're trying.",
    "Every challenge is an opportunity to grow.",
    "Progress, not perfection.",
    "Difficult roads often lead to beautiful destinations.",
    "Your brain is like a muscle — the more you use it, the stronger it gets!"
]

st.set_page_config(page_title="Growth Mindset Tracker", layout="centered")


st.title("🌱 Growth Mindset Tracker")
st.markdown("Log your daily challenges and track your progress.")


with st.form("log_form"):
    challenge = st.text_area("🧠 What challenge did you face today?")
    approach = st.text_area("🛠️ How did you tackle the challenge?")
    lesson = st.text_area("🎓 What did you learn from it?")
    difficulty = st.slider("📊 How difficult was it?", 1, 5, 3)
    persistence = st.slider("🔥 How persistent were you?", 1, 5, 3)
    submitted = st.form_submit_button("Log Reflection")

if "log" not in st.session_state:
    st.session_state.log = []


if submitted and challenge.strip():
    entry = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Challenge": challenge,
        "Approach": approach,
        "Lesson": lesson,
        "Difficulty": difficulty,
        "Persistence": persistence
    }
    st.session_state.log.append(entry)
    st.success("✅ Reflection logged!")

   
    with st.expander("📌 View your logged reflection"):
        st.markdown(f"**🗓️ Date:** {entry['Date']}")
        st.markdown(f"**🧠 Challenge:** {entry['Challenge']}")
        st.markdown(f"**🛠️ Approach:** {entry['Approach']}")
        st.markdown(f"**🎓 Lesson:** {entry['Lesson']}")
        st.markdown(f"**📊 Difficulty:** {entry['Difficulty']}")
        st.markdown(f"**🔥 Persistence:** {entry['Persistence']}")


if st.session_state.log:
    st.subheader("🗂️ All Logged Reflections")
    df = pd.DataFrame(st.session_state.log)
    st.dataframe(df, use_container_width=True)

st.markdown("### 🌟 Growth Mindset Quote")
st.info(random.choice(quotes))

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
