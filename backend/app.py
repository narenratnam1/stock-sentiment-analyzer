import os
import tweepy
from flask import Flask, render_template, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv

# --- SETUP ---
load_dotenv()
app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

# --- API KEYS & CONFIG ---
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
if not bearer_token or bearer_token == 'YOUR_BEARER_TOKEN_GOES_HERE':
    raise Exception("FATAL ERROR: Twitter Bearer Token not found.")
client = tweepy.Client(bearer_token)

# --- ROUTES ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze')
def analyze_sentiment():
    ticker = request.args.get('ticker')
    if not ticker:
        return jsonify({"error": "Stock ticker is required."}), 400

    print(f"Analyzing sentiment for: ${ticker}")

    try:
        query = f'"${ticker}" lang:en -is:retweet'
        response = client.search_recent_tweets(query, max_results=50)
        tweets = response.data

        if not tweets:
            return jsonify({"error": f"No recent tweets found for ticker: {ticker}."}), 404

        sentiment_scores = []
        for tweet in tweets:
            vs = analyzer.polarity_scores(tweet.text)
            sentiment_scores.append(vs['compound'])

        sentiment_scores.reverse()
        chart_data = [{"time": i, "score": score} for i, score in enumerate(sentiment_scores)]

        print(f"Successfully analyzed {len(tweets)} tweets.")
        return jsonify({"ticker": ticker, "data": chart_data})

    except Exception as e:
        print(f"Error fetching or analyzing tweets: {e}")
        return jsonify({"error": "Failed to fetch data from the Twitter API."}), 500

# --- START THE SERVER ---
if __name__ == '__main__':
    app.run(debug=True, port=5000)