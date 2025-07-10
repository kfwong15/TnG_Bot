# bot.py
import datetime
import random

amount = round(random.uniform(1, 100), 2)
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

message = f"收到一笔 Touch n Go 收款：RM {amount}，时间 {now}"

with open("tng_notice.txt", "w", encoding="utf-8") as f:
    f.write(message)

print("✅ 已写入通知内容：", message)
