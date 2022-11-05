# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'map.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_Map(object):
    def setupUi(self, Map):
        if not Map.objectName():
            Map.setObjectName(u"Map")
        Map.resize(400, 300)
        self.map = QLabel(Map)
        self.map.setObjectName(u"map")
        self.map.setGeometry(QRect(40, 40, 321, 211))
        self.mapInfo = QLabel(Map)
        self.mapInfo.setObjectName(u"mapInfo")
        self.mapInfo.setGeometry(QRect(30, 260, 321, 31))

        self.retranslateUi(Map)

        QMetaObject.connectSlotsByName(Map)
    # setupUi

    def retranslateUi(self, Map):
        Map.setWindowTitle(QCoreApplication.translate("Map", u"map", None))
        self.map.setText(QCoreApplication.translate("Map", u"TextLabel", None))
        self.mapInfo.setText(QCoreApplication.translate("Map", u"TextLabel", None))
    # retranslateUi

