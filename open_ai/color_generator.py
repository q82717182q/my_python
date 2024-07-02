# https://openai.com/  -> https://platform.openai.com/usage 使用額度 免費5元
#                      -> create api keys
# $ pip install openai
# https://github.com/openai/openai-python

import os
from dotenv import dotenv_values   # 拿來用.env引入環境變數的檔案  .env檔是預設隱藏檔案
from openai import OpenAI
import gradio as gr

config = dotenv_values('.env') # 這樣是跟.py同一層的檔案


client = OpenAI(
    api_key=config["api_key"],
)

content = """





"""
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": content
        }
    ],
    model="gpt-3.5-turbo",
)


def color(text):
    return chat_completion.choices[0].message.content

demo = gr.Interface(
    fn=color,  # 輸入與輸出經過這個函式做改變
    inputs=color(text),
    outputs="html",  #  其他格式可以上官網研究https://www.gradio.app/docs
    title="顏色產生器",
    description="輸入一段文字，產生2~6個顏色",
    allow_flagging="never" # 關掉flag那個button
)



# print(chat_completion)
# print(chat_completion.choices[0].message.content)