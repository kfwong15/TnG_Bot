# bot.py
import datetime
import random
import os
import shutil

# 🧾 生成收款信息
amount = round(random.uniform(1, 100), 2)
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
message = f"收到一笔 Touch 'n Go 收款：RM {amount}，时间 {now}"

# 💾 写入通知文件
with open("tng_notice.txt", "w", encoding="utf-8") as f:
    f.write(message)

print("✅ 已写入通知内容：", message)

# 🔊 播报语音函数
def speak(text):
    if shutil.which("termux-tts-speak"):
        print("📢 使用 termux-tts-speak 播报")
        os.system(f'termux-tts-speak "{text}"')
    elif shutil.which("espeak"):
        print("📢 使用 espeak 播报")
        os.system(f'espeak -s 130 -p 70 "{text}"')
    else:
        print("⚠️ 未找到语音播报工具，请安装 termux-api 或 espeak")

# 🚀 执行播报
speak(message)
