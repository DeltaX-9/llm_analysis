import openai
openai_api_key=''
from langchain.llms import OpenAI
llm = OpenAI(openai_api_key=openai_api_key, temperature = 0)
text = f"""
A is going to kill B. A was thinking to do xxx. There was a threat yyy.
"""
prompt = f"""
In the given text, go through each line and identify the threat level of each line and give float values ranging from 0 to 1. 0, 0.1, etc being for the least malicious sentences while 0.9, 1 etc for most dangerous sentences. Only assign the values for each sentence and give that as output. Words like think, do, etc are least dangerous while words like kill, threat, murder, bomb are dangerous. Assign float values.
```{text}```
"""
text1 = llm(prompt)
print(text1)