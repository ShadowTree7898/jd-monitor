from selenium import webdriver

PROFILE_DIR = r"D:\PYTHON\chrome-jd-profile"


def create_driver():
    options = webdriver.ChromeOptions()

    # 固定浏览器用户目录，保留登录态
    options.add_argument(fr"--user-data-dir={PROFILE_DIR}")
    options.add_argument("--profile-directory=Default")

    # 先不要无头，方便你第一次登录和观察页面
    # options.add_argument("--headless=new")

    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    return driver
