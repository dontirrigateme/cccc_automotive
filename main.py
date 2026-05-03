import os
import discord
from discord import app_commands
from discord.ext import commands
import random
from electude_data.capacitors import QUESTIONS as capacitor_questions
from electude_data.resistors import QUESTIONS as resistor_questions
from electude_data.fuses import QUESTIONS as fuse_questions
from electude_data.lighting_and_signaling_circuits import QUESTIONS as lighting_and_signaling_circuits_questions
from electude_data.schematics import QUESTIONS as schematics_questions
from electude_data.batteries import QUESTIONS as batteries_questions
from ase_data.ch1_1_engine_diagnosis import QUESTIONS as ch1_1_engine_diagnosis_questions
from ase_data.ch1_2_cylinder_head_valve_train import QUESTIONS as ch1_2_cylinder_head_valve_train_questions
from ase_data.ch1_3_engine_block_diagnosis import QUESTIONS as ch1_3_engine_block_diagnosis_questions
from ase_data.ch1_4_lubrication_cooling_diagnosis import QUESTIONS as ch1_4_lubrication_cooling_diagnosis_questions
from ase_data.ch1_5_gaskets_seals_fasteners import QUESTIONS as ch1_5_gaskets_seals_fasteners_questions

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

ELECTUDE_TOPICS = {
    "capacitors": {
        "label": "Capacitors",
        "questions": capacitor_questions,
    },
    "resistors": {
        "label": "Resistors",
        "questions": resistor_questions,
    },
    "fuses": {
        "label": "Fuses",
        "questions": fuse_questions,
    },
    "lighting_and_signaling_circuits": {
        "label": "Lighting & Signaling Circuits",
        "questions": lighting_and_signaling_circuits_questions,
    },
    "schematics": {
        "label": "Schematics",
        "questions": schematics_questions,
    },
    "batteries": {
        "label": "Batteries",
        "questions": batteries_questions,
    },
}

ASE_TOPICS = {
    "ch1_1_engine_diagnosis": {
        "label": "01.01 Engine Repair: Engine Diagnosis",
        "questions": ch1_1_engine_diagnosis_questions,
    },
    "ch1_2_cylinder_head_valve_train": {
        "label": "01.02 Engine Repair: Cylinder Head & Valve Train Diagnosis & Repair",
        "questions": ch1_2_cylinder_head_valve_train_questions,
    },
    "ch1_3_engine_block_diagnosis": {
        "label": "01.03 Engine Repair: Engine Block Diagnosis & Repair",
        "questions": ch1_3_engine_block_diagnosis_questions,
    },
    "ch1_4_lubrication_cooling_diagnosis": {
        "label": "01.04 Engine Repair: Lubrication & Cooling Systems Diagnosis & Repair",
        "questions": ch1_4_lubrication_cooling_diagnosis_questions,
    },
    "ch1_5_gaskets_seals_fasteners": {
        "label": "01.05 Engine Repair: Gaskets, Seals, & Fastener Service",
        "questions": ch1_5_gaskets_seals_fasteners_questions,
    },
}

def get_all_questions(topic_bank):
    all_questions = []

    for topic_key, topic_info in topic_bank.items():
        for question in topic_info["questions"]:
            question_copy = question.copy()
            question_copy["category"] = topic_info["label"]
            all_questions.append(question_copy)

    return all_questions

class FlashcardView(discord.ui.View):
    def __init__(self, questions, source_name):
        super().__init__(timeout=None)
        self.questions = questions
        self.source_name = source_name
        self.current = random.choice(self.questions)

    def get_question_content(self):
        category = self.current.get("category", "Unknown")
        question = self.current["question"]
        return f"**{self.source_name} - {category}**\n\n{question}"

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

        question_content = self.get_question_content()
        image_path = self.get_image()

        if image_path:
            file = discord.File(image_path)
            await interaction.response.edit_message(
                content=question_content,
                attachments=[file],
                view=self
            )
        else:
            await interaction.response.edit_message(
                content=question_content,
                attachments=[],
                view=self
            )

@bot.tree.command(name="electude", description="Study Electude flashcards")
@app_commands.describe(topic="Choose a topic")
@app_commands.choices(topic=[
    app_commands.Choice(name="Any / Random", value="any"),
    app_commands.Choice(name="Capacitors", value="capacitors"),
    app_commands.Choice(name="Resistors", value="resistors"),
    app_commands.Choice(name="Fuses", value="fuses"),
    app_commands.Choice(name="Lighting & Signaling Circuits", value="lighting_and_signaling_circuits"),
    app_commands.Choice(name="Schematics", value="schematics"),
    app_commands.Choice(name="Batteries", value="batteries"),
])
async def electude(interaction: discord.Interaction, topic: app_commands.Choice[str]):

    if topic.value == "any":
        questions = get_all_questions(ELECTUDE_TOPICS)
    else:
        topic_info = ELECTUDE_TOPICS.get(topic.value)

        if not topic_info:
            await interaction.response.send_message("No questions found for this topic.")
            return

        questions = []
        for question in topic_info["questions"]:
            question_copy = question.copy()
            question_copy["category"] = topic_info["label"]
            questions.append(question_copy)

    view = FlashcardView(questions, "Electude")
    question_content = view.get_question_content()
    image_path = view.get_image()

    if image_path:
        file = discord.File(image_path)
        await interaction.response.send_message(
            question_content,
            file=file,
            view=view
        )
    else:
        await interaction.response.send_message(
            question_content,
            view=view
        )

@bot.tree.command(name="ase", description="Study ASE flashcards")
@app_commands.describe(topic="Choose a topic")
@app_commands.choices(topic=[
    app_commands.Choice(name="Any / Random", value="any"),
    app_commands.Choice(name="01.01 Engine Repair: Engine Diagnosis", value="ch1_1_engine_diagnosis"),
    app_commands.Choice(name="01.02 Engine Repair: Cylinder Head & Valve Train Diagnosis & Repair", value="ch1_2_cylinder_head_valve_train"),
    app_commands.Choice(name="01.03 Engine Repair: Engine Block Diagnosis & Repair", value="ch1_3_engine_block_diagnosis"),
    app_commands.Choice(name="01.04 Engine Repair: Lubrication & Cooling Systems Diagnosis & Repair", value="ch1_4_lubrication_cooling_diagnosis"),
    app_commands.Choice(name="01.05 Engine Repair: Gaskets, Seals, & Fastener Service", value="ch1_5_gaskets_seals_fasteners"),
])
async def ase(interaction: discord.Interaction, topic: app_commands.Choice[str]):

    if topic.value == "any":
        questions = get_all_questions(ASE_TOPICS)
    else:
        topic_info = ASE_TOPICS.get(topic.value)

        if not topic_info:
            await interaction.response.send_message("No questions found for this topic.")
            return

        questions = []
        for question in topic_info["questions"]:
            question_copy = question.copy()
            question_copy["category"] = topic_info["label"]
            questions.append(question_copy)

    view = FlashcardView(questions, "ASE")
    question_content = view.get_question_content()
    image_path = view.get_image()

    if image_path:
        file = discord.File(image_path)
        await interaction.response.send_message(
            question_content,
            file=file,
            view=view
        )
    else:
        await interaction.response.send_message(
            question_content,
            view=view
        )


bot.run(TOKEN)
