import openai
import os

openai.api_key = ""

def generate_questions_answers(training_data):
    for i, data in enumerate(training_data):
        input_text = f"\nTraining data {i + 1}:\n{data}\n"
        prompt = f"Generate new questions and answers based on the following text:\n{input_text}\n\nQuestions:\n1. \n2. \n3. \nAnswers:\n"

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            temperature=0.7,
            max_tokens=1024,
            n=1,
            stop=None,
            timeout=20,
        )

        print(response['choices'][0]['text'].strip())

training_data = ["""
Supply-side policies (SSPs) are government attempts to increase productivity and increase efficiency in the economy. If successful, they will shift AS to the right and enable higher economic growth in the long run.
SSPs fall into two categories: free-market and interventionist.
Free-market
These involve policies to increase competitiveness and free-market efficiency. For example:

Privatisation - sell state owned assets to the private sector. The private sector is more efficient in running businesses because they have a profit motive to reduce costs and develop better services.
Advantages:
-Improved efficiency
-Lack of political interference
-Shareholders pressure
-Increased competition
-Government will raise revenue from the sale
Disadvantages:
-Natural monopoly
-Public interest
-Government loses out on potential dividends
-Problem of regulating private monopolies
-Fragmentation of industries
-Short-termism of firms

Deregulation - reducing entry barriers to allow new firms to enter the market. This will make the market more competitive.
Advantages:
-Lower prices
-Better quality of goods & services
Disadvantages:
-Natural monopolies

Income tax cuts
Advantages:
-Increases labour supply and output.
-Increases investment.
Disadvantages:
-May not always increase work incentives
-Investment may not happen
-Strikes

Flexible labour markets - reduces power of trade unions, minimum wages and regulations.
Advantages:
-Higher profit for firms
-More efficient use of labour
-Increased employment
Disadvantages:
-Increased uncertainty
-Lower productivity

Free-trade agreements - reduces tariff barriers and other obstacles to trade.
Advantages:
-Increase exports
-Lower costs for businesses
Disadvantages:
-Can also increase imports

Reduce welfare benefits - increases incentives to get a job.
Advantages:
-Increased employment
-Increased output
Disadvantages:
-Hard to get right. Who actually needs it? Disabled? etc.


Interventionist
These involve government intervention to overcome market failure. For example:

Public sector investment in infrastructure - improve transport and reduce costs.
Advantages:
-Reduce market failures.
-Reduce costs of infrastructure.
-Encourage investment.
Disadvantages:
-Hard to increase transport capacity in crowded cities.
-Can also lead to market failures such as pollution.
-Large cost to government.

Education/Training - increase funding to schools and universities. This will improve labour productivity.
Advantages:
-Increase labour productivity.
Disadvantages:
-Large cost to government.
-Time lag.

Housing supply - increasing the supply of council housing
Advantages:
-Improves geographical mobility.
-Reduces labour shortages.
Disadvantages:
-Crowds out areas
-Large cost.
-Where to build

Health spending - public spending on health
Advantages:
-Improve labour productivity.
-Healthier population.
Disadvantages:
-Inefficient spending.
-Large cost to government.


Benefits of SSPs
SSPs should increase productivity and shift LRAS to the right.
-Lower Inflation Shifting AS to the right will cause a lower price level. By making the economy more efficient, SSPs will help reduce cost-push inflation.
-Lower Unemployment SSPs can contribute to reducing structural, frictional and real-wage unemployment and therefore help reduce the natural rate of unemployment.
-Improved economic growth SSPs will increase the sustainable rate of economic growth by increasing LRAS; this enables a higher rate of economic growth without causing inflation.
-Improved trade and Balance of Payments By making firms more productive and competitive, they will be able to export more. This is important in light of the increased competition from an increasingly globalised marketplace.

Questions and Answers
Q: What are the advantages of privatisation? 
A: Privatisation is the selling of state-owned assets to the private sector. Privatisation leads to improved efficiency in the running of businesses as they have a profit motive to reduce costs and develop better services due to competition. Since firms are sold from the public sector to the private sector, there will be a lack of political interference. Shareholder pressures and the competitive nature of the private sector will lead to improved efficiency and better quality of goods and services. Finally, the government will also raise revenue from selling state-owned assets which can be spent on interventionist SSPs
Q: How can the government improve labour productivity? 
A: The government can improve labour productivity by investing in education and vocational training. Investing in the quantity and quality of these services will train current and potential labour, leading to increased labour productivity. However, an issue with improving education and vocational training is the time lag. An average student will be in education for 10 years (from reception to GCSEs). This means by changing the syllabus, it can take up to 10 years for it to be effective.
Q: What is the difference between market-based and interventionist SSPs? 
A: Market-based SSPs involve policies to increase competitiveness and free-market efficiency. Examples include privatisation, deregulation, income tax cuts, flexible labour markets, free-trade agreements and reducing welfare benefits. Interventionist SSPs involve government intervention to overcome market failures. Examples include public sector investment, education/training, increasing the housing supply and increasing health spending.
Q: Why would a government not want to cut income tax to increase efficiency? 
A: Cutting income tax may decrease work incentives as workers may not see the benefit of working more and may go on strike, decreasing efficiency. Also, the extra profit firms will have may not go to investment, instead they may give it to shareholders or include it in manager salaries.
Q: What benefits do SSPs have on unemployment? 
A: SSPs can contribute to reducing structural, frictional and real-wage unemployment through policies such as public sector investment, education and increasing the housing supply. This will help reduce the natural rate of unemployment.
""", """
Example Input:
The Challenge of Natural Hazards 
Glossary of Definitions
Adaptation - Responding to climate change by coming up with ways to live and cope with the effects. Atmospheric circulation - The general movements of air around the Earth due to pressure and temperature. Atmospheric hazard - Hazards caused by the weather and processes in the atmosphere. Carbon Capture and Storage (CCS) - The process of capturing carbon dioxide that would normally be emitted into the atmosphere and storing it underground in reservoirs. Climate change - A distinct change in global or regional patterns of climate, such as changes in temperature or precipitation patterns. Conservative plate margin - A plate margin where two plates are moving alongside each other. Constructive plate margin - A plate margin where two plates are moving away from each other. Continental crust - The thicker, less dense crust that makes up the continents. Convection current - The movement of a fluid caused by a difference in temperature or density. Coriolis Effect - The effect of the Earth’s rotation on wind movements. Cyclone - A tropical storm that hits Oceania or Madagascar. Destructive plate margin - A plate margin where two plates are moving towards each other. Eccentricity - The changing of the orbit of the Earth around the Sun from a circular shape to an ellipse. Eye - An area of a tropical storm with extremely low pressure and calm conditions. Eyewall - An area of a tropical storm with the most intense, powerful winds and torrential rain. Ferrel Cell - At around 60° either side of the equator, moist air rises, and travels to lower latitudes at around 30° where it sinks, along with air travelling from the equator. Fossil fuels - Fuels made up of the remains of organic material, such as oil, coal and gas. Geological hazard - A hazard caused by processes on the land. Greenhouse Gases - Gases in the Earth’s atmosphere that trap energy in the Earth’s system and contribute to the greenhouse effect (carbon dioxide, methane, water vapour and nitrous oxides). Hadley Cell - At the equator, hot moist air rises, moves to higher latitudes (30°) and sinks. 

Q1: Define Adaptation.
A1: Responding to climate change by coming up with ways to live and cope with the effects. 

Q2: Define Atmospheric circulation.
A2: The general movements of air around the Earth due to pressure and temperature. 

Q3: Define Atmospheric hazard.
A3: Hazards caused by the weather and processes in the atmosphere.
"""
]

generate_questions_answers(training_data)

