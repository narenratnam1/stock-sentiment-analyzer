# Real-Time Stock Sentiment Analyzer

**Live Demo:** [https://naren-sentiment-analyzer.onrender.com](https://naren-sentiment-analyzer.onrender.com)

![Stock Sentiment Analyzer Screenshot](https://placehold.co/800x400/1e293b/94a3b8?text=Stock%20Sentiment%20Analyzer)

## Overview

This is a full-stack web application that analyzes the real-time public sentiment of a given stock ticker. The Python backend connects to the X (formerly Twitter) API to pull live tweets, performs sentiment analysis on the text, and serves the aggregated data to a dynamic front-end. The front-end, built with vanilla JavaScript and Chart.js, visualizes the sentiment trend and includes a simulated AI prediction based on recent sentiment momentum.

This project demonstrates skills in back-end development with Python and Flask, front-end development, API integration, data processing, and cloud deployment.

## Features

- **Real-Time Data:** Fetches and analyzes the latest 50 tweets mentioning a specific stock ticker.
- **Sentiment Analysis:** Uses the VADER (Valence Aware Dictionary and sEntiment Reasoner) library to score the sentiment of each tweet.
- **Dynamic Visualization:** Displays the sentiment trend on an interactive chart using Chart.js.
- **Simulated AI Prediction:** Provides a simulated "Up," "Down," or "Stable" prediction based on the recent sentiment trend.
- **Cloud Deployed:** The Flask backend is fully deployed and running live on Render.

## Tech Stack

### Backend
- **Language:** Python
- **Framework:** Flask
- **API Integration:** Tweepy (for X API)
- **Sentiment Analysis:** VADER
- **Server:** Gunicorn

### Frontend
- **Frameworks:** Vanilla JavaScript, Chart.js
- **Styling:** Tailwind CSS

### Deployment
- **Platform:** Render
- **Version Control:** Git & GitHub

## How to Run Locally

To run this project on your own machine, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/narenratnam1/stock-sentiment-analyzer.git](https://github.com/narenratnam1/stock-sentiment-analyzer.git)
    cd stock-sentiment-analyzer
    ```

2.  **Set Up the Backend:**
    - Navigate to the backend directory:
      ```bash
      cd backend
      ```
    - Create and activate a Python virtual environment:
      ```bash
      python -m venv venv
      source venv/bin/activate  # On Mac/Linux
      # .\venv\Scripts\activate  # On Windows
      ```
    - Install the required dependencies:
      ```bash
      pip install -r requirements.txt
      ```
    - Create a `.env` file in the `backend` directory and add your X API Bearer Token:
      ```
      TWITTER_BEARER_TOKEN=YOUR_BEARER_TOKEN_GOES_HERE
      ```

3.  **Run the Server:**
    - With your virtual environment active and in the `backend` folder, run the Flask app:
      ```bash
      python app.py
      ```
    - The application will be available at `http://localhost:5000`.