import requests, emoji, os

# This is commented because it's not used for GitHub Actions
## from env import TOKEN, CHAT

# Uncomment this instead if you want to run this locally
TOKEN, CHAT = os.environ['TOKEN'], os.environ['CHAT']

# Yes, you may use these stickers
good_morning = "CAACAgUAAxkBAAM9YTc0SsvypOPzN4VA6r7uJCV9eukAAgEAA8dbrQPU7mkXJrJHPSAE"
good_afternoon = "CAACAgUAAxkBAAM_YTc1HaIdSH6qmXrsDUItfuZZkY8AAgYAA8dbrQOIV91AsC8P2SAE"
good_evening = "CAACAgUAAxkBAANAYTc1I4tAEdTNkAJFYywQGeHB-LcAAgkAA8dbrQOB-BZvTGEUIiAE"
good_night = "CAACAgUAAxkBAANBYTc1Jh-7GXBGzNuKIqpYcsLNVM8AAg0AA8dbrQMV6aNbkZG_AiAE"

def greet(sticker_id):
    resp = requests.get(f"https://api.telegram.org/bot{TOKEN}/sendSticker?chat_id={CHAT}&sticker={sticker_id}")
    return resp.json()

# https://www.webfx.com/tools/emoji-cheat-sheet/
def send(bot_message):
    resp = requests.get(emoji.emojize(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT}&parse_mode=Markdown&text={bot_message}&disable_web_page_preview=true", use_aliases = True))
    return resp.json()

if __name__ == "__main__":
    # To send messages manually, bot in disguise :)
    while True:
        exec(input())
