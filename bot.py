import discord
from discord.ext import commands
import datetime
import os

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Your log channel ID
LOG_CHANNEL_ID = 1405862526222340107  

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_message_delete(message):
    if message.author.bot:
        return

    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    if log_channel is None:
        return

    embed = discord.Embed(
        title="🗑️ Message Deleted",
        color=discord.Color.red(),
        timestamp=datetime.datetime.utcnow()
    )
    embed.add_field(name="Author", value=str(message.author), inline=False)
    embed.add_field(name="Txt content", value=message.content or "*(No text, maybe attachment)*", inline=False)
    embed.add_field(name="Time", value=message.created_at.strftime("%Y-%m-%d %H:%M:%S UTC"), inline=False)

    await log_channel.send(embed=embed)

# 🔹 Get token from environment (.env file)
TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)