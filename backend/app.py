import os
import tweepy
from flask import Flask, render_template, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv

# --- SETUP ---
load_dotenv() # Load environment variables from .env file

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

# --- API KEYS & CONFIG ---
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

if not bearer_token or bearer_token == 'YOUR_BEARER_TOKEN_GOES_HERE':
    raise Exception("FATAL ERROR: Twitter Bearer Token not found or not replaced in .env file.")

client = tweepy.Client(bearer_token)

# --- ROUTES ---

# This route serves the front-end HTML page
@app.route('/')
def index():
    return render_template('index.html')


# This is our main API endpoint
@app.route('/analyze')
def analyze_sentiment():
    ticker = request.args.get('ticker')
    if not ticker:
        return jsonify({"error": "Stock ticker is required."}), 400

    print(f"Analyzing sentiment for: ${ticker}")

    try:
        # 1. Search for recent tweets using Tweepy
        query = f'"${ticker}" lang:en -is:retweet'
        response = client.search_recent_tweets(query, max_results=50)
        
        tweets = response.data
        if not tweets:
            return jsonify({"error": f"No recent tweets found for ticker: {ticker}. Try another one."}), 404

        # 2. Analyze the sentiment of each tweet using VADER
        sentiment_scores = []
        for tweet in tweets:
            # VADER returns a dictionary with neg, neu, pos, and compound scores
            vs = analyzer.polarity_scores(tweet.text)
            # The 'compound' score is a normalized, single metric for sentiment
            sentiment_scores.append(vs['compound'])
        
        # 3. Structure the data for the chart
        # We reverse the scores because the Twitter API returns the newest tweets first
        sentiment_scores.reverse()
        chart_data = [{"time": i, "score": score} for i, score in enumerate(sentiment_scores)]

        print(f"Successfully analyzed {len(tweets)} tweets.")
        # 4. Send the data back to the front-end
        return jsonify({"ticker": ticker, "data": chart_data})

    except Exception as e:
        print(f"Error fetching or analyzing tweets: {e}")
        return jsonify({"error": "Failed to fetch or analyze data from the Twitter API."}), 500

# --- START THE SERVER ---
if __name__ == '__main__':
    app.run(debug=True, port=5000)