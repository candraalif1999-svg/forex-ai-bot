# news.py
import feedparser

def get_market_news():
    feed = feedparser.parse("https://www.forexlive.com/rss.xml")
    keywords = [
        "cpi", "nfp", "fomc", "gdp", "inflation", 
        "employment", "rate decision", "central bank", "job report"
    ]
    news_list = []
    for entry in feed.entries[:10]:
        title = entry.title.lower()
        if any(kw in title for kw in keywords):
            # Deteksi sentimen sederhana
            if any(word in title for word in ["rise", "strong", "gain", "beat"]):
                sentiment = "positive"
            elif any(word in title for word in ["fall", "weak", "drop", "miss"]):
                sentiment = "negative"
            else:
                sentiment = "neutral"
                
            news_list.append({
                "title": entry.title,
                "url": entry.link,
                "sentiment": sentiment
            })
    return news_list[:3]
