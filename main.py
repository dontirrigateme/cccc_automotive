import os
import discord
from discord import app_commands
from discord.ext import commands
import random
from data.capacitors import QUESTIONS as capacitor_questions

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

class FlashcardView(discord.ui.View):
    def __init__(self, answer):
        super().__init__()
        self.answer = answer

    @discord.ui.button(label="Show Answer", style=discord.ButtonStyle.primary)
    async def show_answer(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(self.answer, ephemeral=True)

@bot.tree.command(name="quiz", description="Start a quiz")
@app_commands.describe(topic="Choose a topic")
@app_commands.choices(topic=[
    app_commands.Choice(name="Capacitor", value="capacitor")
])
async def quiz(interaction: discord.Interaction, topic: app_commands.Choice[str]):

    if topic.value == "capacitor":
        q = random.choice(capacitor_questions)
        view = FlashcardView(q["answer"])
        await interaction.response.send_message(q["question"], view=view)


bot.run(TOKEN)
