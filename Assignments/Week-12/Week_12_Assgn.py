import requests
import json

endpoint = "https://mynewresourse.cognitiveservices.azure.com/"
api_key = ""
# Deleted APi Key for Security Purpose.

# Headers for the API request
headers = {
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def analyze_sentiment(text):
    # API URL for sentiment analysis
    sentiment_url = f"{endpoint}/text/analytics/v3.1/sentiment"

    # Request body
    documents = {
        "documents": [
            {"id": "1", "language": "en", "text": text}
        ]
    }

    # Make the API request
    response = requests.post(sentiment_url, headers=headers, json=documents)
    response_json = response.json()

    # Extract sentiment score
    if response.status_code == 200:
        sentiment = response_json['documents'][0]['sentiment']
        confidence_scores = response_json['documents'][0]['confidenceScores']
        return sentiment, confidence_scores
    else:
        raise Exception(f"Request failed: {response.status_code}, {response_json}")

# Example usage
if __name__ == "__main__":
    review = "The movie was fantastic! The plot was gripping and the characters were well-developed."
    sentiment, confidence_scores = analyze_sentiment(review)
    print(f"Sentiment: {sentiment}")
    print(f"Confidence Scores: {confidence_scores}")
