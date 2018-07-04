# 从 bing 和 Windows 10 Spotlight 获取图片并设置为壁纸

[![Build status](https://ci.appveyor.com/api/projects/status/de4cgyjm8ep3evar?svg=true)](https://ci.appveyor.com/project/vflong/wallpaper)

1. 保存图片列表，图片插入日期，当前壁纸等信息到 sqlite3

```bash
# python 版本
Python 3.6.3

# 安装依赖库
pipenv install

# 从 bing 获取壁纸
python get_bing_wallpaper.py
python get_bingcom_wallpaper.py

# 从 Spotlight 获取壁纸
python get_spotlight_wallpaper.py

# 设置随机壁纸
python change_wallpaper.py
```
