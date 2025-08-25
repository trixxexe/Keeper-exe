import discord
from discord.ext import commands
import datetime

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Replace with your log channel ID
LOG_CHANNEL_ID = 123456789012345678  

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

bot.run("YOUR_BOT_TOKEN")