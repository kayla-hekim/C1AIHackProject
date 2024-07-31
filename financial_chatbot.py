import openai
import streamlit as st
import pandas as pd

# Set your OpenAI API key
openai.api_key = 'API-key######FORLATER'

# Load the CSV file
df = pd.read_csv('Corrected_Bank_Transactions_Data.csv')  # Updated to a relative path

# Function to determine sentiment based on savings goal fulfillment
def determine_sentiment(user_id):
    user_data = df[df['id'] == user_id]
    if not user_data.empty:
        if user_data['goal_fulfilled'].values[0] == 1:
            return "You're doing so great! I'm so proud of you my friend."
        else:
            return ("Bestie, you haven't met your goal yet. I'm going to give you words of motivation "
                    "and affirmation. You are the saver. No one will save like you because you're going "
                    "to prioritize this goal. You will NOT spend on unnecessary items in the future.")
    else:
        return "User ID not found. Please check your ID and try again."

# Streamlit UI
st.title("Financial Advisor Chatbot")
st.write("Type your message and provide your user ID to get insights into your checkings account.")

user_input = st.text_input("You: ", "")
user_id = st.number_input("Enter your user ID:", min_value=1, max_value=500, step=1)

if user_input and user_id:
    sentiment_response = determine_sentiment(user_id)
    st.text_area("Bot:", value=sentiment_response, height=200)
