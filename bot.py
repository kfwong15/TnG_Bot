import datetime
import random
import os

# 🧾 生成收款信息
amount = round(random.uniform(1, 100), 2)
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
message = f"收到一笔 Touch n Go 收款：RM {amount}，时间 {now}"

# 💾 写入通知文件
with open("tng_notice.txt", "w", encoding="utf-8") as f:
    f.write(message)

print("✅ 收款信息已生成：", message)

# 🔊 播报语音（使用中文 + 媒体音量）
def speak(text):
    os.system(f'termux-tts-speak -s music -l zh-CN "{text}"')

speak(message)
