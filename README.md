JD Monitor（京东商品监控脚本）
📌 项目介绍

本项目是一个基于 Python 开发的京东商品监控工具，用于实时检测商品库存和价格变化。

适用于：

抢购商品（有货提醒）
价格监控
自动化脚本练习
⚙️ 功能
✅ 商品库存监控
⏳ 价格监控
⏳ 邮件 / 微信通知


jd_monitor/
│
├── main.py
│
├── monitor/
│   ├── stock_selenium.py
│
├── utils/
│   ├── cookie.py          ← 读取 cookie（工具）
│
├── scripts/
│   ├── get_cookie.py      ←  登录获取 cookie（只运行一次）
│
├── data/
│   ├── credentials.json   ←  cookie存放位置（数据）
│
├── notify/
├── driver_factory.py
