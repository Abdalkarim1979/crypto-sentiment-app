from bs4 import BeautifulSoup
import datetime

def get_clean_summary(summary_html):
    if not summary_html:
        return "No summary available"
    
    soup = BeautifulSoup(summary_html, "html.parser")
    clean_text = soup.get_text().strip()
    clean_text = ' '.join(clean_text.split())
    
    if len(clean_text) > 250:
        clean_text = clean_text[:250] + "..."
    
    return clean_text

def parse_date(date_string):
    if not date_string:
        return datetime.datetime.min
    
    formats = [
        "%a, %d %b %Y %H:%M:%S %Z",
        "%a, %d %b %Y %H:%M:%S %z",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d"
    ]
    
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_string, fmt)
        except:
            continue
    
    return datetime.datetime.min