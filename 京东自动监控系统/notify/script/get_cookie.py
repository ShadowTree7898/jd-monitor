from selenium import webdriver
import time
import os
import json


def save_cookies():

    driver = webdriver.Chrome()
    driver.get("https://www.jd.com/")

    print("👉 请手动登录京东（扫码/账号密码）")
    time.sleep(120)  # 给你时间登录

    cookies = driver.get_cookies()

    driver.quit()

    # ⭐ 获取“项目根目录”
    base_dir = os.path.dirname(os.path.dirname(__file__))

    # ⭐ 拼接文件路径（根目录）
    file_path = os.path.join(base_dir, "credentials.json")

    # 保存到credentials
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(cookies, f)

    print("✅ cookie 已保存")


if __name__ == "__main__":
    save_cookies()