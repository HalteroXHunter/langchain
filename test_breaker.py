import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

information="""
Elon Reeve Musk is a businessman and Senior Advisor to the U.S. President, best known for his key roles in Tesla, Inc., SpaceX, the Department of Government Efficiency (DOGE), and his ownership of Twitter. Musk is the wealthiest individual in the world; as of February 2025, Forbes estimates his net worth to be US$397 billion.

Musk was born to an affluent South African family in Pretoria before immigrating to Canada, acquiring its citizenship from his mother. He moved to California in 1995 to attend Stanford University, and with his brother Kimbal co-founded the software company Zip2, which was acquired by Compaq in 1999. That same year, Musk co-founded X.com, a direct bank, that later formed PayPal. In 2002, Musk acquired U.S. citizenship, and eBay acquired PayPal. Using the money he made from the sale, Musk founded SpaceX, a spaceflight services company, in 2002. In 2004, Musk was an early investor in electric vehicle manufacturer Tesla and became its chairman and later CEO. In 2018, the U.S. Securities and Exchange Commission (SEC) sued Musk for fraud, alleging he falsely announced that he had secured funding for a private takeover of Tesla; he stepped down as chairman and paid a fine. Musk was named Time magazine's Person of the Year in 2021. In 2022, he acquired Twitter, and rebranded the service as X the following year. In January 2025, he was appointed head of Trump's newly created DOGE.

His political activities and views have made him a polarizing figure. He has been criticized for making unscientific and misleading statements, including COVID-19 misinformation, affirming antisemitic and transphobic comments, and promoting conspiracy theories. His acquisition of Twitter was controversial due to a subsequent increase in hate speech and the spread of misinformation on the service. Musk has engaged in political activities in several countries, including as a vocal and financial supporter of U.S. president Donald Trump. He was the largest donor in the 2024 United States presidential election, and is a supporter of far-right activists, causes, and political parties.
"""

if __name__ == "__main__":

    summary_template = """
    given the information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
"""
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    # llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    llm =  ChatOllama(model="llama3")

    chain = summary_prompt_template | llm | StrOutputParser()
    res =chain.invoke(input={"information":information})

    print(res)