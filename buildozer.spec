[app]
# 基础配置
title = Comic Reader
package.name = comicreader
package.domain = org.kivy
version = 1.0.0

# 构建配置
requirements = 
    python3==3.10.5,
    kivy==2.3.0,
    pillow==10.1.0,
    pyjnius==1.5.0,
    android

# Android 配置（使用最新参数）
android.api = 34
android.minapi = 21
android.ndk_version = 25b
android.archs = arm64-v8a  # 替换废弃的 android.arch

# 移除废弃参数
# android.sdk = 34  # 已废弃
# android.ndk = 25b  # 改用 android.ndk_version

# 其他配置
orientation = portrait
fullscreen = 0