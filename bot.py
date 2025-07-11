# bot.py
import datetime
import random
import os
import time
import shutil

def speak(text):
    if shutil.which("termux-tts-speak"):
        os.system(f'termux-tts-speak "{text}"')
    elif shutil.which("espeak"):
        os.system(f'espeak -s 130 -p 70 "{text}"')
    else:
        print("⚠️ 无语音播报工具")

def load_last_time():
    try:
        with open("last_transaction.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""

def save_last_time(timestamp):
    with open("last_transaction.txt", "w") as f:
        f.write(timestamp)

print("🚀 实时收款播报助手启动中...")

while True:
    # 🧾 模拟收款信息（未来可接入真实 API）
    amount = round(random.uniform(1, 100), 2)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"收到一笔 Touch 'n Go 收款：RM {amount}，时间 {now}"

    # 🔍 检查是否是新交易
    last_time = load_last_time()
    if now != last_time:
        with open("tng_notice.txt", "w", encoding="utf-8") as f:
            f.write(message)
        print("✅ 新交易播报：", message)
        speak(message)
        save_last_time(now)

    time.sleep(3)  # 每 3 秒检查一次
