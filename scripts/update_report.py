#!/usr/bin/env python3
"""
Stock Learning Report Updater
每天日报生成后调用此脚本：
1. 将日报内容保存为 md 文件到 2026/04/ 目录
2. 更新 README.md 索引
3. 发送 Telegram 消息
4. 自动 git push 到 GitHub
"""

import sys
import os
import json
import urllib.request
import urllib.parse
from datetime import datetime

REPO_PATH = "/home/rao/code/Stock-Learning-Skill"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
GITHUB_REPO = f"https://{GITHUB_TOKEN}@github.com/raopan2021/Stock-Learning-Skill.git"
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "8656350321:AAGEAo3NgPj8Xz2x9WZjEvyPHDrIV_VvNds")
TELEGRAM_CHAT_ID = "7885154100"

def get_current_year_month():
    now = datetime.now()
    return now.strftime("%Y"), now.strftime("%m"), now.strftime("%Y-%m-%d")

def save_report(date_str, title, content):
    year, month, _ = get_current_year_month()
    month_dir = os.path.join(REPO_PATH, year, month)
    os.makedirs(month_dir, exist_ok=True)
    
    filename = f"{date_str}.md"
    filepath = os.path.join(month_dir, filename)
    
    full_content = f"# A股学习日报 | {date_str}\n\n{content}\n\n---\n*本日报由 Stock Learning Skill 自动生成并推送*\n"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_content)
    
    return filepath, f"{year}/{month}/{filename}"

def update_index(date_str, title, filename):
    readme_path = os.path.join(REPO_PATH, "README.md")
    
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_entry = f"| {date_str} | {title} | [查看日报](./{filename}) |"
    
    # 找到空的占位行，替换为第一条数据
    placeholder = "| — | — | — |"
    if placeholder in content:
        content = content.replace(placeholder, new_entry)
    else:
        # 在表格最后一条数据后插入新行
        lines = content.split("\n")
        for i, line in enumerate(lines):
            if line.strip().startswith("|") and "|" in line and "日期" not in line and "---" not in line and "==" not in line:
                last_data_line = i
        lines.insert(last_data_line + 1, new_entry)
        content = "\n".join(lines)
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    })
    req = urllib.request.Request(url, data=data.encode("utf-8"))
    with urllib.request.urlopen(req, timeout=10) as response:
        result = json.loads(response.read().decode())
        if result.get("ok"):
            print("✅ Telegram 消息已发送")
        else:
            print(f"⚠️ Telegram 发送失败: {result}")

def git_push():
    os.chdir(REPO_PATH)
    os.system("git add .")
    os.system(f"git commit -m 'Update: daily report'")
    os.system(f"git remote set-url origin {GITHUB_REPO}")
    os.system("git push origin main --force")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 update_report.py <title> <content>")
        sys.exit(1)
    
    title = sys.argv[1]
    # 所有参数从第3个开始，合并为 content（因为内容可能包含换行）
    content = "\n".join(sys.argv[2:])
    
    year, month, date_str = get_current_year_month()
    
    # 1. 保存日报文件
    filepath, relative_path = save_report(date_str, title, content)
    print(f"✅ 日报已保存: {filepath}")
    
    # 2. 更新索引
    update_index(date_str, title, relative_path)
    print("✅ README.md 索引已更新")
    
    # 3. 发送 Telegram
    telegram_msg = f"📊 *A股学习日报* | {date_str}\n\n{content}\n\n⚠️ 以上内容仅供学习参考，不构成投资建议。"
    send_telegram(telegram_msg)
    
    # 4. Git push
    git_push()
    print("✅ 已推送到 GitHub")

if __name__ == "__main__":
    main()
