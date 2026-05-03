#01.01 Engine Repair - Engine Diagnosis

QUESTIONS = [
    {
        "question": "Abnormal noises often point to internal mechanical issues. True or false?", #001
        "answer": "True",
    },
    {
        "question": "What is the likely cause of blue exhaust smoke?", #002
        "answer": "Burning oil",
    },
    {
        "question": "What could be the cause of an engine that is burning oil?", #003
        "answer": "Worn valve guides, piston rings, or PCV system",
    },
    {
        "question": "What is the likely cause of black exhaust smoke?", #004
        "answer": "Richh air-fuel mixture",
    },
    {
        "question": "What could be some likely causes of an engine with a rich air-fuel mixture?", #005
        "answer": "Faulty injectors, sensor malfunction, restricted air filter",
    },
    {
        "question": "What is the likely cause of white exhaust smoke (cold start)?", #006
        "answer": "Condensation",
    },
    {
        "question": "What does it mean if a vehicle's exhaust is emitting white smoke (cold start)?", #007
        "answer": "Normal, if brief",
    },
    {
        "question": "What is the likely cause of white exhaust smoke (continuous)?", #008
        "answer": "Coolant in combustion",
    },
    {
        "question": "What does it mean if a vehicle's exhaust is emitting white smoke (continuous)?", #009
        "answer": "Blown head gasket, cracked head/block",
    },
    {
        "question": "What system do you inspect if blue smoke appears only during acceleration?", #010
        "answer": "Worn piston rings or PCV valve",
    },
    {
        "question": "What are the likely sources of slick, amber-to-black engine oil under or around a vehicle?", #011
        "answer": "Valve cover, oil pan gasket, front/rear main seal",
    },
    {
        "question": "What are the likely sources of a sweet smell around a vehicle?", #012
        "answer": "Water pump, hoses, radiator, intake manifold",
    },
    {
        "question": "What are the likely sources of green, orange, or pink fluid under or around a vehicle?", #013
        "answer": "Water pump, hoses, radiator, intake manifold",
    },
    {
        "question": "What type of fluid is leaking if it's green, orange, or pink?", #014
        "answer": "Coolant",
    },
    {
        "question": "What type of fluid is leaking if it has a sweet smell?", #015
        "answer": "Coolant",
    },
    {
        "question": "What type of fluid is leaking if it's slick and red or pink?", #016
        "answer": "Transmission fluid",
    },
    {
        "question": "What are the likely sources of slick, red or pink fluid under or around a vehicle?", #017
        "answer": "Front pump seal or cooler lines",
    },
    {
        "question": "What are the likely sources of clear fluid with a gasoline smell under or around a vehicle?", #018
        "answer": "Fuel rail, injector seal, fuel lines",
    },
    {
        "question": "What type of fluid is leaking if it's oily and red or brown?", #019
        "answer": "Power-steering fluid",
    },
    {
        "question": "What is the likely scause of exhaust residue under or around a vehicle?", #020
        "answer": "Rich fuel mixture or poor combustion",
    },
    {
        "question": "What are some tools you can use to find a hard-to-spot oil or coolant leak?", #021
        "answer": "UV dye and blacklight",
    },
    {
        "question": "Name the likely mechanical cause(s) for the following symptom: low power.", #022
        "answer": "Worn piston rings, low compression, valve timing off",
    },
    {
        "question": "Name the likely mechanical cause(s) for the following symptom: rough idle.", #023
        "answer": "Burned valves, vacuum leaks, faulty lifters",
    },
    {
        "question": "Name the likely mechanical cause(s) for the following symptom: misfire (mechanical).", #024
        "answer": "Bent valve, stuck lifter, worn cam lobe",
    },
    {
        "question": "Name the likely mechanical cause(s) for the following symptom: no-start (cranks).", #025
        "answer": "No compression in cylinders, broken timing chain",
    },
    {
        "question": "Name the likely mechanical cause(s) for the following symptom: oil consumption.", #026
        "answer": "Worn guides, rings, or valve seals",
    },
    {
        "question": "Name the likely mechanical cause(s) for the following symptom: coolant consumption with no leak.", #027
        "answer": "Cracked head/block or blown head gasket",
    },
    {
        "question": "What two things should you consider first if you're given a vehicle with poor acceleration, backfiring, or hard starts?", #028
        "answer": "Valve timing or compression issues",
    },
    {
        "question": "Name the likely electronic cause(s) for the following symptom: surging.", #029
        "answer": "Faulty throttle position sensor or IAC",
    },
    {
        "question": "Name the likely electronic cause(s) for the following symptom: hesitation.", #030
        "answer": "Failing MAF sensor or weak ignition coil",
    },
    {
        "question": "Name the likely electronic cause(s) for the following symptom: stalling.", #031
        "answer": "IAC failure, MAP sensor error, fuel delivery issue",
    },
    {
        "question": "Name the likely electronic cause(s) for the following symptom: check-engine light (MIL).", #032
        "answer": "Stored DTCs for misfires, lean/rich codes, sensor faults",
    },
    {
        "question": "What is the main goal of a compression test?", #033
        "answer": "To measure the maximum pressure a cylinder can build during the compression stroke",
    },
    {
        "question": "What four issues could result from low compression?", #034
        "answer": "1) Poor power output, 2) rought idle or misfiring, 3) increased emissions, 4) starting difficulty",
    },
    {
        "question": "What is the range for a normal compression reading in a typical gasoline engine?", #035
        "answer": "125-175 psi",
    },
    {
        "question": "What kind of pressure differences should you expect between the cylinders during a compression test?", #036
        "answer": "All cylinders should be within 10-15% of each other",
    },
    {
        "question": "What is the procedure for a wet compression test?", #037
        "answer": "After running a dry compression test, add 1-2 teaspoons of clean engine oil into the spark plug hole of the low cylinder, then re-test compression",
    },
    {
        "question": "Following dry then wet compression tests, what is the diagnosis if compression increases significantly (20% or more)?", #038
        "answer": "Worn piston rings, because the oil temporarily seals the rings, boosting the pressure",
    },
    {
        "question": "Following dry then wet compression tests, what is the diagnosis if compression stays the same or changes very little?", #039
        "answer": "Leaking valves or blown head gasket, because the oil did not affect valve sealing",
    },
    {
        "question": "Following dry then wet compression tests, what is the diagnosis if compression is very low across all cylinders?", #040
        "answer": "Possible timing issue, severely-worn engine, or incorrect test procedure",
    },
    {
        "question": "What is the likely cause of the following compression pattern: one cylinder much lower than others.", #041
        "answer": "Burned valve, stuck valve, head gasket leak, cracked head",
    },
    {
        "question": "What is the likely cause of the following compression pattern: two adjacent cylinders low.", #042
        "answer": "Blown head gasket between cylinders",
    },
    {
        "question": "What is the likely cause of the following compression pattern: all cylinders low and even.", #043
        "answer": "Incorrect valve timing (slipped timing belt/chain), severely-worn engine",
    },
    {
        "question": "What is the likely cause of the following compression pattern: one low cylinder improves with oil.", #044
        "answer": "Worn piston rings in that cylinder",
    },
    {
        "question": "What is the likely cause of the following compression pattern: no improvement with oil.", #045
        "answer": "Valve seat leak or head gasket failure",
    },
    {
        "question": (
            "ASE SAMPLE QUESTION:\n\n"
            "A 4-cylinder engine shows the following compression readings during a dry compression test. "
            "A wet compression test on Cylinder 3 raises the reading to 145 psi. "
            "What is the MOST likely cause?\n\n"
            "A. Burned exhaust valve\n"
            "B. Worn piston rings\n"
            "C. Blown head gasket\n"
            "D. Camshaft lobe wear"
        ), #046
        "answer": (
            "B. Worn piston rings\n\n"
            "Explanation: The significant increase in compression after oil is added suggests the rings were not sealing well."
        ),
        "image": "images/cylinder_psi.png",
    },
    {
        "question": (
            "ASE SAMPLE QUESTION:\n\n"
            "A customer complains of a misfire. A compression test shows 110 psi in all cylinders (spec is 150 psi minimum). "
            "What is the MOST likely cause?\n\n"
            "A. Bad spark plugs\n"
            "B. Worn valve stem seals\n"
            "C. Incorrect camshaft timing\n"
            "D. Leaking intake gasket on one cylinder"
        ), #047
        "answer": (
            "C. Incorrect camshaft timing\n\n"
            "Explanation: Even compression that is low across all cylinders often points to cam timing problems."
        ),
    },
    {
        "question": "While compression testing tells you how much pressure a cylinder can build, leakdown testing tells you __________.", #048
        "answer": "where that pressure is going.",
    },
    {
        "question": "Once the leakdown tester is installed in the spark plug hole and compressed air is connected, read the leak percentage and listen for __________.", #049
        "answer": "air escaping from various locations.",
    },
    {
        "question": "What's the condition of the engine with the following leak percentage: 0-10%", #050
        "answer": "Excellent - like-new sealing",
    },
    {
        "question": "What's the condition of the engine with the following leak percentage: 10-20%", #051
        "answer": "Acceptable in most engines",
    },
    {
        "question": "What's the condition of the engine with the following leak percentage: 20-30%", #052
        "answer": "Marginal - warrants further inspection",
    },
    {
        "question": "What's the condition of the engine with the following leak percentage: 30% or more", #053
        "answer": "Excessive leakage - mechanical issue likely present",
    },
    {
        "question": "What's a diagnosis for hearing air escaping from around the throttle body or intake?", #054
        "answer": "Leaking iontake valve",
    },
    {
        "question": "What should you check if you hear air escaping from around the throttle body or intake?", #055
        "answer": "Burned, bent, or carboned valve; weak valve spring",
    },
    {
        "question": "What's a diagnosis for hearing air escaping from around the exhaust tailpipe?", #056
        "answer": "Leaking exhaust valve",
    },
    {
        "question": "What should you check if you hear air escaping from around the exhaust tailpipe?", #057
        "answer": "Burned valve or improper valve seat",
    },
    {
        "question": "What's a diagnosis for hearing air escaping from around the oil filler cap or dipstick tube?", #058
        "answer": "Worn or damaged piston rings",
    },
    {
        "question": "What should you check if you hear air escaping from around the oil filler cap or dipstick tube?", #059
        "answer": "Excessive ring wear, broken rings",
    },
    {
        "question": "What's a diagnosis for hearing air escaping from around the adjacent spark plug hole?", #060
        "answer": "Blown head gasket between cylinders",
    },
    {
        "question": "What should you check if you hear air escaping from around the adjacent spark plug hole?", #061
        "answer": "Coolant may also be present in oil",
    },
    {
        "question": "What's a diagnosis for hearing air escaping from around the crankcase breather or PCV valve?", #062
        "answer": "Ring blow-by",
    },
    {
        "question": "What should you check if you hear air escaping from around the crankcase brether or PCV valve?", #063
        "answer": "Normal if slight; excessive = ring damage",
    },
    {
        "question": "What problems could an intake valve leak cause?", #064
        "answer": "May cause hard starting, backfiring through intake, or poor idle",
    },
    {
        "question": "What problems could an exhaust valve leak cause?", #065
        "answer": "Associated with loss ofd power, misfire, and rough idle",
    },
    {
        "question": "What problems could piston ring wear cause?", #066
        "answer": "Results in low power, oil consumption, and blue smoke on acceleration",
    },
    {
        "question": "What problems could a blown head gasket cause?", #067
        "answer": "Often accompanied by overheating and white exhaust smoke",
    },
    {
        "question": (
            "ASE SAMPLE QUESTION:\n\n"
            "A cylinder in a 4-cylinder engine has low compression. A leakdown test shows 40% leakage with air heard at the tailpipe. "
            "What is the MOST likely cause?\n\n"
            "A. Worn piston rings\n"
            "B. Leaking intake valve\n"
            "C. Leaking exhaust valve\n"
            "D. Blown head gasket"
        ), #068
        "answer": (
            "C. Leaking exhaust valve\n\n"
            "Explanation: Air escaping through the tailpipe during a leakdown test indicates an exhaust valve sealing issue"
        ),
    },
    {
        "question": (
            "ASE SAMPLE QUESTION:\n\n"
            "During a cylinder leakdown test, a technician observes air bubbles in the radiator. "
            "What does this indicate?\n\n"
            "A. Leaking intake valve\n"
            "B. Piston ring wear\n"
            "C. Leaking exhaust valve\n"
            "D. Blown head gasket"
        ), #069
        "answer": (
            "D. Blown head gasket\n\n"
            "Explanation: Air entering the cooling system is a strong indicator of cobustion gases leaking past the head gasket into coolant passages."
        ),
    },
    {
        "question": "What is normal manifold vacuum at idle (sea level)?", #070
        "answer": "17-21 inHg (inches of mercury)",
    },
    {
        "question": "Vacuum is typically lower at idle and rises under load or WOT (wide-open throttle). True or false?", #071
        "answer": "False. Vacuum is typically higher at idle and drops under load or WOT (wide-open throttle).",
    },
    {
        "question": "What problems could a blown head gasket cause?", #072
        "answer": "Often accompanied by overheating and white exhaust smoke",
    },
    {
        "question": "What is the condition of an engine with the following vacuum reading: 17-21 inHg (steady)", #073
        "answer": "Normal engine",
    },
    {
        "question": "What is the condition of an engine with the following vacuum reading: 10-15 inHg (steady)", #074
        "answer": "Late valve timing or worn camshaft",
    },
    {
        "question": "What is the condition of an engine with the following vacuum reading: 0-5 inHg", #075
        "answer": "Severe leak, open throttle, or broken vacuum line",
    },
    {
        "question": "What is the condition of an engine with the following vacuum reading: fluctuating rapidly between high and low", #076
        "answer": "Valve issues",
    },
    {
        "question": "What is the condition of an engine with the following vacuum reading: steady low with rhythmic drop", #077
        "answer": "Blown head gasket or piston ring issue",
    },
    {
        "question": "What is the condition of an engine with the following vacuum reading: slowly dropping vacuum at idle", #078
        "answer": "Exhaust restriction",
    },
    {
        "question": "What is the condition of an engine with the following vacuum reading: quick drop and return when throttle blipped", #079
        "answer": "Normal",
    },
    {
        "question": "What is the diagnosis of an engine with the following vacuum reading: 17-21 inHg (steady)", #080
        "answer": "Strong compression, proper valve timing",
    },
    {
        "question": "What is the diagnosis of an engine with the following vacuum reading: 10-15 inHg (steady)", #081
        "answer": "Retarded timing, valve wear",
    },
    {
        "question": "What is the diagnosis of an engine with the following vacuum reading: 0-5 inHg", #082
        "answer": "Possible intake leak or valve stuck open",
    },
    {
        "question": "What is the diagnosis of an engine with the following vacuum reading: fluctuating rapidly between high and low", #083
        "answer": "Sticking valve, weak valve spring, worn cam",
    },
    {
        "question": "What is the diagnosis of an engine with the following vacuum reading: steady low with rhythmic drop", #084
        "answer": "Usually one cylinder causing loss",
    },
    {
        "question": "What is the diagnosis of an engine with the following vacuum reading: slowly dropping vacuum at idle", #085
        "answer": "Plugged catalytic converter or muffler",
    },
    {
        "question": "What is the diagnosis of an engine with the following vacuum reading: quick drop and return when throttle blipped", #086
        "answer": "Healthy engine response",
    },
    {
        "question": "What does the following vacuum pattern indicate: needle oscillates rapidly (5-10 inHg range)", #087
        "answer": "Worn valve guides or bad valve seats",
    },
    {
        "question": "What does the following vacuum pattern indicate: needle drops regularly at intervals", #088
        "answer": "Burned or sticking valve",
    },
    {
        "question": "What does the following vacuum pattern indicate: needle drops slowly, builds again", #089
        "answer": "Restricted exhaust",
    },
    {
        "question": "What does the following vacuum pattern indicate: gauge jumps under acceleration and drops too far under deceleration", #090
        "answer": "Valve spring problem or ignition misfire",
    },
    {
        "question": (
            "ASE SAMPLE QUESTION:\n\n"
            "A technician connects a vacuum gauge to a properly-warmed engine. The gauge reads a steady 10 inHg at idle. "
            "What is the MOST likely cause?\n\n"
            "A. Leaking intake manifold\n"
            "B. Late valve timing\n"
            "C. Worn valve guides\n"
            "D. Exhaust restriction"
        ), #091
        "answer": (
            "B. Late valve timing\n\n"
            "Explanation: A steady but low vacuum reading (10-15 inHg) typically points to retarded valve or ignition timing."
        ),
    },
    {
        "question": (
            "ASE SAMPLE QUESTION:\n\n"
            "During a vacuum test at idle, the needle fluctuates rapidly between 14 and 20 inHg. "
            "What does this most likely indicate?\n\n"
            "A. Sticking intake valve\n"
            "B. Exhaust restriction\n"
            "C. Worn piston rings\n"
            "D. Lean air-fuel mixture"
        ), #092
        "answer": (
            "A. Sticking intake valve\n\n"
            "Explanation: A bouncing or flickering needle usually indicates valve-sealing problems, like sticking or burned valves."
        ),
    },
    {
        "question": "What kind of information does the following parameter on an OBD-II scan tool give you: STFT/LTFT (short-/long-term fuel trim)", #093
        "answer": "How much fuel correction is applied",
    },
    {
        "question": "What kind of information does the following parameter on an OBD-II scan tool give you: MAP/MAF (manifold absolute pressure/mass airflow)", #094
        "answer": "Engine load, air volume",
    },
    {
        "question": "What kind of information does the following parameter on an OBD-II scan tool give you: RPM/crank sensor", #095
        "answer": "Engine speed and timing signal",
    },
    {
        "question": "What kind of information does the following parameter on an OBD-II scan tool give you: misfire counters (per cylinder)", #096
        "answer": "Which cylinder is misfiring",
    },
    {
        "question": "What kind of information does the following parameter on an OBD-II scan tool give you: O2 sensor voltage", #097
        "answer": "Rich or lean condition",
    },
    {
        "question": "What kind of information does the following parameter on an OBD-II scan tool give you: coolant temperature", #098
        "answer": "Confirms engine is at operating temperature",
    },
    {
        "question": "What kinds of issues can you determine from the following OBD-II scan tool parameter: STFT/LTFT (short-/long-term fuel trim)", #099
        "answer": "Vacuum leaks, bad sensors, weak compression",
    },
    {
        "question": "What kinds of issues can you determine from the following OBD-II scan tool parameter: MAP/MAF (manifold absolute pressure/mass airflow)", #100
        "answer": "Intake leaks, valve timing issues",
    },
    {
        "question": "What kinds of issues can you determine from the following OBD-II scan tool parameter: RPM/crank sensor", #101
        "answer": "Misfires, crank no-start",
    },
    {
        "question": "What kinds of issues can you determine from the following OBD-II scan tool parameter: misfire counters (per cylinder)", #102
        "answer": "Burned valve, bad injector, low compression",
    },
    {
        "question": "What kinds of issues can you determine from the following OBD-II scan tool parameter: O2 sensor voltage", #103
        "answer": "Confirms fuel-trim results",
    },
    {
        "question": "What kinds of issues can you determine from the following OBD-II scan tool parameter: coolant temperature", #104
        "answer": "Cold engine can skew trim values",
    },
    {
        "question": "What is the possible mechanical cause of the following fuel trim values: STFT +15% or more", #105
        "answer": "Vacuum leak, low compression, exhaust leak",
    },
    {
        "question": "What is the possible mechanical cause of the following fuel trim values: LTFT consistently +15-25%", #106
        "answer": "Intake valve leak, worn rings, timing issue",
    },
    {
        "question": "What is the possible mechanical cause of the following fuel trim values: STFT or LTFT excessively negative (-15% or more)", #107
        "answer": "Restricted exhaust, leaking injectors, rich condition",
    },
    {
        "question": (
            "ASE SAMPLE QUESTION:\n\n"
            "A vehicle has a P0302 code (cylinder 2 misfire). A scan tool shows cylinder 2 has a rising misfire count, and the LTFT is +18%. "
            "What is the MOST likely cause?\n\n"
            "A. Faulty spark plug\n"
            "B. Faulty injector\n"
            "C. Burned exhaust valve\n"
            "D. Oxygen sensor failure"
        ), #108
        "answer": (
            "C. Burned exhaust valve\n\n"
            "Explanation: Persistent cylinder-specific misfire + lean condition usually means compression loss, often from a valve issue."
        ),
    },
    {
        "question": (
            "A vacuum gauge reads 21 inHg steady at idle. "
            "What does this indicate?\n\n"
            "A. Valve timing issue\n"
            "B. Normal engine\n"
            "C. Exhaust restriction\n"
            "D. Vacuum leak"
        ), #109
        "answer": (
            "B. Normal engine"
        ),
    },
    {
        "question": (
            "A bouncing vacuum needle at idle likely means:\n\n"
            "A. Exhaust back pressure\n"
            "B. Sticking valve\n"
            "C. Leaking head gasket\n"
            "D. Rich mixture"
        ), #110
        "answer": (
            "B. Sticking valve"
        ),
    },
    {
        "question": (
            "Low, steady vacuum (10 inHg) suggests:\n\n"
            "A. Advanced ignition\n"
            "B. Stuck EGR\n"
            "C. Retarded valve timing\n"
            "D. Intake leak"
        ), #111
        "answer": (
            "C. Retarded valve timing"
        ),
    },
    {
        "question": (
            "Vacuum drops slowly while holding 2500 RPM. "
            "What is the MOST likely cause?\n\n"
            "A. Normal operation\n"
            "B. Valve leak\n"
            "C. Exhaust restriction\n"
            "D. Ignition fault"
        ), #112
        "answer": (
            "C. Exhaust restriction"
        ),
    },
    {
        "question": (
            "During dry compression, Cylinder 3 reads 85 psi. Wet test = 120 psi. "
            "What's the issue?\n\n"
            "A. Bad rings\n"
            "B. Bad valve\n"
            "C. Cracked head\n"
            "D. Blown gasket"
        ), #113
        "answer": (
            "A. Bad rings"
        ),
    },
    {
        "question": (
            "Dry/Wet compression = same low value. "
            "Cause?\n\n"
            "A. Worn rings\n"
            "B. Scored cylinder wall\n"
            "C. Burned valve\n"
            "D. Weak timing chain"
        ), #114
        "answer": (
            "C. Burned valve"
        ),
    },
    {
        "question": (
            "During leakdown, air is heard in intake. "
            "What is leaking?\n\n"
            "A. Piston rings\n"
            "B. Head gasket\n"
            "C. Exhaust valve\n"
            "D. Intake valve"
        ), #115
        "answer": (
            "D. Intake valve"
        ),
    },
    {
        "question": (
            "A vacuum gauge shows 5 inHg at idle. "
            "What's the most likely cause\n\n"
            "A. Retarded ignition\n"
            "B. Severe intake leak\n"
            "C. Normal idle\n"
            "D. Closed PCV valve"
        ), #116
        "answer": (
            "B. Severe intake leak"
        ),
    },
    {
        "question": (
            "MAP sensor reads high pressure at idle. Fuel trims are high positive. "
            "What does this suggest?\n\n"
            "A. Plugged injector\n"
            "B. Vacuum leak\n"
            "C. Closed throttle\n"
            "D. Rich mixture"
        ), #117
        "answer": (
            "B. Vacuum leak"
        ),
    },
    {
        "question": (
            "OBD-II shows STFT +22%, LTFT +19%, no misfire codes. "
            "Likely mechanical cause?\n\n"
            "A. Weak ignition\n"
            "B. Fuel pressure too low\n"
            "C. Intake valve leak\n"
            "D. Dirty MAF"
        ), #118
        "answer": (
            "C. Intake valve leak"
        ),
    },
    {
        "question": (
            "Cylinder 2 has high misfire count at idle, but smooth at 2500 RPM. "
            "Next step?\n\n"
            "A. Replace plug\n"
            "B. Swap coil\n"
            "C. Compression test\n"
            "D. Replace O2 sensor"
        ), #119
        "answer": (
            "C. Compression test"
        ),
    },
    {
        "question": (
            "P0171 is stored with no misfire code. STFT +18%. "
            "Best next step?\n\n"
            "A. Replace O2 sensor\n"
            "B. Check vacuum leaks\n"
            "C. Swap MAF\n"
            "D. Reset ECM"
        ), #120
        "answer": (
            "B. Check vacuum leaks"
        ),
    },
    {
        "question": (
            "Vacuum gauge steadily drops 2 inHg every 10 seconds at idle. "
            "What's the likely issue?\n\n"
            "A. Stuck-open PCV\n"
            "B. Leaking intake gasket\n"
            "C. Plugged exhaust\n"
            "D. Failing ignition coil"
        ), #121
        "answer": (
            "C. Plugged exhaust"
        ),
    },
    {
        "question": (
            "OBD-II shows misfire on all cylinders, vacuum gauge bounces between 5-15 inHg. "
            "What's likely?\n\n"
            "A. Restricted fuel supply\n"
            "B. Camshaft worn\n"
            "C. Intake valve carbon\n"
            "D. Incorrect cam timing"
        ), #122
        "answer": (
            "D. Incorrect cam timing"
        ),
    },
    {
        "question": (
            "A scan tool shows normal trims, but misfire counts high at idle for Cylinder 1. Compression = 95 psi. Wet compression = 97 psi. "
            "Diagnosis?\n\n"
            "A. Lean mixture\n"
            "B. Fuel delivery fault\n"
            "C. Valve problem\n"
            "D. Worn rings"
        ), #123
        "answer": (
            "C. Valve problems"
        ),
    },
    {
        "question": (
            "During leakdown, air heard in crankcase. "
            "Diagnosis?\n\n"
            "A. Burned valve\n"
            "B. Timing issue\n"
            "C. Piston ring wear\n"
            "D. Blown gasket"
        ), #124
        "answer": (
            "C. Piston ring wear"
        ),
    },
    {
        "question": (
            "Misfire on Cylinder 3, STFT +12%, compression 100 psi. Wet compression = 130 psi. Leakdown = 20%. "
            "What's the cause?\n\n"
            "A. Carbon buildup\n"
            "B. Ring wear\n"
            "C. Valve guide\n"
            "D. Timing fault"
        ), #125
        "answer": (
            "B. Ring wear"
        ),
    },
    {
        "question": (
            "Steady low vacuum + normal trims at idle. Misfire count = 0. "
            "What's the likely fault?\n\n"
            "A. Plug fouled\n"
            "B. Retarded timing\n"
            "C. Leaky injector\n"
            "D. EGR open"
        ), #126
        "answer": (
            "B. Retarded timing"
        ),
    },
    {
        "question": (
            "Cylinder 4 misfires only when hot. Compression normal when cold. "
            "What's next?\n\n"
            "A. Coil resistance test\n"
            "B. Thermal leakdown test\n"
            "C. PCM flash\n"
            "D. Replace injector"
        ), #127
        "answer": (
            "B. Thermal leakdown test"
        ),
    },
    {
        "question": (
            "Scan tool shows fluctuating fuel trims, vacuum needle bounces fast. "
            "What's the cause?\n\n"
            "A. Exhaust leak\n"
            "B. EGR valve stuck\n"
            "C. Sticking intake valve\n"
            "D. MAF dirty"
        ), #128
        "answer": (
            "C. Sticking intake valve"
        ),
    },
]
