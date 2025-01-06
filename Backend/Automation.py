from AppOpener import close,open as appopen
from webbrowser import open as webopen
from pywhatkit import search, playonyt
from dotenv import dotenv_values
from bs4 import BeautifulSoup
from rich import print
from groq import Groq
import webbrowser
import subprocess
import requests
import keyboard
import asyncio
import os


env_vars = dotenv_values(".env")
GroqAPIKey = env_vars.get("GroqAPIKey")


classes = [
    "zCubwf",
    "hgKElc",
    "LTKOO sY7ric",
    "ZOLcW",
    "gsrt vk_bk FzvWSb YwPhnf",
    "pclqee",
    "tw-Data-text tw-text-small tw-ta",
    "IZ6rdc",
    "05uR6d LTKOO",
    "vlzY6d",
    "webanswers-webanswers_table_webanswers-table",
    "dDoNo ikb4Bb gsrt",
    "sXLa0e",
    "LWkfKe",
    "VQF4g",
    "qv3Wpe",
    "kno-rdesc",
    "SPZz6b",
]


useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"


client = Groq(api_key=GroqAPIKey)


professional_responses = [
    "Your satisfaction is my top priority; feel free to reach out if there's anything else I can help you with.",
    "I'm at your service for any additional questions or support you may need-don't hesitate to ask.",
]

messages = []

SystemChatBot = {"role": "system", "content": f"Hello, I am {os.environ['Username']}, You're a content writer. You have to write content like letter"}

def GoogleSearch(Topic):
    search(Topic)
    return True

def Content(Topic):
    
    def OpenNotepad(File):
        default_text_editor = 'notepad.exe'
        subprocess.Popen([default_text_editor, File])

    def ContentWriterAI(prompt):
        messages.append({"role": "user", "content": f"{prompt}"})

        completion = client.chat.completions.create(
            model = "mixtral-8x-7b-32768",
            messages=SystemChatBot + messages, 
            max_tokens=2048,
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
        return Answer
    
    Topic: str=Topic.replace("Content", "")
    ContentByAI = ContentWritterAI(Topic)

    with open(rf"Data\{Topic.lower().replace(' ','')}.txt", "w", encoding="utf-8") as file:
        file.write(ContentByAI)
        file.close()

    OpenNotpade(rf"Data\{Topic.lower().replace(' ','')}.txt")
    return True

def