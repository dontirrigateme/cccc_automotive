import os
import discord
from discord import app_commands
from discord.ext import commands
import random
# from electude_data.capacitors import QUESTIONS as capacitor_questions
# from electude_data.resistors import QUESTIONS as resistor_questions
# from electude_data.fuses import QUESTIONS as fuse_questions
# from electude_data.lighting_and_signaling_circuits import QUESTIONS as lighting_and_signaling_circuits_questions
# from electude_data.schematics import QUESTIONS as schematics_questions
# from electude_data.batteries import QUESTIONS as batteries_questions
# from electude_data.charging_system_theory import QUESTIONS as charging_system_theory_questions
from electude_data.safety_and_emissions import QUESTIONS as safety_and_emissions_questions
# from electude_data.series_and_parallel_circuits import QUESTIONS as series_and_parallel_circuits_questions
from electude_data.coils_and_relays import QUESTIONS as coils_and_relays_questions
from electude_data.elec_braking_sys_theory import QUESTIONS as elec_braking_sys_theory_questions
from electude_data.tires_and_wheels_properties import QUESTIONS as tires_and_wheels_properties_questions
from electude_data.tire_theory import QUESTIONS as tire_theory_questions
from electude_data.wheels_theory import QUESTIONS as wheels_theory_questions
from electude_data.wheel_balancing_theory import QUESTIONS as wheel_balancing_theory_questions
from electude_data.ac_systems import QUESTIONS as ac_systems_questions

from ase_data.ch1_1_engine_diagnosis import QUESTIONS as ch1_1_engine_diagnosis_questions
from ase_data.ch1_2_cylinder_head_valve_train import QUESTIONS as ch1_2_cylinder_head_valve_train_questions
from ase_data.ch1_3_engine_block_diagnosis import QUESTIONS as ch1_3_engine_block_diagnosis_questions
from ase_data.ch1_4_lubrication_cooling_diagnosis import QUESTIONS as ch1_4_lubrication_cooling_diagnosis_questions
from ase_data.ch1_5_gaskets_seals_fasteners import QUESTIONS as ch1_5_gaskets_seals_fasteners_questions
from ase_data.ch1_6_gen_engine_reassembly import QUESTIONS as ch1_6_gen_engine_reassembly_questions
from ase_data.ch2_1_hydraulic_automatic_transmission import QUESTIONS as ch2_1_hydraulic_automatic_transmission_questions
from ase_data.ch2_2_mech_systems_components import QUESTIONS as ch2_2_mech_systems_components_questions
from ase_data.ch2_3_electronic_control_sys import QUESTIONS as ch2_3_electronic_control_sys_questions
from ase_data.ch2_4_auto_diag_test import QUESTIONS as ch2_4_auto_diag_test_questions
from ase_data.ch3_manual_drive_axles import QUESTIONS as ch3_manual_drive_axles_questions

from study_guide_data.adv_auto_elec_sg import QUESTIONS as adv_auto_elec_sg_questions
from study_guide_data.adv_transp_elec_sg import QUESTIONS as adv_transp_elec_sg_questions
from study_guide_data.adv_eng_perf_sg import QUESTIONS as adv_eng_perf_sg_questions
from study_guide_data.fuel_inj_sys_diag_sg import QUESTIONS as fuel_inj_sys_diag_sg_questions
from study_guide_data.ac_quiz_avi import QUESTIONS as ac_quiz_avi_questions

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
    # "capacitors": {
    #     "label": "Capacitors",
    #     "questions": capacitor_questions,
    # },
    # "resistors": {
    #     "label": "Resistors",
    #     "questions": resistor_questions,
    # },
    # "fuses": {
    #     "label": "Fuses",
    #     "questions": fuse_questions,
    # },
    # "lighting_and_signaling_circuits": {
    #     "label": "Lighting & Signaling Circuits",
    #     "questions": lighting_and_signaling_circuits_questions,
    # },
    # "schematics": {
    #     "label": "Schematics",
    #     "questions": schematics_questions,
    # },
    # "batteries": {
    #     "label": "Batteries",
    #     "questions": batteries_questions,
    # },
    # "charging_system_theory": {
    #     "label": "Charging System Theory",
    #     "questions": charging_system_theory_questions,
    # },
    "safety_and_emissions": {
        "label": "Safety & Emissions",
        "questions": safety_and_emissions_questions,
    },
    # "series_and_parallel_circuits": {
    #     "label": "Series & Parallel Circuits",
    #     "questions": series_and_parallel_circuits_questions,
    # },
    "coils_and_relays": {
        "label": "Coils & Relays",
        "questions": coils_and_relays_questions,
    },
    "electronic_braking_systems_theory": {
        "label": "Electronic Braking Systems Theory",
        "questions": elec_braking_sys_theory_questions,
    },
    "tires_and_wheels_properties": {
        "label": "Properties of Tires and Wheels",
        "questions": tires_and_wheels_properties_questions,
    },
    "tire_theory": {
        "label": "Tire Theory",
        "questions": tire_theory_questions,
    },
    "wheels_theory": {
        "label": "Wheels Theory",
        "questions": wheels_theory_questions,
    },
    "wheel_balancing_theory": {
        "label": "Wheel Balancing Theory",
        "questions": wheel_balancing_theory_questions,
    },
    "ac_systems": {
        "label": "Air-Conditioning Systems",
        "questions": ac_systems_questions,
    },
}

ASE_TOPICS = {
    "ch1_1_engine_diagnosis": {
        "label": "A1.01 Engine Repair: Engine Diagnosis",
        "questions": ch1_1_engine_diagnosis_questions,
    },
    "ch1_2_cylinder_head_valve_train": {
        "label": "A1.02 Engine Repair: Cylinder Head & Valve Train Diagnosis & Repair",
        "questions": ch1_2_cylinder_head_valve_train_questions,
    },
    "ch1_3_engine_block_diagnosis": {
        "label": "A1.03 Engine Repair: Engine Block Diagnosis & Repair",
        "questions": ch1_3_engine_block_diagnosis_questions,
    },
    "ch1_4_lubrication_cooling_diagnosis": {
        "label": "A1.04 Engine Repair: Lubrication & Cooling Systems Diagnosis & Repair",
        "questions": ch1_4_lubrication_cooling_diagnosis_questions,
    },
    "ch1_5_gaskets_seals_fasteners": {
        "label": "A1.05 Engine Repair: Gaskets, Seals, & Fastener Service",
        "questions": ch1_5_gaskets_seals_fasteners_questions,
    },
    "ch1_6_gen_engine_reassembly": {
        "label": "A1.06 Engine Repair: General Engine Reassembly",
        "questions": ch1_6_gen_engine_reassembly_questions,
    },
    "ch2_1_hydraulic_automatic_transmission": {
        "label": "A2.01 Automatic Transmission/Transaxle: Hydraulic Systems in Automatic Transmissions",
        "questions": ch2_1_hydraulic_automatic_transmission_questions,
    },
    "ch2_2_mech_systems_components": {
        "label": "A2.02 Automatic Transmission/Transaxle: Mechanical Systems & Components",
        "questions": ch2_2_mech_systems_components_questions,
    },
    "ch2_3_electronic_control_sys": {
        "label": "A2.03 Automatic Transmission/Transaxle: Electronic Control Systems",
        "questions": ch2_3_electronic_control_sys_questions,
    },
    "ch2_4_auto_diag_test": {
        "label": "A2.04 Automatic Transmission/Transaxle: Diagnosis & Testing Procedures",
        "questions": ch2_4_auto_diag_test_questions,
    },
    "ch3_manual_drive_axles": {
        "label": "A3 Manual Drive Train & Axles",
        "questions": ch3_manual_drive_axles_questions,
    },
}

STUDY_GUIDE_TOPICS = {
    "adv_auto_elec_sg": {
        "label": "Advanced Automotive Electricity Study Guide",
        "questions": adv_auto_elec_sg_questions,
    },
    "adv_transp_elec_sg": {
        "label": "Advanced Transportation Electronics Study Guide",
        "questions": adv_transp_elec_sg_questions,
    },
    "adv_eng_perf_sg": {
        "label": "Advanced Engine Performance Study Guide",
        "questions": adv_eng_perf_sg_questions,
    },
    "fuel_inj_sys_diag_sg": {
        "label": "Fuel Injection System Diagnosis & Service Study Guide",
        "questions": fuel_inj_sys_diag_sg_questions,
    },
    "ac_quiz_avi": {
        "label": "Keeping it Cool - AVI AC Quiz",
        "questions": ac_quiz_avi_questions,
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

class MultipleChoiceQuizView(discord.ui.View):
    def __init__(self, questions, source_name):
        super().__init__(timeout=300)
        self.questions = questions
        self.source_name = source_name
        self.current = random.choice(self.questions)

        for choice in ["A", "B", "C", "D"]:
            self.add_item(AnswerButton(choice))

        self.add_item(NextQuestionButton())

    def get_question_content(self):
        category = self.current.get("category", "Unknown")
        question = self.current["question"]
        return f"**{self.source_name} - {category}**\n\n{question}"

    def get_correct_letter(self):
        answer = self.current["answer"].strip()
        return answer[0].upper()

    def get_answer(self):
        return self.current["answer"]

    def get_image(self):
        return self.current.get("image")

    def disable_answer_buttons(self):
        for item in self.children:
            if isinstance(item, AnswerButton):
                item.disabled = True

    def enable_answer_buttons(self):
        for item in self.children:
            if isinstance(item, AnswerButton):
                item.disabled = False

class AnswerButton(discord.ui.Button):
    def __init__(self, choice):
        super().__init__(
            label=choice,
            style=discord.ButtonStyle.secondary,
            row=0
        )
        self.choice = choice

    async def callback(self, interaction: discord.Interaction):
        view = self.view
        correct_letter = view.get_correct_letter()
        correct_answer = view.get_answer()

        if self.choice == correct_letter:
            result = f"✅ **Correct!**\n\nAnswer: **{correct_answer}**"
        else:
            result = (
                f"❌ **Not quite.**\n\n"
                f"You chose: **{self.choice}**\n"
                f"Correct answer: **{correct_answer}**"
            )

        view.disable_answer_buttons()

        await interaction.response.edit_message(
            content=f"{view.get_question_content()}\n\n{result}",
            view=view
        )

class NextQuestionButton(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="Next Question",
            style=discord.ButtonStyle.primary,
            row=1
        )

    async def callback(self, interaction: discord.Interaction):
        view = self.view
        view.current = random.choice(view.questions)
        view.enable_answer_buttons()

        question_content = view.get_question_content()
        image_path = view.get_image()

        if image_path:
            file = discord.File(image_path)
            await interaction.response.edit_message(
                content=question_content,
                attachments=[file],
                view=view
            )
        else:
            await interaction.response.edit_message(
                content=question_content,
                attachments=[],
                view=view
            )

@bot.tree.command(name="electude", description="Study Electude flashcards")
@app_commands.describe(topic="Choose a topic")
@app_commands.choices(topic=[
    app_commands.Choice(name="Any / Random", value="any"),
    # app_commands.Choice(name="Capacitors", value="capacitors"),
    # app_commands.Choice(name="Resistors", value="resistors"),
    # app_commands.Choice(name="Fuses", value="fuses"),
    # app_commands.Choice(name="Lighting & Signaling Circuits", value="lighting_and_signaling_circuits"),
    # app_commands.Choice(name="Schematics", value="schematics"),
    # app_commands.Choice(name="Batteries", value="batteries"),
    # app_commands.Choice(name="Charging System Theory", value="charging_system_theory"),
    app_commands.Choice(name="Safety & Emissions", value="safety_and_emissions"),
    # app_commands.Choice(name="Series & Parallel Circuits", value="series_and_parallel_circuits"),
    app_commands.Choice(name="Coils & Relays", value="coils_and_relays"),
    app_commands.Choice(name="Electronic Braking Systems Theory", value="elec_braking_sys_theory"),
    app_commands.Choice(name="Properties of Tires and Wheels", value="tires_and_wheels_properties"),
    app_commands.Choice(name="Tire Theory", value="tire_theory"),
    app_commands.Choice(name="Wheels Theory", value="wheels_theory"),
    app_commands.Choice(name="Wheel Balancing Theory", value="wheel_balancing_theory"),
    app_commands.Choice(name="Air-Conditioning Systems", value="ac_systems"),
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

    view = MultipleChoiceQuizView(questions, "Electude")
    question_content = view.get_question_content()
    image_path = view.get_image()

    if image_path:
        file = discord.File(image_path)
        await interaction.response.send_message(
            question_content,
            file=file,
            view=view,
            ephemeral=True
        )
    else:
        await interaction.response.send_message(
            question_content,
            view=view,
            ephemeral=True
        )

@bot.tree.command(name="ase", description="Study ASE flashcards")
@app_commands.describe(topic="Choose a topic")
@app_commands.choices(topic=[
    app_commands.Choice(name="Any / Random", value="any"),
    app_commands.Choice(name="A1.01 Engine Repair: Engine Diagnosis", value="ch1_1_engine_diagnosis"),
    app_commands.Choice(name="A1.02 Engine Repair: Cylinder Head & Valve Train Diagnosis & Repair", value="ch1_2_cylinder_head_valve_train"),
    app_commands.Choice(name="A1.03 Engine Repair: Engine Block Diagnosis & Repair", value="ch1_3_engine_block_diagnosis"),
    app_commands.Choice(name="A1.04 Engine Repair: Lubrication & Cooling Systems Diagnosis & Repair", value="ch1_4_lubrication_cooling_diagnosis"),
    app_commands.Choice(name="A1.05 Engine Repair: Gaskets, Seals, & Fastener Service", value="ch1_5_gaskets_seals_fasteners"),
    app_commands.Choice(name="A1.06 Engine Repair: General Engine Reassembly", value="ch1_6_gen_engine_reassembly"),
    app_commands.Choice(name="A2.01 Automatic Transmission/Transaxle: Hydraulic Systems in Automatic Transmissions", value="ch2_1_hydraulic_automatic_transmission"),
    app_commands.Choice(name="A2.02 Automatic Transmission/Transaxle: Mechanical Systems & Components", value="ch2_2_mech_systems_components"),
    app_commands.Choice(name="A2.03 Automatic Transmission/Transaxle: Electronic Control Systems", value="ch2_3_electronic_control_sys"),
    app_commands.Choice(name="A2.04 Automatic Transmission/Transaxle: Diagnosis & Testing Procedures", value="ch2_4_auto_diag_test"),
    app_commands.Choice(name="A3 Manual Drive Train & Axles", value="ch3_manual_drive_axles"),
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

    view = MultipleChoiceQuizView(questions, "ASE")
    question_content = view.get_question_content()
    image_path = view.get_image()

    if image_path:
        file = discord.File(image_path)
        await interaction.response.send_message(
            question_content,
            file=file,
            view=view,
            ephemeral=True
        )
    else:
        await interaction.response.send_message(
            question_content,
            view=view,
            ephemeral=True
        )

@bot.tree.command(name="studyguide", description="Study guide flashcards")
@app_commands.describe(topic="Choose a topic")
@app_commands.choices(topic=[
    app_commands.Choice(name="Any / Random", value="any"),
    app_commands.Choice(
        name="Advanced Automotive Electricity Study Guide",
        value="adv_auto_elec_sg"
    ),
    app_commands.Choice(
        name="Advanced Transportation Electronics Study Guide",
        value="adv_transp_elec_sg"
    ),
    app_commands.Choice(
        name="Advanced Engine Performance Study Guide",
        value="adv_eng_perf_sg"
    ),
    app_commands.Choice(
        name="Fuel Injection System Diagnosis & Service Study Guide",
        value="fuel_inj_sys_diag_sg"
    ),
    app_commands.Choice(
        name="AC AVI Quiz",
        value="ac_quiz_avi"
    ),
])
async def studyguide(interaction: discord.Interaction, topic: app_commands.Choice[str]):

    if topic.value == "any":
        questions = get_all_questions(STUDY_GUIDE_TOPICS)
    else:
        topic_info = STUDY_GUIDE_TOPICS.get(topic.value)

        if not topic_info:
            await interaction.response.send_message("No questions found for this topic.")
            return

        questions = []
        for question in topic_info["questions"]:
            question_copy = question.copy()
            question_copy["category"] = topic_info["label"]
            questions.append(question_copy)

    view = MultipleChoiceQuizView(questions, "Study Guide")
    question_content = view.get_question_content()
    image_path = view.get_image()

    if image_path:
        file = discord.File(image_path)
        await interaction.response.send_message(
            question_content,
            file=file,
            view=view,
            ephemeral=True
        )
    else:
        await interaction.response.send_message(
            question_content,
            view=view,
            ephemeral=True
        )


bot.run(TOKEN)
