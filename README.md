# TorchlightInfiniteShowMap

#### 介绍
在选择地图界面显示小地图和地图怪物信息，需要配置地图名字位置

本脚本使用ocr进行文字识别，识别率无法保证100%。识别错误时，可替换Map文件夹下图片名称，数据来源 https://nga.178.com/read.php?tid=33931854&fav=f5164a46

识别区域配置在 region.txt 文件中,参数为矩形左上角坐标和宽高，如 Sample.png 所示区域

info.txt存放各个地图需要显示的信息，目前是怪物数量，数据来源：https://nga.178.com/read.php?tid=34003311&fav=ed6f9b69


#### 安装教程

1.  需要 python3
2.  需要安装 PySide6,pyautogui,keyboard,paddleocr

#### 使用说明

1.  双击 run.bat运行

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request