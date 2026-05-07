#01.06 Engine Repair - General Engine Reassembly

QUESTIONS = [
    # {
    #     "question": (
    #         "What can be used to clean the engine block?"
    #     ), #001
    #     "answer": (
    #         "Hot-tanking cleaners\n"
    #         "Pressure-washing cleaners\n"
    #         "Solvent-based cleaners"
    #     ),
    # },
    # {
    #     "question": "How is compressed air used to clean an engine?", #002
    #     "answer": "Blow out oil galleries and coolant passages with compressed air after washing. Ensure no water or debris remains.",
    # },
    # {
    #     "question": "What tools are used to check valve-to-piston clearance?", #003
    #     "answer": "Clay or feeler gauges",
    # },
    # {
    #     "question": "In a 4-stroke engine, how often does the crankshaft turn?", #004
    #     "answer": "Twice for every one camshaft revolution",
    # },
    # {
    #     "question": (
    #         "What are some common timing components?"
    #     ), #005
    #     "answer": (
    #         "Crankshaft gear/sprocket\n"
    #         "Camshaft gear(s)/sprocket(s)\n"
    #         "Timing belt or chain\n"
    #         "Tensioners and guides\n"
    #         "Balance shaft sprockets (on some engines)"
    #     ),
    # },
    # {
    #     "question": (
    #         "What is the basic procedure for aligning the timing system?"
    #     ), #006
    #     "answer": (
    #         "1 - Rotate crankshaft to top dead center (TDC) on the compression stroke for cylinder #1\n"
    #         "2 - Align crankshaft gear mark with its reference point (often a notch or dot)\n"
    #         "3 - Align camshaft gear(s) to their respective marks (which might be on the backing plate, cylinder head, or valve cover mating surface)\n"
    #         "4 - Install chain or belt without disturbing gear positions"
    #     ),
    # },
    # {
    #     "question": "Some dual overhead cam (DOHC) engines require a camshaft alignment tool to hold both cams in position during timing. True or false?", #007
    #     "answer": "True",
    # },
    # {
    #     "question": (
    #         "You should NOT lubricate before an engine's first start-up. True or false?"
    #     ), #008
    #     "answer": (
    #         "False.\n"
    #         "Lubrication before an engine's first start-up is critical. Most engine damage during a rebuild occurs during the initial seconds of the first start-up due to dry metal-to-metal contact. Proper preparation ensures a smooth, safe break-in."
    #     ),
    # },
    # {
    #     "question": (
    #         "Where is assembly lube applied?"
    #     ), #009
    #     "answer": (
    #         "Camshaft lobes and journals\n"
    #         "Main and rod bearings\n"
    #         "Lifter bases and pushrods\n"
    #         "Rocker arms and valve tips\n"
    #         "Timing components (light coating)\n"
    #         "Oil pump gears and shaft (if external)"
    #     ),
    # },
    # {
    #     "question": "What protects bearings before oil pressure builds up?", #010
    #     "answer": "Assembly lube",
    # },
    # {
    #     "question": "What tool is used to spin the oil pump before start-up?", #011
    #     "answer": "Drill + priming tool",
    # },
    # {
    #     "question": "What should be done immediately upon starting an assembled engine?", #012
    #     "answer": "Set RPM to 1,500-2,000 and hold it steady for the first 20-30 minutes",
    # },
    # {
    #     "question": "What is the reason for holding a high idle on first start-up?", #013
    #     "answer": "Ensures camshaft and lifter lubrication",
    # },
    # {
    #     "question": "What should be done if oil pressure is low on first start-up?", #014
    #     "answer": "The engine should be shut off immediately",
    # },
    # {
    #     "question": "A leakdown test is more accurate for pinpointing problems than compression test alone. True or false?", #013
    #     "answer": "True",
    # },
    {
        "question": ( #01
            "What is the main purpose of applying assembly lube during engine reassembly?\n\n"
            "A. Reduce friction during initial start\n"
            "B. Seal gasket surfaces\n"
            "C. Prevent coolant leaks\n"
            "D. Increase oil pressure"
        ), #014
        "answer": (
            "A. Reduce friction during initial start"
        ),
    },
    {
        "question": ( #02
            "Which type of bolt requires tightening to a specified torque and then an additional angle?\n\n"
            "A. Standard bolt\n"
            "B. Torque-to-yield (TTY) bolt\n"
            "C. Threaded stud\n"
            "D. Grade 5 bolt"
        ), #015
        "answer": (
            "B. Torque-to-yield (TTY) bolt"
        ),
    },
    {
        "question": ( #03
            "What is a common cause of gasket failure due to improper bolt tightening?\n\n"
            "A. Under-torquing\n"
            "B. Over-torquing\n"
            "C. Uneven torque sequence\n"
            "D. All of the above"
        ), #016
        "answer": (
            "D. All of the above"
        ),
    },
    {
        "question": ( #04
            "Which seal type is most flexible and often used around irregular engine components?\n\n"
            "A. O-ring\n"
            "B. Rope seal\n"
            "C. Metal crush washer\n"
            "D. Paper gasket"
        ), #017
        "answer": (
            "B. Rope seal"
        ),
    },
    {
        "question": ( #05
            "What does thread chasing involve?\n\n"
            "A. Installing new threads\n"
            "B. Cleaning and restoring damaged threads\n"
            "C. Replacing the bolt\n"
            "D. Welding stripped threads"
        ), #018
        "answer": (
            "B. Cleaning and restoring damaged threads"
        ),
    },
    {
        "question": ( #06
            "When installing a head gasket, what should be done first?\n\n"
            "A. Lubricate bolt threads\n"
            "B. Clean sealing surfaces\n"
            "C. Apply RTV sealant\n"
            "D. Torque bolts fully"
        ), #019
        "answer": (
            "B. Clean sealing surfaces"
        ),
    },
    {
        "question": ( #07
            "Which tool is best suited for checking bolt torque angle during tightening?\n\n"
            "A. Torque wrench\n"
            "B. Torque angle gauge\n"
            "C. Dial indicator\n"
            "D. Feeler gauge"
        ), #020
        "answer": (
            "B. Torque angle gauge"
        ),
    },
    {
        "question": ( #08
            "What type of sealant is typically used to seal metal-to-metal engine joints?\n\n"
            "A. RTV silicone\n"
            "B. Grease\n"
            "C. Anaerobic sealant\n"
            "D. Threadlocker"
        ), #021
        "answer": (
            "C. Anaerobic sealant"
        ),
    },
    {
        "question": ( #09
            "What is the main reason to avoid reusing torque-to-yield (TTY) bolts?\n\n"
            "A. They are too short\n"
            "B. They stretch and lose strength\n"
            "C. They corrode quickly\n"
            "D. They are hard to remove"
        ), #022
        "answer": (
            "B. They stretch and lose strength"
        ),
    },
    {
        "question": ( #10
            "Which gasket material is compressible and often used for valve covers?\n\n"
            "A. Steel\n"
            "B. Rubber\n"
            "C. Cork\n"
            "D. Composite"
        ), #023
        "answer": (
            "C. Cork"
        ),
    },
    {
        "question": ( #11
            "When should a rope seal be used?\n\n"
            "A. Sealing coolant passages\n"
            "B. Rear main crankshaft seals\n"
            "C. Intake manifold gaskets\n"
            "D. Oil filter gaskets"
        ), #024
        "answer": (
            "B. Rear main crankshaft seals"
        ),
    },
    {
        "question": ( #12
            "What happens if you tighten bolts in the wrong sequence?\n\n"
            "A. Bolt stretching\n"
            "B. Uneven gasket compression\n"
            "C. Thread damage\n"
            "D. Increased oil pressure"
        ), #025
        "answer": (
            "B. Uneven gasket compression"
        ),
    },
    {
        "question": ( #13
            "What tool is typically used to remove a stuck stud?\n\n"
            "A. Stud extractor\n"
            "B. Torque wrench\n"
            "C. Thread chaser\n"
            "D. Impact wrench"
        ), #026
        "answer": (
            "A. Stud extractor"
        ),
    },
    {
        "question": ( #14
            "Which type of bolt is designed to stretch slightly to create a stronger clamp load?\n\n"
            "A. Grade 2\n"
            "B. Torque-to-yield (TTY)\n"
            "C. Flanged bolt\n"
            "D. Self-locking bolt"
        ), #027
        "answer": (
            "B. Torque-to-yield (TTY)"
        ),
    },
    {
        "question": ( #15
            "What is the most important step before installing any seal?\n\n"
            "A. Heating the seal\n"
            "B. Cleaning the sealing surface\n"
            "C. Applying oil\n"
            "D. Tightening bolts"
        ), #028
        "answer": (
            "B. Cleaning the sealing surface"
        ),
    },
    {
        "question": ( #16
            "Which of the following is NOT a common cause of seal leaks?\n\n"
            "A. Incorrect installation\n"
            "B. Worn sealing surface\n"
            "C. Using the wrong gasket material\n"
            "D. Proper torque"
        ), #029
        "answer": (
            "D. Proper torque"
        ),
    },
    {
        "question": ( #17
            "What is the primary function of a valve cover gasket?\n\n"
            "A. Prevent oil leaks\n"
            "B. Seal coolant passages\n"
            "C. Increase compression\n"
            "D. Seal combustion gases"
        ), #030
        "answer": (
            "A. Prevent oil leaks"
        ),
    },
    {
        "question": ( #18
            "How should bolts be lubricated when specified in the service manual?\n\n"
            "A. Use engine oil\n"
            "B. Use anti-sieze compound\n"
            "C. Leave dry\n"
            "D. Use grease"
        ), #031
        "answer": (
            "A. Use engine oil"
        ),
    },
    {
        "question": ( #19
            "Which of the following requires precise cleaning and no use of sealants during installation?\n\n"
            "A. Head gasket\n"
            "B. Oil pan gasket\n"
            "C. Valve cover gasket\n"
            "D. Intake manifold gasket"
        ), #032
        "answer": (
            "A. Head gasket"
        ),
    },
    {
        "question": ( #20
            "Why is it important to follow the torque sequence when tightening cylinder head bolts?\n\n"
            "A. To prevent bolt breakage\n"
            "B. To ensure even gasket compression\n"
            "C. To save time\n"
            "D. To prevent thread stripping"
        ), #033
        "answer": (
            "B. To ensure even gasket compression"
        ),
    },
]
