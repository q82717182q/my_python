import requests

url = "https://www.ptt.cc/bbs/NBA/index.html"

response = requests.get(url)
# print(response.text)  # 物件需要加上.text轉成字串才能印

if response.status_code == 200:  # 用狀態碼來判斷是否有正確抓到網頁dd
    with open('output.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
    print("寫入成功！")
else:
    print("沒有抓到網頁")