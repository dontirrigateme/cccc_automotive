import os
import discord
from discord import app_commands
from discord.ext import commands
import random
from data.capacitors import QUESTIONS as capacitor_questions
from data.resistors import QUESTIONS as resistor_questions
from data.relays import QUESTIONS as relay_questions
from data.fuses import QUESTIONS as fuse_questions

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

TOPIC_DATA = {
    "capacitor": capacitor_questions,
    "resistor": resistor_questions,
    "relay": relay_questions,
    "fuse": fuse_questions,
}

class FlashcardView(discord.ui.View):
    def __init__(self, questions):
        super().__init__(timeout=None)
        self.questions = questions
        self.current = random.choice(self.questions)

    def get_question(self):
        return self.current["question"]

    def get_answer(self):
        return self.current["answer"]

    def get_image(self):
        return self.current.get("image")

    @discord.ui.button(label="Show Answer", style=discord.ButtonStyle.primary)
    async def show_answer(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(self.get_answer(), ephemeral=True)

    @discord.ui.button(label="Next Question", style=discord.ButtonStyle.secondary)
    async def next_question(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current = random.choice(self.questions)
    
        question = self.get_question()
        image_path = self.get_image()
    
        if image_path:
            file = discord.File(image_path)
            await interaction.response.edit_message(
                content=question,
                attachments=[file],
                view=self
            )
        else:
            await interaction.response.edit_message(
                content=question,
                attachments=[],
                view=self
            )

@bot.tree.command(name="quiz", description="Start a quiz")
@app_commands.describe(topic="Choose a topic")
@app_commands.choices(topic=[
    app_commands.Choice(name="Capacitor", value="capacitor"),
    app_commands.Choice(name="Resistor", value="resistor"),
    app_commands.Choice(name="Relay", value="relay"),
    app_commands.Choice(name="Fuse", value="fuse"),
])
async def quiz(interaction: discord.Interaction, topic: app_commands.Choice[str]):

    questions = TOPIC_DATA.get(topic.value)

    if not questions:
        await interaction.response.send_message("No questions found for this topic.")
        return
    
    view = FlashcardView(questions)
    question_text = view.get_question()
    image_path = view.get_image()
    
    if image_path:
        file = discord.File(image_path)
        await interaction.response.send_message(
            question_text,
            file=file,
            view=view
        )
    else:
        await interaction.response.send_message(
            question_text,
            view=view
        )


bot.run(TOKEN)
