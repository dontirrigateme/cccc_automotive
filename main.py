import os
import discord
from discord import app_commands
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

    print(f"Logged in as {bot.user}")

@bot.tree.command(name="ping", description="Check if the bot is alive")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

TOPICS = [
    "capacitor",
    "resistor",
    "fuse",
    "relay_circuits",
    "trailer_lights"
]

@bot.tree.command(name="quiz", description="Start a quiz")
@app_commands.describe(topic="Choose a topic")
@app_commands.choices(topic=[
    app_commands.Choice(name=t.replace("_", " ").title(), value=t) for t in TOPICS
])
async def quiz(interaction: discord.Interaction, topic: app_commands.Choice[str]):
    await interaction.response.send_message(f"Starting quiz on {topic.value}")


bot.run(TOKEN)
