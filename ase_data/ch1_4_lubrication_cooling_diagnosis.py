#A1.04 Engine Repair - Lubrication & Cooling Systems Diagnosis & Repair

QUESTIONS = [
    # {
    #     "question": (
    #         "What are three key oil system components?"
    #     ), #001
    #     "answer": (
    #         "Oil pumps\n"
    #         "Pressure sensors\n"
    #         "Oil filters"
    #     ),
    # },
    # {
    #     "question": "What are the two most common types of oil pumps?", #002
    #     "answer": "Gear pumps and rotor (gerotor) pumps",
    # },
    # {
    #     "question": "How do gear pumps work?", #003
    #     "answer": "They use meshing gears to push oil through the system",
    # },
    # {
    #     "question": "How do rotor pumps work?", #004
    #     "answer": "They employ an inner and outer rotor to generate pressure",
    # },
    # {
    #     "question": "What are some things that abnormally high oil pressure might indicate?", #005
    #     "answer": "Blockages or malfunctioning pressure-relief valves",
    # },
    # {
    #     "question": "What component removes contaminants and debris from the circulating oil to prevent wear and damage to engine parts?", #006
    #     "answer": "Oil filter",
    # },
    # {
    #     "question": "What are two types of oil filters?", #007
    #     "answer": "Cartridge-type or spin-on",
    # },
    # {
    #     "question": "What part of an oil filter maintains oil pressure during shutdown?", #008
    #     "answer": "Anti-drainback valve",
    # },
    # {
    #     "question": (
    #         "What are some common causes of low oil pressure?"
    #     ), #009
    #     "answer": (
    #         "Worn or damaged oil pump\n"
    #         "Excessive bearing clearance\n"
    #         "Oil leaks\n"
    #         "Clogged oil filter or passages\n"
    #         "Using incorrect oil viscosity\n"
    #         "Faulty oil pressure sensor or gauge"
    #     ),
    # },
    # {
    #     "question": (
    #         "What are the components of the engine's cooling system?"
    #     ), #010
    #     "answer": (
    #         "Radiator\n"
    #         "Thermostat\n"
    #         "Water pump\n"
    #         "Cooling fans"
    #     ),
    # },
    # {
    #     "question": "What part of the cooling system acts as the primary heat exchanger?", #011
    #     "answer": "Radiator",
    # },
    # {
    #     "question": "What are radiators usually made of?", #012
    #     "answer": "Aluminum or copper alloys",
    # },
    # {
    #     "question": "Thermostats control coolant flow based on __________.", #013
    #     "answer": "Temperature",
    # },
    # {
    #     "question": "At what temperature range does the thermostat usually open to allow coolant to flow to the radiator?", #014
    #     "answer": "180-195°F (82-90°C)",
    # },
    # {
    #     "question": "What typically drives the water pump?", #015
    #     "answer": "The engine's accessory belt or timing belt",
    # },
    # {
    #     "question": "Cooling fans can be mechanically driven by a belt or or electrically powered with thermostatic or ECU control. True or false?", #016
    #     "answer": "True",
    # },
    # {
    #     "question": (
    #         "What are some things that can cause cooling fan failure?"
    #     ), #017
    #     "answer": (
    #         "- Mechanical issues like broken fan blades, damaged belts, or seized fan clutches\n"
    #         "- Electrical faults, such as failed electric fan motors, blown fuses, faulty relays, or damaged wiring\n"
    #         "- Control system failures like malfunctioning temperature sensors or engine control modules (ECMs)"
    #     ),
    # },
    # {
    #     "question": "What happens if the thermostat is stuck closed?", #018
    #     "answer": "This can prevent coolant from flowing to the radiator, causing rapid overheating. The engine warms quickly, but temperature rises sharply and stays high",
    # },
    # {
    #     "question": "What happens if the thermostat is stuck open?", #019
    #     "answer": "This causes the engine to run too cool, leading to poor efficiency, but generally not overheating.",
    # },
    # {
    #     "question": (
    #         "What are some symptoms of a thermostat that is stuck closed?"
    #     ), #020
    #     "answer": (
    #         "Overheating after warm-up\n"
    #         "Poor heater performance\n"
    #         "Fluctuating temperature gauge readings"
    #     ),
    # },
    # {
    #     "question": (
    #         "What are some symptoms of a clogged radiator?"
    #     ), #021
    #     "answer": (
    #         "Overheating under load or prolonged idling\n"
    #         "Visible debris on radiator fins\n"
    #         "Fluctuating temperature gauge readings"
    #     ),
    # },
    # {
    #     "question": "What kind of test can identify leaks that may not be visible when the engine is off or cold?", #022
    #     "answer": "Pressure testing",
    # },
    # {
    #     "question": (
    #         "Detecting combustion gases in the coolant is a key method for diagnosing what three things?"
    #     ), #023
    #     "answer": (
    #         "Head gasket failure\n"
    #         "Cracked cylinder heads\n"
    #         "Block cracks"
    #     ),
    # },
    {
        "question": ( #01
            "What is the primary function of an oil pump?\n\n"
            "A. Circulate coolant\n"
            "B. Circulate engine oil\n"
            "C. Filter oil\n"
            "D. Measure oil pressure"
        ), #024
        "answer": (
            "B. Circulate engine oil"
        ),
    },
    {
        "question": ( #02
            "Which type of oil pump uses gears to move oil?\n\n"
            "A. Rotor\n"
            "B. Gear\n"
            "C. Vane\n"
            "D. Piston"
        ), #025
        "answer": (
            "B. Gear"
        ),
    },
    {
        "question": ( #03
            "What does a low oil pressure gauge reading typically indicate?\n\n"
            "A. High oil level\n"
            "B. Worn bearings\n"
            "C. Normal operation\n"
            "D. Faulty spark plugs"
        ), #026
        "answer": (
            "B. Worn bearings"
        ),
    },
    {
        "question": ( #04
            "Which tool is used to test oil pressure?\n\n"
            "A. Oil pressure gauge\n"
            "B. Compression tester\n"
            "C. Torque wrench\n"
            "D. Vacuum gauge"
        ), #027
        "answer": (
            "A. Oil pressure gauge"
        ),
    },
    {
        "question": ( #05
            "What is a common cause of low oil pressure?\n\n"
            "A. Clogged radiator\n"
            "B. Worn main bearings\n"
            "C. Sticking valve\n"
            "D. Broken timing chain"
        ), #028
        "answer": (
            "B. Worn main bearings"
        ),
    },
    {
        "question": ( #06
            "Which component controls oil flow and pressure?\n\n"
            "A. Oil pump relief valve\n"
            "B. Thermostat\n"
            "C. Water pump\n"
            "D. Camshaft"
        ), #029
        "answer": (
            "A. Oil pump relief valve"
        ),
    },
    {
        "question": ( #07
            "What is the purpose of an oil filter?\n\n"
            "A. Remove contaminants\n"
            "B. Increase oil pressure\n"
            "C. Lubricate valves\n"
            "D. Seal head gasket"
        ), #030
        "answer": (
            "A. Remove contaminants"
        ),
    },
    {
        "question": ( #08
            "Radiators primarily function to:\n\n"
            "A. Cool engine oil\n"
            "B. Cool engine coolant\n"
            "C. Lubricate pistons\n"
            "D. Pump coolant"
        ), #031
        "answer": (
            "B. Cool engine coolant"
        ),
    },
    {
        "question": ( #09
            "What component opens to allow coolant flow when the engine reaches operating temperature?\n\n"
            "A. Radiator cap\n"
            "B. Thermostat\n"
            "C. Water pump\n"
            "D. Oil pump"
        ), #032
        "answer": (
            "B. Thermostat"
        ),
    },
    {
        "question": ( #10
            "What does a sticking thermostat cause?\n\n"
            "A. Overheating\n"
            "B. Low oil pressure\n"
            "C. Increased fuel economy\n"
            "D. Smooth idle"
        ), #033
        "answer": (
            "A. Overheating"
        ),
    },
    {
        "question": ( #11
            "Which is a common symptom of a clogged radiator?\n\n"
            "A. Overheating\n"
            "B. High oil pressure\n"
            "C. Rough idle\n"
            "D. Low compression"
        ), #034
        "answer": (
            "A. Overheating"
        ),
    },
    {
        "question": ( #12
            "Cooling fans help:\n\n"
            "A. Circulate coolant\n"
            "B. Increase oil flow\n"
            "C. Draw air through the radiator\n"
            "D. Open the thermostat"
        ), #035
        "answer": (
            "C. Draw air through the radiator"
        ),
    },
    {
        "question": ( #13
            "What is a primary cause of engine overheating?\n\n"
            "A. Faulty oil pump\n"
            "B. Fan failure\n"
            "C. Spark plug fouling\n"
            "D. Clogged air filter"
        ), #036
        "answer": (
            "B. Fan failure"
        ),
    },
    {
        "question": ( #14
            "What does a cooling system pressure test detect?\n\n"
            "A. Coolant leaks\n"
            "B. Oil leaks\n"
            "C. Exhaust leaks\n"
            "D. Fuel leaks"
        ), #037
        "answer": (
            "A. Coolant leaks"
        ),
    },
    {
        "question": ( #15
            "How does a block tester detect head gasket leaks?\n\n"
            "A. Measures coolant temperature\n"
            "B. Detects combustion gases in coolant\n"
            "C. Tests oil pressure\n"
            "D. Measures compression"
        ), #038
        "answer": (
            "B. Detects combustion gases in coolant"
        ),
    },
    {
        "question": ( #16
            "What color change in a block tester indicates combustion gases?\n\n"
            "A. Blue to yellow\n"
            "B. Red to green\n"
            "C. Yellow to blue\n"
            "D. Green to red"
        ), #039
        "answer": (
            "A. Blue to yellow"
        ),
    },
    {
        "question": ( #17
            "Which is NOT a component of the cooling system?\n\n"
            "A. Radiator\n"
            "B. Oil pump\n"
            "C. Thermostat\n"
            "D. Water pump"
        ), #040
        "answer": (
            "B. Oil pump"
        ),
    },
    {
        "question": ( #18
            "What typically causes coolant loss without visible leaks?\n\n"
            "A. Head gasket failure\n"
            "B. Broken timing belt\n"
            "C. Worn piston rings\n"
            "D. Stuck valve"
        ), #041
        "answer": (
            "A. Head gasket failure"
        ),
    },
    {
        "question": ( #19
            "Which of these would cause a low oil pressure reading but normal engine temperature?\n\n"
            "A. Worn bearings\n"
            "B. Stuck thermostat\n"
            "C. Clogged radiator\n"
            "D. Fan failure"
        ), #042
        "answer": (
            "A. Worn bearings"
        ),
    },
    {
        "question": ( #20
            "Which test is best to confirm a blown head gasket?\n\n"
            "A. Block tester for combustion gases\n"
            "B. Compression test\n"
            "C. Oil pressure test\n"
            "D. Vacuum gauge reading"
        ), #043
        "answer": (
            "A. Block tester for combustion gases"
        ),
    },
]
