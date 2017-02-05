# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

import ipaddress
import socket
import time
import os
import psutil
import sys
import ctypes
import winreg
from PyQt5 import QtCore, QtGui, QtWidgets
from psutil import virtual_memory

now = time.localtime() #현재 시간
time = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

mem = virtual_memory() # RAM 정보

pid = os.getpid() # 메모리 사용량 정보
py = psutil.Process(pid)
memoryUse = py.memory_info()[0]/2.**30



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(634, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 231, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 5, 0, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.listWidget.setFont(font)
        self.listWidget.setIconSize(QtCore.QSize(50, 50))
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setModelColumn(0)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setBatchSize(200)
        self.listWidget.setWordWrap(False)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        item.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Desktop/스크린샷 2017-02-01 오후 4.21.30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Desktop/스크린샷 2017-02-01 오후 4.24.31.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Desktop/스크린샷 2017-02-01 오후 4.30.29.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../Desktop/스크린샷 2017-02-01 오후 4.30.49.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.listWidget)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(230, 0, 411, 561))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(30, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_ip = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_ip.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_ip.setObjectName("label_ip")
        self.verticalLayout_2.addWidget(self.label_ip)
        self.label_access = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_access.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_access.setObjectName("label_access")
        self.verticalLayout_2.addWidget(self.label_access)
        self.label_ip_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_ip_v.setEnabled(True)
        self.label_ip_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_ip_v.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_ip_v.setObjectName("label_ip_v")
        self.verticalLayout_2.addWidget(self.label_ip_v)
        self.label_mac = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_mac.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_mac.setObjectName("label_mac")
        self.verticalLayout_2.addWidget(self.label_mac)
        self.label_mac_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_mac_v.setEnabled(True)
        self.label_mac_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_mac_v.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_mac_v.setObjectName("label_mac_v")
        self.verticalLayout_2.addWidget(self.label_mac_v)
        self.label_name = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_name.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_name.setObjectName("label_name")
        self.verticalLayout_2.addWidget(self.label_name)
        self.label_name_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_name_v.setEnabled(True)
        self.label_name_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_name_v.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_name_v.setObjectName("label_name_v")
        self.verticalLayout_2.addWidget(self.label_name_v)
        self.label_cpu = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_cpu.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_cpu.setObjectName("label_cpu")
        self.verticalLayout_2.addWidget(self.label_cpu)
        self.label_cpu_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_cpu_v.setEnabled(True)
        self.label_cpu_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_cpu_v.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_cpu_v.setObjectName("label_cpu_v")
        self.verticalLayout_2.addWidget(self.label_cpu_v)
        self.label_ram = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_ram.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_ram.setObjectName("label_ram")
        self.verticalLayout_2.addWidget(self.label_ram)
        self.label_ram_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_ram_v.setEnabled(True)
        self.label_ram_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_ram_v.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_ram_v.setObjectName("label_ram_v")
        self.verticalLayout_2.addWidget(self.label_ram_v)
        self.label_access_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_access_v.setEnabled(True)
        self.label_access_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_access_v.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_access_v.setObjectName("label_access_v")
        self.verticalLayout_2.addWidget(self.label_access_v)
        self.label_usage = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_usage.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_usage.setObjectName("label_usage")
        self.verticalLayout_2.addWidget(self.label_usage)
        self.label_usage_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_usage_v.setEnabled(True)
        self.label_usage_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_usage_v.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_usage_v.setObjectName("label_usage_v")
        self.verticalLayout_2.addWidget(self.label_usage_v)
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.listWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 22))
        self.menubar.setObjectName("menubar")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsetting = QtWidgets.QAction(MainWindow)
        self.actionsetting.setObjectName("actionsetting")
        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.menuSetting.addAction(self.actionsetting)
        self.menuHelp.addAction(self.actionhelp)
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('www.naver.com', 0))
      #  i = Ram_info()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HackerViewer"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Sung Kyungmo"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Park Minwoo"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Choi Jinseok"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Kim Heejoong"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_ip.setText(_translate("MainWindow", "IP : "+s.getsockname()[0]))
        self.label_access.setText(_translate("MainWindow", "Access Time"))
        self.label_ip_v.setText(_translate("MainWindow", ""+str(time)))
        self.label_mac.setText(_translate("MainWindow", "MAC"))
        self.label_mac_v.setText(_translate("MainWindow", "null"))
        self.label_name.setText(_translate("MainWindow", "NAME"))
        self.label_name_v.setText(_translate("MainWindow", ""+socket.gethostname()))
        self.label_cpu.setText(_translate("MainWindow", "CPU"))
        self.label_cpu_v.setText(_translate("MainWindow", "null"))
        self.label_ram.setText(_translate("MainWindow", "RAM"))
        self.label_ram_v.setText(_translate("MainWindow", "")) #i.totalRam
        self.label_access_v.setText(_translate("MainWindow", "null"))
        self.label_usage.setText(_translate("MainWindow", "Usage Time"))
        self.label_usage_v.setText(_translate("MainWindow", "Memory Usage :"+str(memoryUse)))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionsetting.setText(_translate("MainWindow", "setting"))
        self.actionhelp.setText(_translate("MainWindow", "help"))



def get_registry_value(key, subkey, value):
    if sys.platform != 'win32':
        raise OSError("get_registry_value is only supported on Windows")

    import winreg
    key = getattr(winreg, key)
    handle = winreg.OpenKey(key, subkey)
    (value, type) = winreg.QueryValueEx(handle, value)
    return value
#
# class Ram_info:
#     def __init__(self):
#         self.os = self._os_version().strip()
#         self.cpu = self._cpu().strip()
#         self.browsers = self._browsers()
#         self.totalRam, self.availableRam = self._ram()
#         self.totalRam = self.totalRam / (1024 * 1024)
#         self.availableRam = self.availableRam / (1024 * 1024)
#         self.hdFree = self._disk_c() / (1024 * 1024 * 1024)
#
#     def _os_version(self):
#         def get(key):
#             return get_registry_value(
#                 "HKEY_LOCAL_MACHINE",
#                  "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion",
#                 key)
#
#         os = get("ProductName")
#         sp = get("CSDVersion")
#         build = get("CurrentBuildNumber")
#         return "%s %s (build %s)" % (os, sp, build)
#
#     def _cpu(self):
#         return get_registry_value(
#             "HKEY_LOCAL_MACHINE",
#             "HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0",
#             "ProcessorNameString")
#
#     def _browsers(self):
#         browsers = []
#         firefox = self._firefox_version()
#         if firefox:
#              browsers.append(firefox)
#         iexplore = self._iexplore_version()
#         if iexplore:
#             browsers.append(iexplore)
#
#         return browsers
#
#     def _ram(self):
#         kernel32 = ctypes.windll.kernel32
#         c_ulong = ctypes.c_ulong
#
#         class MEMORYSTATUS(ctypes.Structure):
#             _fields_ = [
#                 ('dwLength', c_ulong),
#                 ('dwMemoryLoad', c_ulong),
#                 ('dwTotalPhys', c_ulong),
#                 ('dwAvailPhys', c_ulong),
#                 ('dwTotalPageFile', c_ulong),
#                 ('dwAvailPageFile', c_ulong),
#                 ('dwTotalVirtual', c_ulong),
#                 ('dwAvailVirtual', c_ulong)
#             ]
#
#         memoryStatus = MEMORYSTATUS()
#         memoryStatus.dwLength = ctypes.sizeof(MEMORYSTATUS)
#         kernel32.GlobalMemoryStatus(ctypes.byref(memoryStatus))
#         return (memoryStatus.dwTotalPhys, memoryStatus.dwAvailPhys)
#
#         return freeuser.value


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

