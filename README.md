# Crypto Sentiment Dashboard  
**Real-time AI-Powered Crypto News Sentiment Analysis**

A beautiful, fast, and fully responsive web dashboard that aggregates the latest cryptocurrency news from multiple trusted sources, analyzes the sentiment of each article using AI (TextBlob), and displays an interactive sentiment overview with live filtering and bilingual (Arabic / English) support.

Live Demo: https://crypto-sentiment-app-six.vercel.app/ *(example – deploy yours in seconds)*

## Features

- Real-time news aggregation from 7 major crypto sources (CoinDesk, CoinTelegraph, Decrypt, Bitcoin Magazine, CryptoSlate, CryptoPotato, CryptoNews)
- AI-powered sentiment analysis (Positive, Optimistic, Neutral, Pessimistic, Negative)
- Interactive Doughnut Chart (Chart.js) that updates dynamically
- Time-based filtering: Today • Last 3 Days • Last 7 Days • All News
- Auto-refresh toggle (every 5 minutes) with visual indicator
- Full bilingual support (العربية / English) with RTL/LTR switching
- Clean separation of concerns: HTML • CSS • JavaScript • Python utils
- Mobile-first, dark-themed, modern UI with smooth animations
- Cached responses (5-minute cache) for fast loading
- 100% open source & easy to deploy

## Project Structure

```
crypto-sentiment-dashboard/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── config.py                 # (Optional) Configuration
│
├── templates/
│   └── home.html             # Main page (clean HTML + Jinja2)
│
├── static/
│   ├── css/style.css         # Complete styling (dark theme, responsive)
│   └── js/script.js          # All frontend logic (lang, filter, chart, auto-refresh)
│
└── utils/
    ├── __init__.py
    ├── feeds.py              # RSS feed sources
    ├── sentiment.py          # Sentiment analysis & color mapping
    └── parsing.py            # Text cleaning & date parsing
```

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/crypto-sentiment-dashboard.git
cd crypto-sentiment-dashboard

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate    # Linux/Mac
# or
venv\Scripts\activate       # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Open your browser and go to: http://127.0.0.1:5000


## Technologies Used

- Backend: Flask (Python)
- Frontend: HTML5, CSS3, Vanilla JavaScript
- Chart: Chart.js
- Sentiment Analysis: TextBlob
- Parsing: feedparser, BeautifulSoup
- Caching: Flask-Caching

## Contributing

Contributions are welcome! Feel free to:
- Add new RSS feeds
- Improve sentiment accuracy (VADER, transformers, etc.)
- Add more languages
- Enhance UI/UX
- Add export to PDF/CSV

Just fork → make changes → submit a pull request.

## License

MIT License 

---

**Made with passion for the crypto community**  
Built by developers, for traders, analysts, and enthusiasts.

Give it a star if you like it!  
Feedback & suggestions are always appreciated.

Enjoy tracking the market mood in real time!

If you need any further help or have any other questions I will be happy to help.
## Contact
  avrmicrotech@gmail.com
