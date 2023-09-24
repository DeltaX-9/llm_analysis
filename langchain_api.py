from flask import Flask
import openai
import langchain
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import json
from dotenv import load_dotenv

app = Flask(__name__)

@app.route('/api/analyse/<content>')
def analyse(content):
    print(content)
    messages = [content]
    prompt = PromptTemplate.from_template(
        "Whatever the darkest corner of diabolical human mind can conceive, Dark-Web can deliver with anonymity and impunity. Dark web markets and forums are filled with illicit activities such as counterfeit currency, fake documents, contraband drugs, ransomware attacks etc. In India, Dark-web crimes have proliferated in recent times especially in the arena of Cyber terrorism, drug trafficking, counterfeit documents, currency and sale of classified Government documents. Governments have also recently raised concern over digital currency and use of Dark-Web for drug trafficking. It is important that appropriate tools and techniques may be developed to monitor and track anti-national activities carried out behind the shield of anonymity by using dark web and cryptocurrency technology. I will give an input of messages. Analyse those messages based on the prompt and asign float values to them ranging from 0 to 1 with 0, 0.1, .. being for less dangerous messages containg words like peace, etc. while most dangerous being kill, murder, bombs, etc can be assigned 0.9, 1, etc depending on the level of threat {message}? (give me the output in json formate)")

    llm = OpenAI(temperature=0.3)
    Chain = LLMChain(llm=llm, prompt=prompt)
    output = Chain.run(messages)
    print(output)

    return json.loads(output)


app.run(debug=True)