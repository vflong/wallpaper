# 从 bing 和 Windows 10 Spotlight 获取图片并设置为壁纸
1. 保存图片列表，图片插入日期，当前壁纸等信息到 sqlite3

```bash
# python 版本
Python 3.6.3

# 安装依赖库
pip install -r requirements.txt

# 从 bing 获取壁纸
python get_bing_wallpaper.py
python get_bingcom_wallpaper.py

# 从 Spotlight 获取壁纸
python get_spotlight_wallpaper.py

# 设置随机壁纸
python change_wallpaper.py
```