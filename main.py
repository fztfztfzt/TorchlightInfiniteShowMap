import sys
from time import sleep
from PySide6 import  QtWidgets, QtGui
from PySide6.QtCore import Signal,Qt,QThread,QRect
import pyautogui
import keyboard
import threading
import os
from paddleocr import PaddleOCR
import ui_map

pause = False
class MapThead(QThread):
    showmap = Signal(str)
    def __init__(self) -> None:
        super().__init__()
        self.pocr = PaddleOCR(use_angle_cls=True, lang='ch') 
    def run(self):
        while True:
            if not pause:
                name = self.GetName()
                if name :
                    self.showmap.emit(name)
                else:
                    self.showmap.emit(None)
            sleep(1)
    def GetRegion(self):
        with open("region.txt","r",encoding="utf8") as infoFile:
            pos = infoFile.readline().strip()
            return list(map(int,pos.split(',')))

    def GetName(self):
        img = pyautogui.screenshot(region=self.GetRegion())
        img.save("img.png")
        # res = self.ocr.ocr(im)
        # print(res)
        # if len(res) == 0:
        #     return None
        ans = self.pocr.ocr("img.png", cls=True)
        if len(ans[0]) == 0:
            return None
        result = ans[0][0][1][0]
        # result = res[0]['text']
        if len(result) >=6:
            result = result[3:]
        print(f"识别结果:{result}")
        return result

class MapWidget(QtWidgets.QWidget):
    curname = None
    def __init__(self):
        super().__init__()
        self.stopFlag = False
        self.ui = ui_map.Ui_Map()#实例化UI对象
        self.ui.setupUi(self)#初始化
        self.th = MapThead()
        self.th.showmap.connect(self.ShowMap)
        self.th.start()
        self.mapInfo={}
        with open("info.txt","r",encoding="utf8") as infoFile:
            count = 0
            name = ""
            for line in infoFile:
                line = line.strip()
                if count%2 == 0:
                    name = line
                else:
                    self.mapInfo[name] = line
                count += 1
        

    def ShowMap(self,name):
        if name == self.curname:
            return
        self.curname = name
        if name:
            self.show()
            path = f'map/{name}.jpg'
            if not os.path.exists(path):
                self.ui.map.setText(f"识别的名字{name},可手动修改文件名匹配下")
            else:
                mapName = f'map/{name}.jpg'
                pix = QtGui.QPixmap(mapName)
                size =pix.size()
                self.ui.map.setGeometry(0,0,size.width(),size.height())
                self.resize(size.width(),size.height()+40)
                self.ui.map.setPixmap(pix)
                self.ui.mapInfo.setGeometry(QRect(30, size.height()+10, 321, 31))
                self.ui.mapInfo.setText(f"信息：{self.mapInfo[name]}")
        else:
            self.hide()
        

def Stop():
    global pause
    pause = not pause

def ListenRun():
    keyboard.add_hotkey("F1",Stop)
    keyboard.wait()
            
if __name__ == "__main__":
    threading.Thread(target=ListenRun).start()
    app = QtWidgets.QApplication([])
    widget = MapWidget()
    widget.setWindowFlags(Qt.WindowStaysOnTopHint) #置顶
    widget.show()
    sys.exit(app.exec())