import httpx
import json
import os
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import time

import net
JACKET_API_URL = "https://assets2.lxns.net/maimai/jacket/{song_id}.png"
FONT_PATH = os.path.join("res", "FOT-NewRodin Pro B.otf")
MAX_TITLE_LENGTH = 200
MAX_RETRIES = 10


def load_music_list():
    try:
        with open(os.path.join(os.path.dirname(__file__), 'music_list.json'), 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("未找到 music_list.json 文件。")
        return {}
    except json.JSONDecodeError:
        print("解析 music_list.json 文件失败。")
        return {}


def get_music_name(music_data, music_id):
    return music_data.get('data', {}).get(str(music_id), {}).get('title', '未知乐曲')


def fetch_jacket_image(song_id):
    if len(str(song_id)) == 5:
        song_id -= 10000

    url = JACKET_API_URL.format(song_id=song_id)
    retries = 0
    while retries < MAX_RETRIES:
        with httpx.Client() as client:
            try:
                response = client.get(url)
                if response.status_code == 200:
                    return Image.open(BytesIO(response.content))
                else:
                    print(
                        f"曲绘请求失败: {url} (状态码: {response.status_code})，重试中... ({retries + 1}/{MAX_RETRIES})")
            except Exception as e:
                print(f"曲绘请求异常: {e}，重试中... ({retries + 1}/{MAX_RETRIES})")
            retries += 1
            time.sleep(1)
    print(f"曲绘请求失败: {url}，燃尽了 {MAX_RETRIES}。")
    return None


def fetch_jacket_image_local(song_id):
    cover_path = os.path.join(os.path.dirname(
        __file__), 'res', 'cover', f'{song_id}.png')
    if os.path.exists(cover_path):
        return Image.open(cover_path)
    else:
        print(f"未找到本地曲绘: {cover_path}")
        return None


def generate_ranking_image(data, music_data, output_path="music_output.png"):
    background_path = os.path.join("res", "background.jpg")
    try:
        parsed_data = json.loads(data)
        game_ranking_list = parsed_data.get('gameRankingList', [])
        sorted_ranking = sorted(
            game_ranking_list, key=lambda x: x['point'], reverse=True)

        try:
            background = Image.open(os.path.join(
                os.path.dirname(__file__), background_path))
        except FileNotFoundError:
            print(f"未找到 {background_path}")
            return

        draw = ImageDraw.Draw(background)

        try:
            font = ImageFont.truetype(FONT_PATH, 20)
        except IOError:
            print("字体加载失败")
            font = ImageFont.load_default()

        x = 60
        y = 43
        line_height = 70

        for player in sorted_ranking[:20]:
            music_name = get_music_name(music_data, player['id'])
            bbox = draw.textbbox((0, 0), music_name, font=font)
            text_length = bbox[2] - bbox[0]
            if text_length > MAX_TITLE_LENGTH:
                music_name = music_name[:int(len(music_name) *
                                             MAX_TITLE_LENGTH / text_length)]
                music_name = music_name[:-1]+'...'

            jacket_image = fetch_jacket_image_local(player['id'])
            if jacket_image:
                jacket_image = jacket_image.resize((45, 45))
                background.paste(jacket_image, (x, y + 13))

            draw.text((x + 55, y + 24), music_name, font=font, fill="white")
            y += line_height

        script_dir = os.path.dirname(__file__)
        output_path = os.path.join(script_dir, 'gen_pic', output_path)
        background.save(output_path)
        print(f"图片已保存为 {output_path}")
        return output_path

    except Exception as e:
        print(f"生成图片失败: {e}")
        return None


def main():
    api_name = "GetGameRankingApiMaimaiChn"
    data = '{"type":1}'

    status, response = net.send_request(api_name, data)

    if status == 200:
        music_data = load_music_list()
        start_time = time.time()
        output_path = generate_ranking_image(
            response, music_data, output_path="output.png")
        end_time = time.time()
        print(f"生成图片耗时: {end_time - start_time} 秒")


if __name__ == '__main__':
    main()
