import time
from monitor.stock_selenium import check_stock
from driver_factory import create_driver
from notify.wechat import send_wechat

URLS = [
    "https://item.jd.com/100012043978.html",
]

CHECK_INTERVAL = 10


def main():
    driver = create_driver()
    last_status = {}

    try:
        while True:
            print("\n===== 检测中 =====")

            for url in URLS:
                try:
                    stock, msg = check_stock(driver, url)
                    print(url, msg)

                    prev = last_status.get(url)

                    # 只有从“非有货”变成“有货”时才通知一次
                    if stock is True and prev is not True:
                        send_wechat("京东有货", url)

                    last_status[url] = stock

                    if msg == "需要登录":
                        print("请在浏览器中手动登录京东")
                        time.sleep(60)

                    elif msg in ["触发验证码", "触发风控"]:
                        print("页面被风控，稍后重试")
                        time.sleep(30)

                except Exception as e:
                    print("单商品异常:", e)
                    time.sleep(10)

            time.sleep(CHECK_INTERVAL)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
