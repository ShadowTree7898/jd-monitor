from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def detect_page_state(text):
    if "扫码登录" in text or "请登录" in text:
        return "login"
    if "验证" in text or "滑块" in text:
        return "captcha"
    if "访问过于频繁" in text or "网络不给力" in text:
        return "risk"
    return "ok"


def check_stock(driver, url):
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    text = driver.find_element(By.TAG_NAME, "body").text

    state = detect_page_state(text)

    if state == "login":
        return None, "需要登录"
    if state == "captcha":
        return None, "触发验证码"
    if state == "risk":
        return None, "触发风控"

    if "无货" in text or "到货通知" in text:
        return False, "无货"

    if "有货" in text or "仅剩" in text:
        return True, "有货"

    if "加入购物车" in text or "立即购买" in text:
        return True, "可下单"

    return None, "未知状态"
