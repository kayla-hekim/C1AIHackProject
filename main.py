# import openai
from flask import Flask, request, jsonify, render_template
import pandas as pd
import random

app = Flask(__name__)

# # Set your OpenAI API key
# openai.api_key = 'key'

# Load the CSV file
df = pd.read_csv('Corrected_Bank_Transactions_Data.csv')

# Enhanced function to determine sentiment based on savings goal fulfillment
def determine_sentiment(user_id):
    print(user_id)
    print(df)
    user_data = df[df['id'] == int(user_id)]
    print(user_data)
    if not user_data.empty:
        if user_data['goal_fulfilled'].values[0] == 1:
            positive_responses = [
                "Guess what: You've reached your goal! Fantastic job! You're doing so great! Keep up the amazing work and make another goal.",
                "You've done it, bestie! You've reached your goal, awesome! I'm so proud of you. Your dedication is paying off! You should totally make another goal.",
                "I'm gonna praise you. Great job meeting your savings goal! You're on the right track. Continue that track by creating another goal.",
                "Another goal has been MET! You're doing excellent and should create another goal. Keep up the great work and continue saving."
            ]
            return random.choice(positive_responses)
        else:
            motivational_responses = [
                "You haven't met your goal, bestie. But, don't worry, you'll get there! Here is your affirmation: You are smart. You are the best saver. No one saves quite like you.",
                "You haven't met your goal yet, but I believe in you. Keep trying! Here is an affirmation: I'm in awe of all you do. Has anyone told you how much progress you've made? Because it's a LOT of progress!",
                "Unfortunately, the goal hasn't been met, my friend. Stay positive and keep pushing forward. Here's an affirmation: You are a disciplined saver, and your efforts are paying off.",
                "Sorry, bestie, but your goal hasn't been met. Keep your head up! Here's your affirmation: You're capable of amazing things. Your saving habits are a testament to your strong will and determination.."
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
