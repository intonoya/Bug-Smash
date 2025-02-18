from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Simulated ML prediction model
def model_predict(click_location):
    # A simple "model" that checks if the click is in the right place
    if click_location in "valid_click_area":
        return "bug_smashed"
    return "no_bug"

# In-memory leaderboard (for simplicity)
leaderboard = []

@app.route('/')
def home():
    return 'Welcome to Bug Smash!'

@app.route('/smash', methods=['POST'])
def smash():
    data = request.get_json()
    prediction = model_predict(data['action'])  # Simulated ML prediction
    if prediction == 'bug_smashed':
        return jsonify({'message': 'Bug smashed!'})
    return jsonify({'message': 'No bug detected! Try again.'})

@app.route('/leaderboard', methods=['GET'])
def leaderboard_view():
    # Sort leaderboard by score in descending order
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)
    return jsonify(sorted_leaderboard)

@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.get_json()
    leaderboard.append(data)
    return jsonify({'message': 'Score submitted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
