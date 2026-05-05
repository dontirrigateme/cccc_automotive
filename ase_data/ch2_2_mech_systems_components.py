#02.02 Automatic Transmission/Transaxle - Mechanical Systems & Components

QUESTIONS = [
    {
        "question": "What is another term for a planetary gear set?", #001
        "answer": "Epicyclic gear set",
    },
    {
        "question": (
            "What are the three main components of a planetary gear set?"
        ), #002
        "answer": (
            "Sun gear\n"
            "Planet gears and carriers\n"
            "Ring gear (annulus)"
        ),
    },
    {
        "question": "What is a sun gear?", #003
        "answer": "The central gear around which the planet gears rotate",
    },
    {
        "question": "What are planet gears and carriers?", #004
        "answer": "Several smaller gears (planet gears) mounted on a carrier that orbits around the sun gear. The carrier holds the planet gears and allows them to rotate.",
    },
    {
        "question": "What is a ring gear (annulus)?", #005
        "answer": "A large outer gear that meshes with the planet gears from the outside",
    },
    {
        "question": (
            "What are the planetary gear ratios/settings?"
        ), #006
        "answer": (
            "Direct drive (1:1 ratio)\n"
            "Reduction gear (low gear)\n"
            "Overdrive (high gear)\n"
            "Reverse"
        ),
    },
    {
        "question": "With regard to planetary gears, what is direct drive (1:1 ratio)?", #007
        "answer": "When the sun gear, planet carrier, and ring gear all rotate together, the output speed equals the input speed",
    },
    {
        "question": "With regard to planetary gears, what is reduction gear (low gear)?", #008
        "answer": "Holding the ring gear stationary allows the planet carrier to turn slower than the sun gear input, resulting in torque multiplication and lower output speed",
    },
    {
        "question": "With regard to planetary gears, what is overdrive (high gear)?", #009
        "answer": "Holding the sun gear stationary allows the planet carrier to turn faster than the ring gear input, providing higher output speed",
    },
    {
        "question": "With regard to planetary gears, what is reverse?", #010
        "answer": "The ring gear is held stationary, and the sun gear is driven in reverse, causing the planet carrier (output) to turn backwards",
    },
    {
        "question": (
            "What are the types of gear train arrangements?"
        ), #011
        "answer": (
            "Single planetary gear set\n"
            "Compound planetary gear sets\n"
            "Ravigneaux gear set\n"
            "Simpson gear set\n"
            "Compound gear train with multiple sets"
        ),
    },
    {
        "question": "What is the function of the input shaft?", #012
        "answer": "Transfers engine power into the transmission",
    },
    {
        "question": "What is the function of the output shaft?", #013
        "answer": "Delivers power from the transmission to the driveshaft or transaxle",
    },
    {
        "question": "What is the role of the input shaft in the gear set?", #014
        "answer": "Drives sun gear, carrier, or ring",
    },
    {
        "question": "What is the role of the output shaft in the gear set?", #015
        "answer": "Driven by carrier or ring gear",
    },
    {
        "question": "What is the role of the sun gear in the gear set?", #016
        "answer": "Drives or held to set ratio/direction",
    },
    {
        "question": "What is the role of the ring gear in the gear set?", #017
        "answer": "Held or driven to control output",
    },
    {
        "question": "What is the role of the planet carrier in the gear set?", #018
        "answer": "Transfers power to output shaft or held",
    },
    {
        "question": (
            "What are the two main types of clutches in an automatic transmission?"
        ), #019
        "answer": (
            "Friction clutch (multi-plate clutch)\n"
            "Sprag clutch"
        ),
    },
    {
        "question": "__________ engage to connect rotating components, while __________ hold specific parts stationary.", #020
        "answer": "Clutches, bands",
    },
    {
        "question": (
            "Which components are responsible for applying and releasing the bands and clutches that control gear changes?"
        ), #021
        "answer": (
            "Servos\n"
            "Actuators"
        ),
    },
    {
        "question": "What are hydraulic servos?", #022
        "answer": "They use pressurized transmission fluid to move a piston inside a cylinder",
    },
    {
        "question": "What are mechanical actuators in an automatic transmission?", #023
        "answer": "Found in older or simpler designs, they use direct mechanical linkage, such as rods or cables, to engage bands or clutches",
    },
    {
        "question": "What are hydraulic actuators?", #024
        "answer": "They are controlled by valves within the valve body, often coordinated by electronic controls, responding to pressure signals based on vehicle speed, throttle position, and other sensor inputs",
    },
    {
        "question": (
            "What are some symptoms of band problems in an automatic transmission?"
        ), #025
        "answer": (
            "Slipping in certain gears\n"
            "Burnt transmission fluid smell\n"
            "Harsh or erratic shifts\n"
            "Delayed or no engagement"
        ),
    },
    {
        "question": (
            "What are some causes of band problems in an automatic transmission?"
        ), #026
        "answer": (
            "Wear and stretching\n"
            "Improper adjustment\n"
            "Contamination\n"
            "Hydraulic problems"
        ),
    },
    {
        "question": (
            "What are some symptoms of servo problems in an automatic transmission?"
        ), #027
        "answer": (
            "Incomplete band application\n"
            "Delayed or harsh shifts\n"
            "Noise during shifts"
        ),
    },
    {
        "question": ( #01
            "What is the primary function of a planetary gear set in an automatic transmission?\n\n"
            "A. Transfer engine coolant\n"
            "B. Provide multiple gear ratios\n"
            "C. Lubricate the clutch packs\n"
            "D. Control hydraulic pressure"
        ), #028
        "answer": (
            "B. Provide multiple gear ratios"
        ),
    },
    {
        "question": ( #02
            "Which component holds the planetary gears and allows them to rotate?\n\n"
            "A. Carrier\n"
            "B. Sun gear\n"
            "C. Ring gear\n"
            "D. Output shaft"
        ), #029
        "answer": (
            "A. Carrier"
        ),
    },
    {
        "question": ( #03
            "What is the main role of the sun gear in a planetary gear set?\n\n"
            "A. Apply band tension\n"
            "B. Transmit power to the ring gear\n"
            "C. Drive the planetary gears\n"
            "D. Act as the output shaft"
        ), #030
        "answer": (
            "C. Drive the planetary gears"
        ),
    },
    {
        "question": ( #04
            "What gear train arrangement produces reverse gear in an automatic transmission?\n\n"
            "A. Direct drive\n"
            "B. Reversing the sun gear direction\n"
            "C. Holding the ring gear stationary\n"
            "D. Locking the carrier in place"
        ), #031
        "answer": (
            "C. Holding the ring gear stationary"
        ),
    },
    {
        "question": ( #05
            "What component transfers engine power into the transmission?\n\n"
            "A. Input shaft\n"
            "B. Output shaft\n"
            "C. Planet carrier\n"
            "D. Clutch pack"
        ), #032
        "answer": (
            "A. Input shaft"
        ),
    },
    {
        "question": ( #06
            "Clutch packs in automatic transmissions are primarily used to:\n\n"
            "A. Hold gears stationary\n"
            "B. Connect and disconnect gears\n"
            "C. Regulate fluid pressure\n"
            "D. Transfer hydraulic fluid"
        ), #033
        "answer": (
            "B. Connect and disconnect gears"
        ),
    },
    {
        "question": ( #07
            "What is a common sign that a clutch pack is worn?\n\n"
            "A. Hard shifting\n"
            "B. Transmission slipping\n"
            "C. No fluid leaks\n"
            "D. Constant fluid pressure"
        ), #034
        "answer": (
            "B. Transmission slipping"
        ),
    },
    {
        "question": ( #08
            "Bands in automatic transmissions are adjusted to:\n\n"
            "A. Increase engine RPM\n"
            "B. Prevent gear slippage\n"
            "C. Lubricate planetary gears\n"
            "D. Control fluid temperature"
        ), #035
        "answer": (
            "B. Prevent gear slippage"
        ),
    },
    {
        "question": ( #09
            "What hydraulic component applies the band to hold the gear stationary?\n\n"
            "A. Servo\n"
            "B. Regulator valve\n"
            "C. Manual valve\n"
            "D. Shift valve"
        ), #036
        "answer": (
            "A. Servo"
        ),
    },
    {
        "question": ( #10
            "A worn band typically causes which of the following?\n\n"
            "A. Hard gear engagement\n"
            "B. Gear slipping\n"
            "C. Excessive fluid pressure\n"
            "D. Faster shift times"
        ), #037
        "answer": (
            "B. Gear slipping"
        ),
    },
    {
        "question": ( #11
            "Which of these is NOT a typical cause of servo failure?\n\n"
            "A. Worn seals\n"
            "B. Hydraulic leaks\n"
            "C. Electrical short\n"
            "D. Damaged piston"
        ), #038
        "answer": (
            "C. Electrical short"
        ),
    },
    {
        "question": ( #12
            "How is servo piston movement usually powered?\n\n"
            "A. Mechanical linkage\n"
            "B. Hydraulic pressure\n"
            "C. Electrical motor\n"
            "D. Manual lever"
        ), #039
        "answer": (
            "B. Hydraulic pressure"
        ),
    },
    {
        "question": ( #13
            "When checking band adjustment, what indicates a need for adjustment?\n\n"
            "A. Excessive free play\n"
            "B. Excessive tightness\n"
            "C. No movement\n"
            "D. Fluid leakage"
        ), #040
        "answer": (
            "A. Excessive free play"
        ),
    },
    {
        "question": ( #14
            "The output shaft in an automatic transmission:\n\n"
            "A. Connects to the torque converter\n"
            "B. Drives the wheels\n"
            "C. Controls the hydraulic pressure\n"
            "D. Applies the band"
        ), #041
        "answer": (
            "B. Drives the wheels"
        ),
    },
    {
        "question": ( #15
            "How do planetary gear sets achieve multiple gear ratios?\n\n"
            "A. Varying hydraulic pressure\n"
            "B. Locking and releasing different components\n"
            "C. Changing fluid viscosity\n"
            "D. Altering torque converter speed"
        ), #042
        "answer": (
            "B. Locking and releasing different components"
        ),
    },
    {
        "question": ( #16
            "What should you inspect first when diagnosing slipping bands?\n\n"
            "A. Hydraulic pressure\n"
            "B. Band wear and adjustment\n"
            "C. Transmission fluid color\n"
            "D. Shift solenoid function"
        ), #043
        "answer": (
            "B. Band wear and adjustment"
        ),
    },
    {
        "question": ( #17
            "The ring gear in a planetary set:\n\n"
            "A. Is located at the center\n"
            "B. Encircles the planetary gears\n"
            "C. Drives the input shaft\n"
            "D. Moves independently"
        ), #044
        "answer": (
            "B. Encircles the planetary gears"
        ),
    },
    {
        "question": ( #18
            "Which type of clutch pack friction material is commonly used?\n\n"
            "A. Steel\n"
            "B. Fiberglass composite\n"
            "C. Rubber\n"
            "D. Cork"
        ), #045
        "answer": (
            "B. Fiberglass composite"
        ),
    },
    {
        "question": ( #19
            "Servos are typically located:\n\n"
            "A. Inside the torque converter\n"
            "B. On the transmission case exterior\n"
            "C. Within the valve body\n"
            "D. Attached to the driveshaft"
        ), #046
        "answer": (
            "B. On the transmission case exterior"
        ),
    },
    {
        "question": ( #20
            "What can cause servo piston sticking?\n\n"
            "A. Clean hydraulic fluid\n"
            "B. Damaged seals or debris\n"
            "C. Proper band adjustment\n"
            "D. High fluid pressure"
        ), #047
        "answer": (
            "B. Damaged seals or debris"
        ),
    },
]
