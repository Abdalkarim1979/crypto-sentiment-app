from textblob import TextBlob

def analyze_sentiment(title, summary):
    text = f"{title} {summary}"
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0.2:
        return "Positive", polarity, "😊"
    elif polarity > 0.1:
        return "Optimistic", polarity, "🙂"
    elif polarity < -0.2:
        return "Negative", polarity, "😞"
    elif polarity < -0.1:
        return "Pessimistic", polarity, "😕"
    else:
        return "Neutral", polarity, "😐"

def get_sentiment_color(sentiment):
    colors = {
        "Positive": "linear-gradient(135deg, #00b09b, #96c93d)",
        "Optimistic": "linear-gradient(135deg, #a8ff78, #78ffd6)",
        "Neutral": "linear-gradient(135deg, #ffd89b, #19547b)",
        "Pessimistic": "linear-gradient(135deg, #ff9a9e, #fecfef)",
        "Negative": "linear-gradient(135deg, #ff6b6b, #ee5a24)"
    }
    return colors.get(sentiment, "linear-gradient(135deg, #74b9ff, #0984e3)")