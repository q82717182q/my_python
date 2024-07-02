import gradio as gr  # 快速做展示的工具


# def color(text):
#     return text + "hello world"
#
# demo = gr.Interface(
#     fn=color,  # 輸入與輸出經過這個函式做改變
#     inputs="text",
#     outputs="text"
# )


def color(text):
    return "<div style='background-color:#FF5151; color:#FFFFFF; padding:10px;'>{text}</div>"

demo = gr.Interface(
    fn=color,  # 輸入與輸出經過這個函式做改變
    inputs="text",
    outputs="html",  #  其他格式可以上官網研究https://www.gradio.app/docs
    title="顏色產生器",
    description="輸入一段文字，產生2~6個顏色",
    allow_flagging="never" # 關掉flag那個button
)




demo.launch()  # 執行完會給url
