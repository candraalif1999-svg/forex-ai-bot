# main.py
import discord
import os
import asyncio
from datetime import datetime
from discord import app_commands

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Import modul
try:
    from calendar import get_economic_calendar
    from news import get_market_news
    from sentiment import analyze_sentiment
except ImportError as e:
    print(f"Error import: {e}")

# Inisialisasi bot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Ambil token dari environment
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Perintah: /kalender
@tree.command(name="kalender", description="Tampilkan jadwal rilis data makroekonomi")
async def kalender(interaction: discord.Interaction):
    await interaction.response.defer()
    try:
        events = get_economic_calendar()
        embed = discord.Embed(
            title="📅 Kalender Ekonomi Hari Ini",
            color=0xFFD700,
            timestamp=datetime.utcnow()
        )
        for ev in events:
            embed.add_field(
                name=f"🔥 {ev['country']} — {ev['event']}",
                value=f"⏰ {ev['time']} | Impact: {ev['impact']}",
                inline=False
            )
        embed.set_footer(text="Sumber: Alpha Vantage")
        await interaction.followup.send(embed=embed)
    except Exception as e:
        await interaction.followup.send(f"❌ Gagal ambil data: {str(e)}")

# Perintah: /berita
@tree.command(name="berita", description="Berita terbaru & market catalyst")
async def berita(interaction: discord.Interaction):
    await interaction.response.defer()
    try:
        news = get_market_news()
        embed = discord.Embed(
            title="📰 Berita & Market Catalyst",
            color=0x0099ff,
            timestamp=datetime.utcnow()
        )
        for item in news:
            sentiment = "🟢 Bullish" if "positive" in item['sentiment'].lower() else "🔴 Bearish"
            embed.add_field(
                name=f"{sentiment} | {item['title']}",
                value=f"[Baca di ForexLive
