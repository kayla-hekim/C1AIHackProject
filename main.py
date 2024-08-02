import matplotlib
matplotlib.use('Agg')

from flask import Flask, render_template, jsonify, request
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Mock data
savings_data = {
    "goal": 1000,
    "saved": 600,
    "committed": 200,
    "date": "2024-06-01"
}

@app.route('/')
def index():
    fig, ax = plt.subplots()
    labels = ['Saved', 'Committed', 'Remaining']
    sizes = [savings_data["saved"], savings_data["committed"], savings_data["goal"] - savings_data["saved"] - savings_data["committed"]]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
    return render_template('index2.html', data=savings_data, chart_img=img_base64)

@app.route('/index2')
def overview():
    fig, ax = plt.subplots()
    labels = ['Saved', 'Committed', 'Remaining']
    sizes = [savings_data["saved"], savings_data["committed"], savings_data["goal"] - savings_data["saved"] - savings_data["committed"]]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
    # print("working")
    return render_template('index2.html', chart_img=img_base64, data=savings_data)

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/motivate', methods=['POST'])
def motivate():
    user_input = request.json.get('message')
    response = "Keep going! You're doing great!"  # Simple motivational response
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)