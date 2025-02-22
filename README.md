# maicard-flask
改为flask api，以不占用过多的bot性能。
更新res文件至prism版本[res_new.rar(谷歌云盘)](https://drive.google.com/file/d/1Pn416VpaAHTff3__3SkYKwxZjLzlmZRg/view?usp=sharing)

*card*
玩家收藏品组合的图片生成器
![output.png](/gen_pic/output_image.png)
*raking*
推荐乐曲排行榜生成器
![output.png](/gen_pic/output.png)

## 项目简介

`maicard-flask` 是一个基于 Flask 的应用，用于生成各式各样的 maimai 相关图片。

## 安装

### 环境要求

- Python 3.12+
- pip

### 安装依赖

克隆项目到本地；

下载项目的资源文件，然后将压缩包中的`res`文件夹复制到项目根目录中；

在项目根目录下运行以下命令安装所需的依赖：

```sh 
pip install -r requirements.txt
```

## 使用方法

### 调用
访问api根地址查看可调用api


### POST参数说明
#### card

|       参数       |  类型  |                   默认值                    |      描述       |
|:--------------:|:----:|:----------------------------------------:|:-------------:|
|  `nickname`  | str  |                "Ｈｏｓｈｉｎｏ☆"                |     玩家昵称      |
|   `title`    | str  |              "游戏中心岛今天也很平静呢"              |     玩家称号      |
|    `icon`    | int  |                  350101                  |    玩家头像ID     |
|   `frame`    | int  |                  350101                  |    玩家背景板ID    |
|   `plate`    | int  |                  350101                  |    玩家姓名框ID    |
|   `rating`   | int  |                  12345                   |   玩家Rating    |
| `classRank`  | int  |                    7                     |   玩家友人对战等级    |
| `courseRank` | int  |                    10                    |   玩家段位认定等级    |
| `titleRare`  | str  |                 "Normal"                 |    玩家称号稀有度    |
|   `chara`    | list | [350105, 350104, 350103, 350102, 350101] | 玩家设置的旅行伙伴ID列表 |
| `charaLevel` | list |      [9999, 9999, 9999, 9999, 9999]      | 玩家设置的旅行伙伴等级列表 |
|   `output`   | str  |               "output.png"               |    图片输出路径     |

### 示例输出
运行上述命令后，将在用户指定目录下生成图片，并显示该图片。

