import openai
import os

openai.api_key = "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"

def generate_questions_answers(input_text):
    prompt = f"Generate questions and answers based on the following text:\n{input_text}\n\nQuestions:\n1. \n2. \n3. \nAnswers:\n"
    
    
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

prompt = """
Supply-side policies (SSPs) are government attempts to increase productivity and increase efficiency in the economy. If successful, they will shift AS to the right and enable higher economic growth in the long run.
SSPs fall into two categories: free-market and interventionist.
Free-market
These involve policies to increase competitiveness and free-market efficiency. For example:
Privatisation - sell state owned assets to the private sector. The private sector is more efficient in running businesses because they have a profit motive to reduce costs and develop better services.
Advantages:
Improved efficiency
Lack of political interference
Shareholders pressure
Increased competition
Government will raise revenue from the sale
Disadvantages:
Natural monopoly
Public interest
Government loses out on potential dividends
Problem of regulating private monopolies
Fragmentation of industries
Short-termism of firms
Deregulation - reducing entry barriers to allow new firms to enter the market. This will make the market more competitive.
Advantages:
Lower prices
Better quality of goods & services
Disadvantages:
Natural monopolies
Income tax cuts
Advantages:
Increases labour supply and output.
Increases investment.
Disadvantages:
May not always increase work incentives
Investment may not happen
Strikes

Q: What are the advantages of privatisation? 
A: Privatisation is the selling of state-owned assets to the private sector. Privatisation leads to improved efficiency in the running of businesses as they have a profit motive to reduce costs and develop better services due to competition. Since firms are sold from the public sector to the private sector, there will be a lack of political interference. Shareholder pressures and the competitive nature of the private sector will lead to improved efficiency and better quality of goods and services. Finally, the government will also raise revenue from selling state-owned assets which can be spent on interventionist SSPs
Q: How can the government improve labour productivity? 
A: The government can improve labour productivity by investing in education and vocational training. Investing in the quantity and quality of these services will train current and potential labour, leading to increased labour productivity. However, an issue with improving education and vocational training is the time lag. An average student will be in education for 10 years (from reception to GCSEs). This means by changing the syllabus, it can take up to 10 years for it to be effective.
Q: What is the difference between market-based and interventionist SSPs? 
A: Market-based SSPs involve policies to increase competitiveness and free-market efficiency. Examples include privatisation, deregulation, income tax cuts, flexible labour markets, free-trade agreements and reducing welfare benefits. Interventionist SSPs involve government intervention to overcome market failures. Examples include public sector investment, education/training, increasing the housing supply and increasing health spending.
"""

generate_questions_answers(prompt)
