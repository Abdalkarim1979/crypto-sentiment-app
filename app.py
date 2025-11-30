from flask import Flask, render_template, request
from flask_caching import Cache
import datetime
from utils.feeds import crypto_feeds
from utils.sentiment import analyze_sentiment, get_sentiment_color
from utils.parsing import get_clean_summary, parse_date

app = Flask(__name__)
cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
cache.init_app(app)

@app.route("/")
@cache.cached(timeout=300)
def home():
    from utils.sentiment import analyze_sentiment  # تأخير الاستيراد لتجنب circular import إن وُجد
    all_news = []
    sentiment_counts = {"Positive": 0, "Optimistic": 0, "Neutral": 0, "Pessimistic": 0, "Negative": 0}
    empty_sources = []
    total_articles = 0
    import feedparser

    for source, url in crypto_feeds.items():
        try:
            feed = feedparser.parse(url)
            if feed.bozo or not feed.entries:
                empty_sources.append(source)
                continue

            articles_from_source = 0
            for entry in feed.entries[:10]:
                try:
                    title = entry.get("title", "No title")
                    summary_html = entry.get("summary", entry.get("description", ""))
                    link = entry.get("link", "#")
                    summary_text = get_clean_summary(summary_html)
                    sentiment, polarity, emoji = analyze_sentiment(title, summary_text)
                    
                    published_date = entry.get("published", "")
                    published_datetime = parse_date(published_date)
                    display_date = published_date if published_date.lower() == "unknown date" else published_datetime.strftime("%Y-%m-%d %H:%M") if published_datetime != datetime.datetime.min else "Unknown date"

                    sentiment_counts[sentiment] += 1
                    total_articles += 1
                    articles_from_source += 1

                    all_news.append({
                        "source": source,
                        "title": title,
                        "summary": summary_text,
                        "link": link,
                        "sentiment": sentiment,
                        "emoji": emoji,
                        "polarity": round(polarity, 3),
                        "published": display_date,
                        "published_datetime": published_datetime,
                        "color": get_sentiment_color(sentiment)
                    })
                except:
                    continue

            if articles_from_source == 0:
                empty_sources.append(source)

        except:
            empty_sources.append(source)

    all_news.sort(key=lambda x: x["published_datetime"], reverse=True)

    return render_template(
        "home.html",
        news=all_news,
        counts=sentiment_counts,
        empty_sources=empty_sources,
        total_articles=total_articles,
        current_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        active_sources=[s for s in crypto_feeds.keys() if s not in empty_sources]
    )

@app.route("/clear-cache")
def clear_cache():
    cache.clear()
    return "Cache cleared!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)