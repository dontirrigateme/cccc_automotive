#01.03 Engine Repair - Engine Block Diagnosis & Repair

QUESTIONS = [
    {
        "question": "What is a short block?", #001
        "answer": "The core lower assembly of an engine",
    },
    {
        "question": "What components does the short block include?", #002
        "answer": "Pistons, connecting rods, crankshaft, bearings, and timing gear",
    },
    {
        "question": "What is a piston?", #003
        "answer": "A cylindrical component that moves up and down within the engine cylinders, usually made of lightweight aluminum alloys for strength and heat resistance.",
    },
    {
        "question": "What is a piston's function?", #004
        "answer": "To convert expanding combustion gases into mechanical force, with rings that seal the combustion chamber, control oil consumption, and transfer heat to the cylinder walls.",
    },
    {
        "question": "What is the function of the connecting rods?", #005
        "answer": "These link the pistons to the crankshaft. The rods transfer the linear motion of the pistons into rotational motion.",
    },
    {
        "question": "What is the function of the crankshaft?", #006
        "answer": "It converts the reciprocating motion of the pistons into rotational motion that ultimately powers the drivetrain.",
    },
    {
        "question": "Where/On what components in the short block would someone find bearings?", #007
        "answer": "Main bearings, which support the crankshaft in the engine block, and rod bearings, which connect the rods to the crankshaft journals.",
    },
    {
        "question": "What is the function of the timing gear, belt, and/or chain?", #008
        "answer": "Making up the timing system, these parts synchronize the crankshaft's rotation with the camshaft(s) to ensure that valves open and close at the correct times during the combustion cycle.",
    },
    {
        "question": "What are the most frequently encountered problems in a short block?", #009
        "answer": "Scored cylinders, cracked blocks, and low oil pressure",
    },
    {
        "question": "How do scored cylinders cause engine problems?", #010
        "answer": "Deep scratches/grooves compromise the smooth surface required for piston rings to seal properly, resulting in reduced compression, increased oil consumption, and engine smoking.",
    },
    {
        "question": "How is a scored cylinder addressed during service?", #011
        "answer": "A severely scored cylinder usually required cylinder reboring or replacement",
    },
    {
        "question": "What causes a scored cylinder?", #012
        "answer": "Debris, insufficient lubrication, or overheating",
    },
    {
        "question": "What causes a cracked block?", #013
        "answer": "Extreme overheating, freezing of coolant inside the block, or manufacturing defects",
    },
    {
        "question": "What effect does a cracked block have on an engine?", #014
        "answer": "Cracks often lead to coolant leaks, mixing of oil and coolant, and loss of compression.",
    },
    {
        "question": "What are some symptoms of a cracked block?", #015
        "answer": "Overheating, white smoke from the exhaust, milky oil contamination.",
    },
    {
        "question": "How is a cracked block addressed during service?", #016
        "answer": "Repair may involve welding, use of block sealants, or complete engine replacement (depending on severity)",
    },
    {
        "question": "What are some causes of low oil pressure related to the short block?", #017
        "answer": "Causes related to the block include worn main and rod bearings, clogged oil galleries, or a failing oil pump housed near the block.",
    },
    {
        "question": "What are some synmptoms of low oil pressure?", #018
        "answer": "Engine knocking, warning lights, and abnormal oil pressure gauge readings.",
    },
    {
        "question": "How is low oil pressure diagnosed?", #019
        "answer": "Diagnosis involves checking oil level, oil pump function, bearing clearances, and inspecting for block or gallery obstructions.",
    },
    {
        "question": "How is low oil pressure addressed during service?", #020
        "answer": "Resolving low oil pressure often requires bearing replacement, oil pump servicing, or thorough block cleaning.",
    },
    {
        "question": "What are some precision tools that are used to measure components during engine service?", #021
        "answer": "Micrometers, bore gauges, and plastigage.",
    },
    {
        "question": "What is a micrometer?", #022
        "answer": "A precision measuring tool that provides highly accurate measurements of component diameters and thicknesses, usually to the nearest thousandth of an inch (0.001 in).",
    },
    {
        "question": "What short block components are usually measured with a micrometer?", #023
        "answer": "Crankshaft journal diameters, piston diameters, and other cylindrical parts to determine wear and whether parts can be machined or require replacement",
    },
    {
        "question": "What is a bore gauge?", #024
        "answer": "A bore gauge is a precision measuring instrument used to accurately measure the inside diameter of holes, cylinders, or bores",
    },
    {
        "question": "What parts in a short block are measured with a bore gauge?", #025
        "answer": "Bore gauges measure the internal diameter of cylinders or bearing bores. They detect wear patterns, out-of-round conditions (oval shapes), and taper (diameter variations along the cylinder length).",
    },
    {
        "question": "How is a bore gauge used when measuring parts?", #026
        "answer": "Using a bore gauge involves inserting it into the cylinder and adjusting the gauge to find the smallest diameter point, then comparing it to factory specifications.",
    },
    {
        "question": "What is plastigage?", #027
        "answer": "It's a thin strip of deformable plastic material used to measure small clearances between fitted metal parts.",
    },
    {
        "question": "What block components are measured with plastigage?", #028
        "answer": "It is used to measure the bearing clearances between journals and bearing surfaces.",
    },
    {
        "question": "How is plastigage used to measure block components?", #029
        "answer": "It is placed between the crankshaft journal and bearing shell, then compressed by tightening the bearing cap to specification. After removal, the width of the flattened plastigage strip is compated to a clearance chart to determine the oil clearance.",
    },
    {
        "question": "What can happen if dimensional tolerances of crankshaft journals and bearing clearances are exceeded?", #030
        "answer": "Exceeding these tolerances risks premature wear, loss of oil pressure, or catastrophic failure.",
    },
    {
        "question": "What is the typical tolerance range for a crankshaft journal diameter?", #031
        "answer": "Usually ranges between 1.850 to 2.000 inches",
    },
    {
        "question": "What is the typical tolerance range for the bearing clearance of main and rod bearings?", #032
        "answer": "Typical oil clearance is 0.001 to 0.003 inches",
    },
    {
        "question": "What is the typical tolerance range for a cylinder bore diameter?", #033
        "answer": "Varies widely by engine, but typical values range from 3.000 to 4.000 inches",
    },
    {
        "question": "What is the typical tolerance range for piston-to-cylinder clearance?", #034
        "answer": "Usually between 0.001 and 0.003 inches",
    },
    {
        "question": "What two things are measured to ensure engine durability and smooth operation?", #035
        "answer": "Crankshaft end play and crankshaft runout",
    },
    {
        "question": "What is crankshaft end play?", #036
        "answer": "The axial (front-to-back_) movement of the crankshaft within the engine block",
    },
    {
        "question": "What is crankshaft runout?", #037
        "answer": "Runout measures the crankshaft's bending or warping along its length",
    },
    {
        "question": "What can excessive crankshaft end play cause?", #038
        "answer": "Excessive end play can lead to misalignment of the crankshaft, damage to thrust bearings, oil seal leaks, and abnormal engine noise",
    },
    {
        "question": "What can excessive crankshaft runout cause?", #039
        "answer": "Excessive runout causes vibrations, uneven bearing wear, and can lead to catastrophic engine failure.",
    },
    {
        "question": "What are two common cylinder wall wear patterns that impact engine efficiency?", #040
        "answer": "Taper and out-of-round",
    },
    {
        "question": "How does tapered cylinder wear affect the engine?", #041
        "answer": "It can cause uneven piston ring sealing, leading to blow-by, reduced compression, and increased oil comsumption.",
    },
    {
        "question": "How does out-of-round cylinder wear affect the engine?", #042
        "answer": "This condition causes piston rings to not seat properly around the entire circumference, resulting in compression loss and uneven wear.",
    },
    {
        "question": "What are the repair options for cylinders that are tapered or out-of-round?", #043
        "answer": "Reboring and honing, and sleeving",
    },
    {
        "question": "How is a cylinder rebored and honed?", #044
        "answer": "Cylinders exceeding wear limits are machined to a larger, uniform diameter and then honed to restore proper surface finish and geometry. Oversized pistons and rings are installed accordingly.",
    },
    {
        "question": "How is a cylinder sleeved?", #045
        "answer": "For severely worn or damaged cylinders, a metal alseve can be inserted to restore bore dimensions, avoiding the need for excessive overboring.",
    },
    {
        "question": (
            "What is a common cause of scored cylinder walls?\n\n"
            "A. Overheating\n"
            "B. Lack of lubrication\n"
            "C. Excessive valve lash\n"
            "D. Dirty air filter"
        ), #046
        "answer": (
            "B. Lack of lubrication"
        ),
    },
    {
        "question": (
            "Cracks in the engine block usually occur due to:\n\n"
            "A. Overcooling\n"
            "B. Engine overheating\n"
            "C. Loe oil pressure\n"
            "D. Incorrect spark timing"
        ), #047
        "answer": (
            "B. Engine overheating"
        ),
    },
    {
        "question": (
            "What tool is used to measure cylinder bore diameter accurately?\n\n"
            "A. Dial bore gauge\n"
            "B. Torque wrench\n"
            "C. Feeler gauge\n"
            "D. Compression tester"
        ), #048
        "answer": (
            "A. Dial bore gauge"
        ),
    },
    {
        "question": (
            "Plastigage is used to measure:\n\n"
            "A. Bearing clearance\n"
            "B. Valve lash\n"
            "C. Compression pressure\n"
            "D. Crankshaft runout"
        ), #049
        "answer": (
            "A. Bearing clearance"
        ),
    },
    {
        "question": (
            "Excessive crankshaft end play can cause:\n\n"
            "A. Bearing damage\n"
            "B. Valve float\n"
            "C. Low oil pressure\n"
            "D. Overheating"
        ), #050
        "answer": (
            "A. Bearing damage"
        ),
    },
    {
        "question": (
            "Typical cause of crankshaft runout is:\n\n"
            "A. Bent crankshaft\n"
            "B. Worn pistons\n"
            "C. Sticking lifters\n"
            "D. Broken valve springs"
        ), #051
        "answer": (
            "A. Bent crankshaft"
        ),
    },
    {
        "question": (
            "A cylinder bore that is out-of-round can cause:\n\n"
            "A. Excessive oil consumption\n"
            "B. Poor fuel economy\n"
            "C. Engine overheating\n"
            "D. Misfires"
        ), #052
        "answer": (
            "A. Excessive oil consumption"
        ),
    },
    {
        "question": (
            "Which of these is a common sign of low oil pressure in an engine block?\n\n"
            "A. Bearing damage\n"
            "B. Valve noise\n"
            "C. High compression\n"
            "D. Spark knock"
        ), #053
        "answer": (
            "A. Bearing damage"
        ),
    },
    {
        "question": (
            "When measuring crankshaft end play, what instrument is commonly used?\n\n"
            "A. Dial indicator\n"
            "B. Torque wrench\n"
            "C. Dial bore gauge\n"
            "D. Compression tester"
        ), #054
        "answer": (
            "A. Dial indicator"
        ),
    },
    {
        "question": (
            "A cylinder bore taper greater than specifications typically requires:\n\n"
            "A. Boring and honing\n"
            "B. Valve adjustment\n"
            "C. Head gasket replacement\n"
            "D. Ignition timing reset"
        ), #055
        "answer": (
            "A. Boring and honing"
        ),
    },
    {
        "question": (
            "What is the usual cause of low oil pressure related to the engine block?\n\n"
            "A. Worn bearings\n"
            "B. Sticking valves\n"
            "C. Broken timing belt\n"
            "D. Faulty spark plugs"
        ), #056
        "answer": (
            "A. Worn bearings"
        ),
    },
    {
        "question": (
            "What happens if crankshaft runout exceeds limits?\n\n"
            "A. Engine vibration and bearing failure\n"
            "B. Improved power\n"
            "C. Lower oil consumption\n"
            "D. Quieter engine"
        ), #057
        "answer": (
            "A. Engine vibration and bearing failure"
        ),
    },
    {
        "question": (
            "What component prevents metal-to-metal contact on the crankshaft?\n\n"
            "A. Bearings\n"
            "B. Pistons\n"
            "C. Valve springs\n"
            "D. Camshaft"
        ), #058
        "answer": (
            "A. Bearings"
        ),
    },
    {
        "question": (
            "What is an effect of scored cylinders?\n\n"
            "A. Reduced compression and increased oil consumption\n"
            "B. Increased horsepower\n"
            "C. Reduced fuel consumption\n"
            "D. Quieter engine"
        ), #059
        "answer": (
            "A. Reduced compression and increased oil consumption"
        ),
    },
    {
        "question": (
            "When using plastigage, the clearance measurement is based on:\n\n"
            "A. Width of crushed plastigage strip\n"
            "B. Color change\n"
            "C. Length of plastigage strip\n"
            "D. Sound made"
        ), #060
        "answer": (
            "A. Width of crushed plastigage strip"
        ),
    },
    {
        "question": (
            "What's a possible cause of of cracked engine blocks?\n\n"
            "A. Overheating and freeze damage\n"
            "B. Incorrect oil viscosity\n"
            "C. Bad spark plugs\n"
            "D. Dirty fuel"
        ), #061
        "answer": (
            "A. Overheating and freeze damage"
        ),
    },
    {
        "question": (
            "How often should timing gears be inspected on an engine block?\n\n"
            "A. During major engine overhaul\n"
            "B. Every oil change\n"
            "C. Every 500 miles\n"
            "D. Never"
        ), #062
        "answer": (
            "A. During major engine overhaul"
        ),
    },
    {
        "question": (
            "What does excessive cylinder wall wear cause?\n\n"
            "A. Loss of compression and oil burning\n"
            "B. Increased compression\n"
            "C. Better fuel economy\n"
            "D. Reduced emissions"
        ), #063
        "answer": (
            "A. Loss of compression and oil burning"
        ),
    },
    {
        "question": (
            "What indicates a need to measure crankshaft end play?\n\n"
            "A. Abnormal engine noise or vibration\n"
            "B. Regular oil change\n"
            "C. Low coolant\n"
            "D. Battery failure"
        ), #064
        "answer": (
            "A. Abnormal engine noise or vibration"
        ),
    },
    {
        "question": (
            "How is cylinder out-of-round detected?\n\n"
            "A. Measuring diameter at multiple points around the bore\n"
            "B. Visual inspection only\n"
            "C. Oil pressure test\n"
            "D. Compression test"
        ), #065
        "answer": (
            "A. Measuring diameter at multiple points around the bore"
        ),
    },
]
