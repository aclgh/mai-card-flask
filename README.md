# maicard-py

基于Python的玩家收藏品组合的图片生成器
![output.png](output.png)

## 项目简介

`maicard-py` 是一个使用 Python 编写的工具，用于生成玩家收藏品组合的图片。通过提供玩家的相关数据，该工具可以生成一张与机台上方副屏风格相似的图片。

## 安装

### 环境要求

- Python 3.12+
- pip

### 安装依赖

克隆项目到本地；

通过[该链接](https://alist.error063.work/Games/res.zip)下载项目的资源文件，然后将压缩包中的`res`文件夹复制到项目根目录中；

在项目根目录下运行以下命令安装所需的依赖：

```sh 
pip install -r requirements.txt
```

## 使用方法

### 命令行调用

你可以通过命令行调用 `generate_image.py` 脚本来生成图片。以下是一个示例命令：

```sh 
python generate_image.py --nickname "你的昵称" --title "你的称号" --icon 12345 --frame 12345 --plate 12345 --rating 67890 --classRank 5 --courseRank 8 --titleRare "Rare" --version "Ver.CN1.45-E" --chara 12345 67890 11111 22222 33333 --charaLevel 9999 9999 9999 9999 9999
```

### 参数说明

|       参数       |  类型  |                   默认值                    |      描述       |
|:--------------:|:----:|:----------------------------------------:|:-------------:|
|  `--nickname`  | str  |                "Ｈｏｓｈｉｎｏ☆"                |     玩家昵称      |
|   `--title`    | str  |              "游戏中心岛今天也很平静呢"              |     玩家称号      |
|    `--icon`    | int  |                  350101                  |    玩家头像ID     |
|   `--frame`    | int  |                  350101                  |    玩家背景板ID    |
|   `--plate`    | int  |                  350101                  |    玩家姓名框ID    |
|   `--rating`   | int  |                  12345                   |   玩家Rating    |
| `--classRank`  | int  |                    7                     |   玩家友人对战等级    |
| `--courseRank` | int  |                    10                    |   玩家段位认定等级    |
| `--titleRare`  | str  |                 "Normal"                 |    玩家称号稀有度    |
|   `--chara`    | list | [350105, 350104, 350103, 350102, 350101] | 玩家设置的旅行伙伴ID列表 |
| `--charaLevel` | list |      [9999, 9999, 9999, 9999, 9999]      | 玩家设置的旅行伙伴等级列表 |
|   `--output`   | str  |               "output.png"               |    图片输出路径     |

### 示例输出
运行上述命令后，将在用户指定目录下生成图片，并显示该图片。

