import openai
from flask import Flask, request, jsonify, render_template
import pandas as pd
import random

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'enterkeyhere'

# Load the CSV file
df = pd.read_csv('Corrected_Bank_Transactions_Data.csv')

# Enhanced function to determine sentiment based on savings goal fulfillment
def determine_sentiment(user_id):
    user_data = df[df['id'] == user_id]
    if not user_data.empty:
        if user_data['goal_fulfilled'].values[0] == 1:
            positive_responses = [
                "Fantastic job! You're doing so great! Keep up the amazing work.",
                "Awesome! I'm so proud of you. Your dedication is paying off!",
                "Great job meeting your savings goal! You're on the right track.",
                "You're doing excellent! Keep up the great work and continue saving."
            ]
            return random.choice(positive_responses)
        else:
            motivational_responses = [
                "Don't worry, you'll get there! Keep focusing on your goal.",
                "You haven't met your goal yet, but I believe in you. Keep trying!",
                "Stay positive and keep pushing forward. You can do it!",
                "Keep your head up! You're capable of amazing things, just keep trying."
            ]
            return random.choice(motivational_responses)
    else:
        return "User ID not found. Please check your ID and try again."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data['user_input']
    user_id = data['user_id']
    
    # Your logic to generate a response based on user_input and user_id
    response = determine_sentiment(user_id)
    
    return jsonify(response=response)

if __name__ == '__main__':
    app.run(debug=True)
