from groq import Groq
from json import load, dump
import datetime
from dotenv import dotenv_values

env_vars = dotenv_values(".env")

Username = env_vars.get("Username")
Assistantname= env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")

client = Groq(api_key=GroqAPIKey)

messages = []

System = f"""
Hello, I am {Username}. You are {Assistantname}, my highly intelligent, accurate, and friendly AI Assistant.  

Your behavior is defined as follows:
- Provide accurate and concise answers to all queries.  
- Always reply in English, regardless of the language of the question.  
- Do not include notes, disclaimers, or mention training data in responses.  
- Never tell the current time or date unless explicitly asked.  
- Maintain a balance between professionalism and a friendly conversational tone.  
- Focus on the user’s intent and offer practical solutions or insights as needed.  

Remember, simplicity and accuracy are key in all interactions. 
"""


SystemChatBot = [
    {"role": "system", "content": System}
]

try:
    with open(r"Data\ChatLog.json", "r") as f:
        messages = load(f)
except:
    with open(r"Data\ChatLog.json", "w") as f:
        dump([],f)

def RealtimeInformation():
    current_date_time = datetime.datetime.now()
    day  = current_date_time.strftime("%A")
    date = current_date_time.strftime("%d")
    month = current_date_time.strftime("%B")
    year = current_date_time.strftime("%Y")
    hour = current_date_time.strftime("%H")
    minute = current_date_time.strftime("%M")
    second = current_date_time.strftime("%S")

    data = f"Please use this realtime information if needed,\n"
    data += f"Day: {day}\nDate: {date}\nMonth: {month}\nYear: {year}\n"
    data += f"Time: {hour} hours :{minute} minutes :{second} seconds.\n"
    return data

def AnswerModifier(Answer):
    lines = Answer.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    modified_answer= '\n'.join(non_empty_lines)
    return modified_answer

def ChatBot(Query):
    try:
        with open(r"Data\ChatLog.json","r") as f:
            messages = load(f)
        
        messages.append({"role": "user", "content": f"{Query}"})

        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=SystemChatBot + [{"role": "system", "content": RealtimeInformation()}] + messages,
            max_tokens=1024,
            temperature=0.7,
            top_p=1,
            stream=True,
            stop=None
        )

        Answer = ""

        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content

        Answer = Answer.replace("</s>", "")

        messages.append({"role": "assistant", "content": Answer})

        with open(r"Data\ChatLog.json", "w") as f:
            dump(messages, f, indent=4)

        return AnswerModifier(Answer=Answer)
    
    except Exception as e:
        print(f"Error: {e}")
        with open(r"Data\ChatLog.json", "w") as f:
            dump([],f,indent=4)
        return ChatBot(Query)

if __name__=="__main__":
    while True:
        user_input = input("IamKavy47: ")
        print(f"Kaash: {ChatBot(user_input)}")