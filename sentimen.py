# sentiment.py
import random

def analyze_sentiment():
    sentiments = [
        " pasar saat ini **bullish** karena data ekonomi AS kuat dan ekspektasi kenaikan suku bunga Fed tertunda.",
        " pasar menunjukkan sentimen **netral**, menunggu keputusan FOMC dan rilis NFP pekan depan.",
        " pasar cenderung **bearish** setelah CPI lebih tinggi dari perkiraan, memicu ekspektasi hawkish Fed."
    ]
    return "Sentimen pasar hari ini: 🟢" + random.choice(sentiments)
