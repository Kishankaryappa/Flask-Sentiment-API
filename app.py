from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()  # Get the user message from the request
    message = data['message']
    
    # Perform sentiment analysis using TextBlob
    analysis = TextBlob(message)
    sentiment_polarity = analysis.sentiment.polarity

    # Determine if sentiment is positive, negative, or neutral
    if sentiment_polarity > 0:
        sentiment = 'positive'
    elif sentiment_polarity < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    # Return the result as a JSON response
    return jsonify({
        'message': message,
        'sentiment': sentiment
    })

if __name__ == '__main__':
    app.run(debug=True)
