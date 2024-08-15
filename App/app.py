import streamlit as st
from groq import Groq

def generate(api_key, fasting, pre_meal, post_meal, dietary_pref ):
    client = Groq(
        api_key=api_key,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"""
                            Based on the provided inputs:
                            - Fasting Sugar Level: {fasting} mg/dL
                            - Pre-meal Sugar Level: {pre_meal} mg/dL
                            - Post-meal Sugar Level: {post_meal} mg/dL
                            - Dietary Preferences: {dietary_pref}
                            
                            You are acting as a world class nutritionist and specialize in diabetes disease. Please provider a personalized diet plan according to above conditions.
                            """,
            }
        ],
        model="llama3-8b-8192",
    )

    return (chat_completion.choices[0].message.content)

api_key = st.secrets["GROQ_API_KEY"]

# Set up the page configuration
st.set_page_config(
    page_title="Mealian Guide",
    page_icon=":shield:",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Apply blue theme for the sidebar
st.markdown(
    """
    <style>
    .css-1d391kg {
        background-color: #007BFF;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("Health Inputs")
    fasting_sugar = st.number_input("Fasting Sugar Level (mg/dL)", min_value=0, max_value=500, value=100)
    pre_meal_sugar = st.number_input("Pre-meal Sugar Level (mg/dL)", min_value=0, max_value=500, value=100)
    post_meal_sugar = st.number_input("Post-meal Sugar Level (mg/dL)", min_value=0, max_value=500, value=100)
    dietary_pref = st.text_input("Dietary Preferences", placeholder="e.g., High protein, Vegetarian")
    generate_button = st.button("Generate")

# Centered title and description
st.markdown("<h1 style='text-align: center;'>Velo Guardian</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center;'>Your personalized health monitor and meal plan generator. Enter your sugar levels and dietary preferences to get customized recommendations.</p>",
    unsafe_allow_html=True,
)

st.divider()
# Placeholder for the LLM response
if generate_button:
    response = generate(api_key, fasting_sugar, pre_meal_sugar, post_meal_sugar, dietary_pref)
    st.markdown(response)
