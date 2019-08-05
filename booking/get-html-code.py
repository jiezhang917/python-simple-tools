import requests

with open("code.txt", "w", encoding="utf-8") as f:
    headers = {
        "Host": "www.booking.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    response = requests.get("http://www.booking.com")
    f.write(response.text)
