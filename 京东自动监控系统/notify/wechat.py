import requests

SCKEY = "你的key"

def send_wechat(title, content):
    url = f"https://sctapi.ftqq.com/{SCKEY}.send"

    data = {
        "title": title,
        "desp": content
    }

    requests.post(url, data=data)