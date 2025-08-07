# app.py (Final Enhanced Version of CraveDecode)

import streamlit as st
import sqlite3
from datetime import date
from utils import init_db, insert_log, fetch_weekly_data, fetch_summary_stats
import plotly.express as px
from chatbot import get_bot_response, chat_memory

st.set_page_config(page_title="CraveDecode - Track Your Cravings & Mood", layout="centered")
st.markdown("""
<style>
    .main {
        background-color: #fff5f5;
    }
    .stButton > button {
        background-color: #ff6f91;
        color: white;
        font-weight: bold;
    }
    .stTextInput > div > input {
        background-color: #fff0f5;
    }
</style>
""", unsafe_allow_html=True)

init_db()

st.title("🍓 CraveDecode: Decode Your Cravings, Elevate Your Mood")

st.markdown("""
### 🧠 What are Cravings?
Cravings can be a signal from our body — due to nutritional needs, emotional triggers, or habits.
They often reflect deeper imbalances related to mood, hydration, and daily lifestyle choices.

**Your cravings + mood + lifestyle = Your health roadmap.**
Let's explore it together 👇
""")

# ----- DAILY CHECK-IN -----
st.header("📋 Let’s check what you crave and how you feel today")

today = date.today()
craving = st.selectbox("🥑 What do you crave?", [
    "Sweet", "Salty", "Crunchy", "Spicy", "Cheese", "Chocolate", "Carbs", "No craving"
])
hunger_type = st.radio("🍽️ Type of hunger?", ["Stomach", "Emotional", "Habit", "Thirst", "None"])
mood = st.select_slider("🧘 Mood right now", ["😞 Sad", "😐 Neutral", "😊 Happy"])
water = st.slider("💧 How much water did you drink (L)?", 0.0, 5.0, 2.0, 0.5)

craving_insights = {
    "Sweet": "🍬 Sweet cravings: Try fruits or cinnamon tea (linked to chromium or stress).",
    "Salty": "🧂 Salty cravings: May need sodium. Try olives, soup, or salted nuts.",
    "Cheese": "🧀 Cheese craving = possible calcium deficiency. Try spinach or yogurt.",
    "Chocolate": "🍫 Chocolate? Might be magnesium-related. Try bananas or almonds.",
    "Crunchy": "🥜 Crunchy cravings often signal stress. Try roasted chickpeas!",
    "Spicy": "🌶️ Spicy food may reflect stimulation-seeking. Balance with hydration.",
    "Carbs": "🍞 Carb cravings could relate to serotonin dips. Choose whole grains!",
}

if craving in craving_insights:
    st.info(craving_insights[craving])

if st.button("🚀 Submit My Day"):
    insert_log(today, craving, hunger_type, mood, water)
    st.success("✅ Entry logged! You're building self-awareness 💪")

# ----- WEEKLY REPORT -----
st.header("📊 Weekly Analysis")
data = fetch_weekly_data()

if data:
    fig = px.pie(names=[d[0] for d in data], values=[d[1] for d in data], title="Your Craving Patterns (7 Days)")
    st.plotly_chart(fig)

    avg_water, entry_count, happy_days = fetch_summary_stats()

    st.markdown(f"""
### 🎯 Your Score Summary:
- **Logged Days:** {entry_count} 📆
- **Avg. Water Intake:** {avg_water:.1f} L/day 💧
- **Happy Mood Days:** {happy_days} 😊

### 🧠 Improvements You Can Try:
- Stay hydrated to reduce unnecessary cravings
- Add breathing/yoga to handle emotional eating
- Use healthy snack swaps
- Track your hunger source daily
""")
else:
    st.warning("You need at least 7 entries to generate a weekly report 💙")

# ----- CHATBOT ----
from chatbot import get_bot_response, chat_memory
st.header("💬 Ask Cravy (Your Chatbot Guide)")

with st.form("chat_form", clear_on_submit=True):
    user_message = st.text_input("You:", placeholder="e.g. What causes chocolate cravings?")
    submitted = st.form_submit_button("Send")

if submitted and user_message:
    bot_reply = get_bot_response(user_message)
    chat_memory.append(("You", user_message))
    chat_memory.append(("Cravy", bot_reply))

for speaker, msg in chat_memory:
    st.markdown(f"**{speaker}**: {msg}")

# ----- ENDING FOOTER -----
st.markdown("""
---
### 🌟 Thanks for using CraveDecode!
If you have any doubts about cravings or moods, feel free to write to us:
📧 **cravedecode@wellnesshub.com**

🔁 Share your feedback & rate us:
⭐⭐⭐⭐⭐

Made with ❤️ for self-awareness & wellness.
""")
