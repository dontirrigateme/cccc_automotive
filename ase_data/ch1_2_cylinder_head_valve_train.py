#01.02 Engine Repair - Cylinder Head & Valve Train Diagnosis & Repair

QUESTIONS = [
    {
        "question": "What two materials are modern cylinder heads typically made of?", #001
        "answer": "Cast iron or aluminum alloy",
    },
    {
        "question": "What is the valve train responsible for?", #002
        "answer": "The valve train is the mechanical system responsible for opening and closing the engine's intake and exhaust valves in precise timing with piston movement.",
    },
    {
        "question": "What two materials are modern cylinder heads typically made of?", #003
        "answer": "Cast iron or aluminum alloy",
    },
    {
        "question": "What is a camshaft?", #004
        "answer": "A camshaft is a rotating, cylindrical shaft equipped with shaped lobes (cams) that converts rotational motion into linear or reciprocating motion.",
    },
    {
        "question": "Where is a camshaft located in an overhead valve (OHV) or pushrod engine?", #005
        "answer": "In the engine block",
    },
    {
        "question": "Where is a camshaft located in an overhead camshaft (OHC) engine?", #006
        "answer": "Directly above the valves",
    },
    {
        "question": "What does the camshaft operate in a single overhead camshaft engine (SOHC)?", #007
        "answer": "A single camshaft operates both intake and exhaust valves",
    },
    {
        "question": "How does a camshaft operate the valves in an overhead camshaft engine (OHC)?", #008
        "answer": "Via rocker arms or directly on the valve stems",
    },
    {
        "question": "What does the camshaft operate in a double overhead camshaft engine (DOHC)?", #009
        "answer": "One camshaft operates the intake valves, and the other operates the exhaust valves",
    },
    {
        "question": "What is an advantage of a double overhead camshaft engine (DOHC)?", #010
        "answer": "More precise valve timing, supports multiple valves per cylinder",
    },
    {
        "question": "What keeps valves closed?", #011
        "answer": "Valve springs",
    },
    {
        "question": "What is valve float/bounce?", #012
        "answer": "When springs cannot close valves fast enough at high RPMs",
    },
    {
        "question": "What do valve lifters do?", #013
        "answer": "Lifters maintain proper valve lash/clearance",
    },
    {
        "question": "What do valve retainers and keepers do?", #014
        "answer": "Retainers and keepers secure springs to the valve stems",
    },
    {
        "question": "What are four common failures of the valve train?", #015
        "answer": "1) Burned valves, 2) broken valve springs, 3) worn cam lobes, and 4) Sticking lifters",
    },
    {
        "question": "How do valves on the valve train get burned?", #016
        "answer": "They burn when the valve's sealing surface is damaged by excessive heat",
    },
    {
        "question": "What are common causes of burned valves?", #017
        "answer": "Poor combustion, lean air-fuel mixtures, incorrect ignition timing, or prolonged overheating",
    },
    {
        "question": "What happens when an engine has burned valves?", #018
        "answer": "Burned valves fail to seal properly, causing compression loss, misfires, rough idle, and increased emissions.",
    },
    {
        "question": "Which valves are more prone to burning?", #019
        "answer": "Exhaust valves, because they handle hotter gases.",
    },
    {
        "question": "What causes broken valve springs?", #020
        "answer": "Valves springs can break due to metal fatigue, improper spring tension, or valve float at high RPMs.",
    },
    {
        "question": "What happens when an engine has broken valve springs?", #021
        "answer": "A broken spring results in a valve that won't close fully on time, causing rough running, loss of power, and potential piston-to-valve contact, which can severely damage the engine.",
    },
    {
        "question": "What happens when a camshaft develops worn cam lobes?", #022
        "answer": "Worn cam lobes reduce the camshaft's ability to lift valves fully, leading to weak valve opening.",
    },
    {
        "question": "What effect do worn cam lobes have on an engine?", #023
        "answer": "Worn cam lobes can cause poor combustion, reduced power, and often noisy valve operation (ticking).",
    },
    {
        "question": "What can cause worn cam lobes?", #024
        "answer": "Lobe wear can be caused by and/or accelerated by inadequate lubrication or contaminated oil",
    },
    {
        "question": "What is the purpose of timing chains and belts?", #025
        "answer": "They synchronize the camshaft(s) with the crankshaft.",
    },
    {
        "question": "What are some symptoms of timing-related issues?", #026
        "answer": "Rattling or slapping noises; hard starting or no start; rough idle, misfires, or poor acceleration; check engine light with cam/crank correlation codes",
    },
    {
        "question": "What could rattling or slapping noises coming from the engine indicate with relation to valve timing?", #027
        "answer": "Worn chain guides, tensioners, or a loose belt",
    },
    {
        "question": "What could a hard start or no start indicate with relation to valve timing?", #028
        "answer": "The timing has jumped teeth or the belt/chain has broken",
    },
    {
        "question": "What could rough idle, misfires, or poor acceleration indicate with relation to valve timing?", #029
        "answer": "These are caused by slight timing shifts due to stretched chains or worn tensioners",
    },
    {
        "question": "What could the check engine light with cam/crank correlation codes indicate with relation to valve timing?", #030
        "answer": "The PCM detecting misalignment",
    },
    {
        "question": "What is variable valve timing (VVT)?", #031
        "answer": "A system that allows the engine control module (ECM) to adjust camshaft timing dynamically for improved efficiency, power, and emissions.",
    },
    {
        "question": "Variable valve timing (VVT) can advance or retard cam timing using hydraulic actuators controlled by oil pressure. True or false?", #032
        "answer": "True",
    },
    {
        "question": "What happens if valve lash is too tight?", #033
        "answer": "Valves will not fully close, leading to compression loss, burned valves, and poor performance.",
    },
    {
        "question": "What happens if valve lash is too loose?", #034
        "answer": "Loose lash results in noisy operation (ticking or tapping sounds), accelerated wear on valve train components, and potential valve train damage at high RPMs.",
    },
    {
        "question": "What causes a warped cylinder head?", #035
        "answer": "It typically results from overheating, causing the metal to distort and lose its flatness.",
    },
    {
        "question": "What happens when a cylinder head is warped?", #036
        "answer": "The warping compromises the seal between the head and the engine block, often leading to head gasket failure.",
    },
    {
        "question": "What are the two telltale symptoms of a blown head gasket?", #037
        "answer": "Coolant loss and oil contamination",
    },
    {
        "question": "Why is coolant loss/oil contamination a symptom of a blown head gasket?", #038
        "answer": "When the head gasket fails between the coolant passages and combustion chamber, combustion gases can enter the cooling system, increasing pressure and forcing coolant out through the overflow or radiator cap.",
    },
    {
        "question": "How does oil contamination present with a blown head gasket?", #039
        "answer": "A blown head gasket may allow coolant to mix with engine oil, creating a milky, frothy substance often visible on the dipstick or oil filler cap.",
    },
    {
        "question": "What diagnostic clues point to a blown head gasket?", #040
        "answer": "Coolant loss, oil contamination, white smoke from the exhaust, bubbles in radiator/coolant overflow, loss of compression, overheating engine, poor engine performance",
    },
    {
        "question": "How does a thermal inspection help with diagnosing a warped cylinder head?", #041
        "answer": "Significant temperature variations on the cylinder head surface after engine operation can indicate coolant flow blockage",
    },
    {
        "question": "What should you do before removing and replacing a warped cylinder head?", #042
        "answer": "Repair any causes of overheating to prevent recurrence after repair",
    },
    {
        "question": (
            "What is a common cause of a warped cylinder head?\n\n"
            "A. Overcooling\n"
            "B. Engine overheating\n"
            "C. Excessive oil change intervals\n"
            "D. Poor fuel quality"
        ), #043
        "answer": (
            "B. Engine overheating"
        ),
    },
    {
        "question": (
            "Which material is typically used for cylinder heads?\n\n"
            "A. Cast iron or aluminum\n"
            "B. Plastic\n"
            "C. Steel\n"
            "D. Titanium"
        ), #044
        "answer": (
            "A. Cast iron or aluminum"
        ),
    },
    {
        "question": (
            "Which valve train component directly follows the camshaft motion transfer?\n\n"
            "A. Pushrod\n"
            "B. Rocker arm\n"
            "C. Lifter (tappet)\n"
            "D. Timing belt"
        ), #045
        "answer": (
            "C. Lifter (tappet)"
        ),
    },
    {
        "question": (
            "What symptom si common with a broken valve spring?\n\n"
            "A. Engine overheating\n"
            "B. Excessive valve noise and misfire\n"
            "C. Loss of oil pressure\n"
            "D. Transmission slipping"
        ), #046
        "answer": (
            "B. Excessive valve noise and misfire"
        ),
    },
    {
        "question": (
            "Sticking lifters usually cause:\n\n"
            "A. Loud ticking noise\n"
            "B. Smooth idle\n"
            "C. Excessive fuel comsumption\n"
            "D. Exhaust smoke"
        ), #047
        "answer": (
            "A. Loud ticking noise"
        ),
    },
    {
        "question": (
            "Low compression and large difference between wet and dry compression indicates:\n\n"
            "A. Bad rings\n"
            "B. Bad valve\n"
            "C. Cracked head\n"
            "D. Blown gasket"
        ), #048
        "answer": (
            "B. Bad valve"
        ),
    },
    {
        "question": (
            "What does a burned valve cause?\n\n"
            "A. Increased power\n"
            "B. Rough idle and misfire\n"
            "C. Smooth idle\n"
            "D. Improved fuel economy"
        ), #049
        "answer": (
            "B. Rough idle and misfire"
        ),
    },
    {
        "question": (
            "Valve springs function to:\n\n"
            "A. Open the valve\n"
            "B. Close the valve\n"
            "C. Lubricate the valve\n"
            "D. Seal the combustion chamber"
        ), #050
        "answer": (
            "B. Close the valve"
        ),
    },
    {
        "question": (
            "A worn cam lobe leads to\n\n"
            "A. Reduced valve lift and poor performance\n"
            "B. Increased compression\n"
            "C. No effect\n"
            "D. Better fuel economy"
        ), #051
        "answer": (
            "A. Reduced valve lift and poor performance"
        ),
    },
    {
        "question": (
            "Uneven temperature on a cylinder head scan often means:\n\n"
            "A. Warped head\n"
            "B. Perfect head\n"
            "C. Faulty spark plugs\n"
            "D. Incorrect oil viscosity"
        ), #052
        "answer": (
            "A. Warped head"
        ),
    },
    {
        "question": (
            "What does excessive valve lash cause?\n\n"
            "A. Valve not closing\n"
            "B. Noisy operation and valve damage\n"
            "C. Valve stuck open\n"
            "D. Head gasket failure"
        ), #053
        "answer": (
            "B. Noisy operation and valve damage"
        ),
    },
    {
        "question": (
            "Valve guides are for:\n\n"
            "A. Controlling valve movement and alignment\n"
            "B. Sealing head gasket\n"
            "C. Opening valves\n"
            "D. Lubricating camshaft"
        ), #054
        "answer": (
            "A. Controlling valve movement and alignment"
        ),
    },
    {
        "question": (
            "What's a key sign of a blown head gasket?\n\n"
            "A. White exhaust smoke\n"
            "B. Engine stalls at idle\n"
            "C. Transmission slipping\n"
            "D. Overfilled oil pan"
        ), #055
        "answer": (
            "A. White exhaust smoke"
        ),
    },
    {
        "question": (
            "Valve timing errors caused by timing chains often result from:\n\n"
            "A. Chain stretch or worn guides\n"
            "B. Low oil pressure\n"
            "C. Worn spark plugs\n"
            "D. Dirty air filter"
        ), #056
        "answer": (
            "A. Chain stretch or worn guides"
        ),
    },
    {
        "question": (
            "Which test best diagnoses valve sealing problems?\n\n"
            "A. Cylinder leakdown\n"
            "B. Oil pressure\n"
            "C. Compression only\n"
            "D. Spark test"
        ), #057
        "answer": (
            "A. Cylinder leakdown"
        ),
    },
    {
        "question": (
            "Valve float at high RPM is usually caused by:\n\n"
            "A. Valve spring failure\n"
            "B. Camshaft bearing\n"
            "C. Oil pump failure\n"
            "D. Fuel injector issue"
        ), #058
        "answer": (
            "A. Valve spring failure"
        ),
    },
    {
        "question": (
            "What is the function of a hydraulic lifter?\n\n"
            "A. Automatically maintain valve lash clearance\n"
            "B. Rotate camshaft\n"
            "C. Pump oil\n"
            "D. Control ignition timing"
        ), #059
        "answer": (
            "A. Automatically maintain valve lash clearance"
        ),
    },
    {
        "question": (
            "Timing belt replacement intervals are typically:\n\n"
            "A. 60,000-100,000 miles\n"
            "B. 10,000 miles\n"
            "C. 200,000 miles\n"
            "D. Never needed"
        ), #060
        "answer": (
            "A. 60,000-100,000 miles"
        ),
    },
    {
        "question": (
            "What causes a sticking lifter?\n\n"
            "A. Dirt or lack of oil\n"
            "B. Broken valve spring\n"
            "C. Faulty spark plug\n"
            "D. Worn piston rings"
        ), #061
        "answer": (
            "A. Dirt or lack of oil"
        ),
    },
    {
        "question": (
            "What effect does a burned valve have on compression?\n\n"
            "A. Lower compression on affected cylinder\n"
            "B. Higher compression\n"
            "C. No change\n"
            "D. causes overpressurization"
        ), #061
        "answer": (
            "A. Lower compression on affected cylinder"
        ),
    },
]
