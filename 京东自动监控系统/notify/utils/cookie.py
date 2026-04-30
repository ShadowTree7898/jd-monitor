import json
import os


def load_cookie_string():

    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, "credentials.json")

    with open(file_path, "r", encoding="utf-8") as f:
        cookies = json.load(f)

    # ⭐ 关键：转换成 requests 能用的字符串
    cookie_str = "; ".join([f"{c['name']}={c['value']}" for c in cookies])

    return cookie_str