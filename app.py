import time
import json
import pytz
import os
import io
from datetime import datetime
from flask import Flask, request, redirect, jsonify, send_file
from flask_cors import CORS
from card_img import call_user_img
from musicranking_img import call_ranking_img

app = Flask(__name__)
app.json.sort_keys = False
app.json.ensure_ascii = False
app.json.mimetype = 'application/json;charset=UTF-8'
app.json.compact = False
CORS(app)


def check_json(user_data):
    required_keys = {
        "nickname", "title", "icon", "frame", "plate",
        "rating", "classRank", "courseRank", "titleRare",
        "chara", "charaLevel"
    }

    # 检查user_data是否包含所有需要的键
    if set(user_data.keys()) == required_keys:
        # 如果包含了所有必需的键，可以进一步验证每个字段的类型或值
        # 例如，验证某些字段是否为字符串或数字等
        if isinstance(user_data["nickname"], str) and \
           isinstance(user_data["title"], str) and \
           isinstance(user_data["icon"], int) and \
           isinstance(user_data["frame"], int) and \
           isinstance(user_data["plate"], int) and \
           isinstance(user_data["rating"], (int)) and \
           isinstance(user_data["classRank"], int) and \
           isinstance(user_data["courseRank"], int) and \
           isinstance(user_data["titleRare"], str) and \
           isinstance(user_data["chara"], list) and \
           isinstance(user_data["charaLevel"], list):
            return True
        else:
            return False
    else:
        return False


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": "404 Not Found", "timestamp": int(time.time()), "info": "The route you are trying to access is missing.", "date": datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%a, %d %b %Y %H:%M:%S GMT+8')}), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"status": "405 Method Not Allowed", "timestamp": int(time.time()), "info": "You are using the wrong method. Check the docs.", "date": datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%a, %d %b %Y %H:%M:%S GMT+8')}), 405


@app.errorhandler(400)
def bad_request(e):
    return jsonify({"status": "400 Bad Request", "timestamp": int(time.time()), "info": "Something went Wrong.", "date": datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%a, %d %b %Y %H:%M:%S GMT+8')}), 400


@app.route("/")
def index():
    return jsonify({"status": "200 OK", "timestamp": int(time.time()), "info": "Mai Card Flask", "availableApi": ["card", "ranking"], "date": datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%a, %d %b %Y %H:%M:%S GMT+8')}), 200


@app.route("/card", methods=['POST'])
def gen_card():
    request_data = request.get_json()
    if check_json(request_data):
        img = call_user_img(request_data, False)
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)  # 重置字节流位置
        timestamp = int(time.time())
        img.save(os.path.join('cache', f'{timestamp}.png'))
        return send_file(img_byte_arr, mimetype='image/png')
    else:
        return jsonify({"status": "400 Bad Request", "timestamp": int(time.time()), "info": "Invalid JSON Format", "date": datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%a, %d %b %Y %H:%M:%S GMT+8')}), 400


@app.route("/ranking")
def ranking():
    img = call_ranking_img()
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    timestamp = int(time.time())
    img.save(os.path.join('cache', f'{timestamp}.png'))
    return send_file(img_byte_arr, mimetype='image/png')


if __name__ == '__main__':
    app.run(port=6970)
