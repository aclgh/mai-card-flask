import requests

url = "http://127.0.0.1:6969/gen"
user_data = {
    "nickname": "Ｈｏｓｈｉｎｏ☆",
    "title": "游戏中心岛今天也很平静呢",
    "icon": 350101,
    "frame": 350101,
    "plate": 350101,
    "rating": 12345,
    "classRank": 7,
    "courseRank": 10,
    "titleRare": "Normal",
    "chara": [101, 104, 355610, 355611, 355612],
    "charaLevel": [1000, 9999, 1000, 9999, 9999],
}
response = requests.post(url, json=user_data)
print(type([1000, 9999, 1000, 9999, 9999]))
print(f"Status Code: {response.status_code}")
if response.status_code == 200:
    with open("./gen_pic/output_image.png", "wb") as f:
        f.write(response.content)
else:
    print("Failed to retrieve image")
