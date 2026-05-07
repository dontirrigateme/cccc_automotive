#01.05 Engine Repair - Gaskets, Seals, & Fastener Service

QUESTIONS = [
    # {
    #     "question": "The head gasket forms a critical seal between __________.", #001
    #     "answer": "the engine block and cylinder head",
    # },
    # {
    #     "question": (
    #         "What three materials are head gaskets commonly made of?"
    #     ), #002
    #     "answer": (
    #         "Multi-layer steel (MLS)\n"
    #         "Composite materials\n"
    #         "Copper"
    #     ),
    # },
    # {
    #     "question": "Which head gasket material is most common in modern engines?", #003
    #     "answer": "Multi-layer steel (MLS)",
    # },
    # {
    #     "question": "Blown head gaskets often result from __________.", #004
    #     "answer": "overheating",
    # },
    # {
    #     "question": (
    #         "What three materials are intake and exhaust manifold gaskets commonly made of?"
    #     ), #005
    #     "answer": (
    #         "Graphite layered over steel or composite backing\n"
    #         "Multi-layer steel (MLS)\n"
    #         "Metal-clad composite"
    #     ),
    # },
    # {
    #     "question": (
    #         "What are two common symptoms of intake manifold gasket failure?"
    #     ), #006
    #     "answer": (
    #         "Lean condition\n"
    #         "Vacuum leak"
    #     ),
    # },
    # {
    #     "question": (
    #         "What are two common symptoms of exhaust manifold gasket failure?"
    #     ), #007
    #     "answer": (
    #         "Ticking noise\n"
    #         "Oxygen sensor errors"
    #     ),
    # },
    # {
    #     "question": (
    #         "What three materials are oil pan gaskets commonly made of?"
    #     ), #008
    #     "answer": (
    #         "Cork-rubber composite\n"
    #         "Silicone room-temperature vulcanizing (RTV) sealant\n"
    #         "Molded rubber with steel core"
    #     ),
    # },
    # {
    #     "question": (
    #         "What two materials are valve cover gaskets commonly made of?"
    #     ), #009
    #     "answer": (
    #         "Rubber or silicone\n"
    #         "Corn or cork-rubber composite"
    #     ),
    # },
    # {
    #     "question": (
    #         "What are three common symptoms of head gasket failure?"
    #     ), #010
    #     "answer": (
    #         "Overheating\n"
    #         "Coolant in oil\n"
    #         "Misfire"
    #     ),
    # },
    # {
    #     "question": (
    #         "What are two common symptoms of oil pan gasket failure?"
    #     ), #011
    #     "answer": (
    #         "Oil leaks\n"
    #         "Low oil level"
    #     ),
    # },
    # {
    #     "question": (
    #         "What are two common symptoms of valve cover gasket failure?"
    #     ), #012
    #     "answer": (
    #         "Oil on engine exterior\n"
    #         "Spark plug fouling"
    #     ),
    # },
    # {
    #     "question": "What is another term for the front crankshaft seal?", #013
    #     "answer": "Timing cover seal",
    # },
    # {
    #     "question": "What is another term for the rear crankshaft seal?", #014
    #     "answer": "Rear main seal",
    # },
    # {
    #     "question": (
    #         "What are four common symptoms of crankshaft seal failure?"
    #     ), #015
    #     "answer": (
    #         "- Oil leaking from the front or rear of the engine\n"
    #         "- Oil on the flywheel/flexplate or inside the bellhousing (rear)\n"
    #         "- Oil sling on the crank pulley or belts (front)\n"
    #         "- Low oil levels and oil on driveway or undercarriage"
    #     ),
    # },
    # {
    #     "question": (
    #         "Camshaft seals are rare in overhead cam (OHC) engines. True or false?"
    #     ), #016
    #     "answer": (
    #         "False.\n"
    #         "These are common in overhead cam (OHC) engines and are usually located behind the timing gear or sprocket."
    #     ),
    # },
    # {
    #     "question": (
    #         "What are three common symptoms of camshaft seal failure?"
    #     ), #017
    #     "answer": (
    #         "- Oil leaks from the front of the engine\n"
    #         "- Contamination of timing belt (can lead to belt degradation)\n"
    #         "- Oil-burning smells or oil dripping near the front of the engine"
    #     ),
    # },
    # {
    #     "question": (
    #         "What are two uses for room-temperature vulcanizing (RTV) silicone?"
    #     ), #018
    #     "answer": (
    #         "- Gasket substitute (e.g., sealing timing covers, oil pans)\n"
    #         "- Gasket supplement, applied at seams or corners (e.g., junction of timing cover and oil pan)"
    #     ),
    # },
    # {
    #     "question": (
    #         "What are three types of room-temperature vulcanizing (RTV) silicone?"
    #     ), #019
    #     "answer": (
    #         "Oil-resistant RTV\n"
    #         "Sensor-safe RTV\n"
    #         "High-temp RTV"
    #     ),
    # },
    # {
    #     "question": "How were rope seals traditionally used?", #020
    #     "answer": "As rear main seals in older engines (especially pre-1980s domestic and industrial engines)",
    # },
    # {
    #     "question": (
    #         "What are two common symptoms of rope seal failure?"
    #     ), #021
    #     "answer": (
    #         "- Persistent oil leak at rear main, often slow and steady\n"
    #         "- Oil accumulation around the rear of the oil pan or bellhousing"
    #     ),
    # },
    # {
    #     "question": "How do you ensure even load distribution across sealing surfaces when torquing a cylinder head?", #022
    #     "answer": "Move from the center outward in a spiral or cross pattern",
    # },
    # {
    #     "question": "Standard bolts are torqued to a specific value within their elastic range, meaning they can return to their original shape if removed. True or false?", #023
    #     "answer": "True",
    # },
    # {
    #     "question": (
    #         "Standard bolts are not typically reusable. True or false?"
    #     ), #024
    #     "answer": (
    #         "False.\n"
    #         "These bolts are typically reusable if they are not damaged or stretched beyond specification."
    #     ),
    # },
    # {
    #     "question": "Torque-to-yield (TTY) bolts are tightened beyond the yield point into the plastic deformation zone, where they permanently stretch to maintain clamping force. True or false?", #025
    #     "answer": "True",
    # },
    # {
    #     "question": (
    #         "Torque-to-yield (TTY) bolts are not reusable. True or false?"
    #     ), #026
    #     "answer": (
    #         "True.\n"
    #         "Once stretched, they must be replaced."
    #     ),
    # },
    # {
    #     "question": (
    #         "What are two common applications for standard bolts?"
    #     ), #027
    #     "answer": (
    #         "Oil pans\n"
    #         "Accessory brackets"
    #     ),
    # },
    # {
    #     "question": (
    #         "What are two common applications for torque-to-yield (TTY) bolts?"
    #     ), #028
    #     "answer": (
    #         "Cylinder heads\n"
    #         "Main bearing caps"
    #     ),
    # },
    # {
    #     "question": (
    #         "What are four common causes of stripped threads?"
    #     ), #029
    #     "answer": (
    #         "- Over-tightening fasteners beyond torque spec\n"
    #         "- Cross-threading during installation\n"
    #         "- Corrosion and thread galling (especially in aluminum)\n"
    #         "- Improper use of power tools or impact drivers"
    #     ),
    # },
    # {
    #     "question": (
    #         "What are three symptoms of stripped threads?"
    #     ), #030
    #     "answer": (
    #         "- Bolt spins without tightening\n"
    #         "- Inability to torque to spec\n"
    #         "- Coolant, oil, or compression leaks at the joint"
    #     ),
    # },
    # {
    #     "question": "What are helicoil inserts?", #031
    #     "answer": "Helicoils (or similar thread inserts like Time-Sert) are coiled wire or solid inserts used to restore damaged threads",
    # },
    # {
    #     "question": (
    #         "What do you use to repair stripped threads?"
    #     ), #032
    #     "answer": (
    #         "Helicoil\n"
    #         "Solid inserts"
    #     ),
    # },
    # {
    #     "question": (
    #         "What tool(s) is/are required to repair stripped threads?"
    #     ), #033
    #     "answer": (
    #         "Drill\n"
    #         "Tap\n"
    #         "Insert tool"
    #     ),
    # },
    # {
    #     "question": (
    #         "What do you use to repair a broken exposed stud?"
    #     ), #034
    #     "answer": (
    #         "Double-nut\n"
    #         "Stud extractor"
    #     ),
    # },
    # {
    #     "question": (
    #         "What tool(s) is/are required to repair a broken exposed stud?"
    #     ), #035
    #     "answer": (
    #         "Wrenches\n"
    #         "Extractor tool"
    #     ),
    # },
    # {
    #     "question": "What do you use to repair a broken flush stud?", #036
    #     "answer": "Drill + Easy-Out extractor",
    # },
    # {
    #     "question": (
    #         "What tool(s) is/are required to repair a broken flush stud?"
    #     ), #037
    #     "answer": (
    #         "Drill bits\n"
    #         "Extractor"
    #     ),
    # },
    # {
    #     "question": (
    #         "What do you use to repair corroded thread holes?"
    #     ), #038
    #     "answer": (
    #         "Clean the thread holes\n"
    #         "Chase threads\n"
    #         "Insert"
    #     ),
    # },
    # {
    #     "question": (
    #         "What tool(s) is/are required to repair corroded thread holes?"
    #     ), #039
    #     "answer": (
    #         "Thread chaser\n"
    #         "Tap/Die"
    #     ),
    # },
    {
        "question": ( #01
            "What is the main function of a head gasket?\n\n"
            "A.Increase oil pressure\n"
            "B. Reduce fuel consumption\n"
            "C. Lubricate valves\n"
            "D. Seal combustion, coolant, and oil passages"
        ), #040
        "answer": (
            "D. Seal combustion, coolant, and oil passages"
        ),
    },
    {
        "question": ( #02
            "What gasket is commonly used between the intake manifold and cylinder head?\n\n"
            "A. Oil pan gasket\n"
            "B. Exhaust gasket\n"
            "C. Valve cover gasket\n"
            "D. Intake gasket"
        ), #041
        "answer": (
            "D. Intake gasket"
        ),
    },
    {
        "question": ( #03
            "What is a common sign of a leaking valve cover gasket?\n\n"
            "A. Coolant loss\n"
            "B. Rough idle\n"
            "C. Oil on the outside of the engine\n"
            "D. White exhaust smoke"
        ), #042
        "answer": (
            "C. Oil on the outside of the engine"
        ),
    },
    {
        "question": ( #04
            "What is the function of a crankshaft seal?\n\n"
            "A. Seal the cylinder head\n"
            "B. Lubricate the crankshaft\n"
            "C. Provide combustion sealing\n"
            "D. Prevent oil leaks at crankshaft ends"
        ), #043
        "answer": (
            "D. Prevent oil leaks at crankshaft ends"
        ),
    },
    {
        "question": ( #05
            "What can cause premature gasket failure?\n\n"
            "A. Incorrect torque\n"
            "B. Overheating\n"
            "C. Poor surface prep\n"
            "D. All of the above"
        ), #044
        "answer": (
            "D. All of the above"
        ),
    },
    {
        "question": ( #06
            "What material is commonly used for modern multi-layer steel (MLS) head gaskets?\n\n"
            "A. Rubber\n"
            "B. Cork\n"
            "C. Aluminum\n"
            "D. Steel"
        ), #045
        "answer": (
            "D. Steel"
        ),
    },
    {
        "question": ( #07
            "Which gasket seals the oil pan to the engine block?\n\n"
            "A. Valve cover gasket\n"
            "B. Intake gasket\n"
            "C. Head gasket\n"
            "D. Oil pan gasket"
        ), #046
        "answer": (
            "D. Oil pan gasket"
        ),
    },
    {
        "question": ( #08
            "Which seal type is most likely to be used at the rear of the crankshaft?\n\n"
            "A. Rope seal\n"
            "B. Paper seal\n"
            "C. O-ring\n"
            "D. Crush washer"
        ), #047
        "answer": (
            "A. Rope seal"
        ),
    },
    {
        "question": ( #09
            "What is a common material used for valve cover gaskets?\n\n"
            "A. Cork\n"
            "B. Copper\n"
            "C. Teflon\n"
            "D. Steel"
        ), #048
        "answer": (
            "A. Cork"
        ),
    },
    {
        "question": ( #10
            "What type of sealant is commonly used on RTV applications?\n\n"
            "A. Paper\n"
            "B. Anaerobic\n"
            "C. RTV silicone\n"
            "D. Teflon paste"
        ), #049
        "answer": (
            "C. RTV silicone"
        ),
    },
    {
        "question": ( #11
            "Which seal would be found at the camshaft exit point in the engine block?\n\n"
            "A. Rear main seal\n"
            "B. Intake seal\n"
            "C. Camshaft seal\n"
            "D. Freeze plug"
        ), #050
        "answer": (
            "C. Camshaft seal"
        ),
    },
    {
        "question": ( #12
            "What should be done before installing a gasket?\n\n"
            "A. Overtorque bolts\n"
            "B. Leave old gasket in place\n"
            "C. Apply grease\n"
            "D. Clean and inspect sealing surfaces"
        ), #051
        "answer": (
            "D. Clean and inspect sealing surfaces"
        ),
    },
    {
        "question": ( #13
            "What torquing pattern is commonly used on cylinder heads?\n\n"
            "A. Random order\n"
            "B. From edges to center\n"
            "C. From rear to front\n"
            "D. From center outward in sequence"
        ), #052
        "answer": (
            "D. From center outward in sequence"
        ),
    },
    {
        "question": ( #14
            "What is a torque-to-yield (TTY) bolt?\n\n"
            "A. Reusable head bolt\n"
            "B. Measured only by torque wrench\n"
            "C. Always tightened by feel\n"
            "D. One-time-use bolt stretched to precise yield point"
        ), #053
        "answer": (
            "D. One-time-use bolt stretched to precise yield point"
        ),
    },
    {
        "question": ( #15
            "What is a common reason for stripped threads during assembly?\n\n"
            "A. Using thread sealant\n"
            "B. Under-tightening bolts\n"
            "C. Cross-threading or overtightening\n"
            "D. Thread-locking compound"
        ), #054
        "answer": (
            "C. Cross-threading or overtightening"
        ),
    },
    {
        "question": ( #16
            "How are damaged threads commonly repaired?\n\n"
            "A. Use longer bolts\n"
            "B. Grease the bolt\n"
            "C. Replace the entire engine\n"
            "D. Install a thread insert like Helicoil"
        ), #055
        "answer": (
            "D. Install a thread insert like Helicoil"
        ),
    },
    {
        "question": ( #17
            "Which tool is used to repair a stripped thread hole?\n\n"
            "A. Compression tester\n"
            "B. Thread chaser\n"
            "C. Feeler gauge\n"
            "D. Torque-angle gauge"
        ), #056
        "answer": (
            "B. Thread chaser"
        ),
    },
    {
        "question": ( #18
            "What does a torque angle gauge measure?\n\n"
            "A. Oil pressure\n"
            "B. Thread pitch\n"
            "C. Bolt length\n"
            "D. Degrees of rotation after initial torque"
        ), #057
        "answer": (
            "D. Degrees of rotation after initial torque"
        ),
    },
    {
        "question": ( #19
            "What is the purpose of angle-tightening bolts?\n\n"
            "A. Make reuse easier\n"
            "B. Stretch bolt to specified tension\n"
            "C. Reduce clamping force\n"
            "D. Prevent gasket sealing"
        ), #058
        "answer": (
            "B. Stretch bolt to specified tension"
        ),
    },
    {
        "question": ( #20
            "Which of the following requires re-torquing in a specific sequence and angle?\n\n"
            "A. Oil pan\n"
            "B. Timing cover\n"
            "C. Valve cover\n"
            "D. Cylinder head"
        ), #059
        "answer": (
            "D. Cylinder head"
        ),
    },
]
