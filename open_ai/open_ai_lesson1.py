# https://www.youtube.com/watch?v=8GsLbNdbV6c

# https://openai.com/  -> https://platform.openai.com/usage 使用額度 免費5元
#                      -> create api keys
# $ pip install openai
# https://github.com/openai/openai-python

import os
from dotenv import dotenv_values   # 拿來用.env引入環境變數的檔案  .env檔是預設隱藏檔案
from openai import OpenAI
import json
import gradio as gr

# config = dotenv_values(".env")
# print(config)
# api_key=dotenv_values(".env.api_key")
# print(api_key)
config = dotenv_values('.env') # 這樣是跟.py同一層的檔案
# print(config)
# print(config["api_key"])


client = OpenAI(
    # This is the default and can be omitted
    api_key=config["api_key"],
)


def generate_colors(text):
    # 三個雙引號用於產生多行文字
    content = f"""  
        根據以下文字產生2~6個顏色
        
        輸出格式：輸出格式 python列表  16進制顏色編碼
        
        ###
        google
        ###
        ["#FF0000", "#4285F4", "#34A853", "#FBBC05", "#EA4335", "#7B0099"]
        
        ###
        {text}
        ###
    """

    chat_completion = client.chat.completions.create(
        # completions字樣就看你要做什麼應用
        # 不同的模型會有不同的token轉換模式，輸入輸出都會轉換成模型可以理解的形式（token）   https://platform.openai.com/tokenizer
        # 回答會根據token數量去收費  max_tokens沒事別開太高  相關設定請看官方文件
        # https://platform.openai.com/playground/chat?models=gpt-4o 這邊可以測試不同模型
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        model="gpt-3.5-turbo",  # 官網有提供很多模型 不同模型 價格不同 可以處理的事情也不同
        max_tokens=200,  # 最大回應字數
        # stop=["蚵", "魯", "滷"] # 遇到這個字就停止   也可以用成list
        # stop="蚵" # 遇到這個字就停止  也可以用成list
        # n=2,  # 會回應兩次
    )

    res = chat_completion.choices[0].message.content
    print("res : ")
    print(res)
    colors = json.loads(res)

    html = ""
    for i in colors:
        html += f"<div style='background-color:{i}; padding:10px;'>{i}</div>"
    print("html : ")
    print(html)
    return html

# print(type(generate_colors("facebook")))
# print(generate_colors("facebook"))
# colors = json.loads(generate_colors("facebook"))
# print(colors)
# print(type(colors))  # finish_reason -> (length:因為長度限制停止, stop:因為回應完停止)


def color(text):
    return "<div style='background-color:#FF5151; color:#FFFFFF; padding:10px;'>{text}</div>"

demo = gr.Interface(
    fn=generate_colors,  # 輸入與輸出經過這個函式做改變
    inputs="text",
    outputs="html",  #  其他格式可以上官網研究https://www.gradio.app/docs
    title="顏色產生器",
    description="輸入一段文字，產生2~6個顏色",
    allow_flagging="never" # 關掉flag那個button
)

# print(generate_colors("google"))



demo.launch()

# 1. 主要指令（你要模型幫你做什麼）    指令與資料之間可以用 ### 或 """ 區隔
# 2. 附上資料（如果需要的話）
# 3. 輸出格式（你希望模型怎麼輸出）
# 4. 明確的描述以上3點

# 可以拿來做總結，提取資料

# 範例
# 列出以下句子出現的所有人名
# 輸出格式：csv
# """
# 1986年，她參與世界貿易組織等國際談判，獲得政府賞識［11］。在李登輝政府時期，她是國安會諮詢委員，為「特殊的國與國關係」理論的主要起草人。2000年陳水扁政府上臺後，她以無黨籍學者身分擔任陸委會主委。2004年，她加入民進黨擔任不分區立法委員。2006年，她擔任蘇貞昌內閣的行政院副院長，直到隔年總辭［12］。
# """












# print(chat_completion)
#
# ChatCompletion(
#     id = 'chatcmpl-9fwNtpew2Fr5sdaNVxkEUsTz29G5K',
#     choices = [Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='你好！有什么可以帮助你的吗？', role='assistant', function_call=None, tool_calls=None))],
#     created = 1719782905,
#     model = 'gpt-3.5-turbo-0125',
#     object = 'chat.completion',
#     service_tier = None,
#     system_fingerprint = None,
#     usage = CompletionUsage(
#         completion_tokens = 17,
#         prompt_tokens = 9,
#         total_tokens = 26
#     )
# )

