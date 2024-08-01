import openai
import streamlit as st
import pandas as pd

# Set your OpenAI API key
openai.api_key = '###'

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
st.write("Type your message and provide your user ID to get insights into your checking account.")
st.text_area("Bot:", "Hey Bestie!\nI'm Pac, your Capital One friend. I'm not a human, but I'm here to support you 24/7. Ask me a question about your savings progress, and I'll provide some motivation!")

# Input field for the user to type their question
user_input = st.text_input("You: ", "")

# Input field for the user to enter their user ID
user_id = st.number_input("Enter your user ID:", min_value=1, max_value=500, step=1)

# If both user input and user ID are provided
if user_input and user_id:
    # Determine the sentiment response based on the user ID
    sentiment_response = determine_sentiment(user_id)
    # Display the bot's response in a text area
    st.text_area("Bot:", value=sentiment_response, height=200)

# To run this app in your browser, use the following command in your terminal:
# streamlit run financial_chatbot.py