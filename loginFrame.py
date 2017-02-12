from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QUrl
from joinFrame import JoinFrame
from model.user import User
from mongoDao import LoginDao
from myhttp import Communication
import webbrowser
from util import MyYaml


class LoginFrame(object):

    login_form = 1

    def __init__(self, form, view):
        super().__init__()

        self.login_form = form
        self.setupUi(form, view)
        form.show()

    def setupUi(self, Form, view):

        Form.setObjectName("Form")
        Form.resize(400, 300)

        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 60, 345, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_5.addWidget(self.lineEdit_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.addWidget(view)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_signin = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_signin.setObjectName("pushButton_signin")
        self.pushButton_signup = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_signup.setObjectName("pushButton_signup")
        self.pushButton_cancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_cancel.setObjectName("pushButton_cancel")


        self.pushButton_kakao = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_kakao.setIcon(QtGui.QIcon('img/kakao_login.png'))
        self.pushButton_kakao.setIconSize(QtCore.QSize(226, 49))
        self.pushButton_kakao.setObjectName("pushButton_kakao")
        self.pushButton_kakao.setFixedWidth(226)
        self.pushButton_kakao.setFixedHeight(49)

        self.horizontalLayout.addWidget(self.pushButton_signin)
        self.horizontalLayout.addWidget(self.pushButton_signup)
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.pushButton_kakao)
        self.verticalLayoutWidget.raise_()



        self.retranslateUi(Form)


        self.pushButton_cancel.clicked.connect(self.btnOkClicked)
        self.pushButton_signin.clicked.connect(self.btnOkClicked)
        self.pushButton_signup.clicked.connect(JoinFrame.widget_show)
        self.pushButton_kakao.clicked.connect(self.btnKaKaoClicked)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.label.setText(_translate("Form", "ID"))
        self.label_2.setText(_translate("Form", "PW"))

        self.pushButton_cancel.setText(_translate("Form", "Cancel"))
        self.pushButton_signin.setText(_translate("Form", "Sign in"))
        self.pushButton_signup.setText(_translate("Form", "Sign up"))

    def btnOkClicked(self, i):

        my_id = self.lineEdit.text()
        my_pw = self.lineEdit_2.text()
        if LoginDao.login(my_id, my_pw):
            self.login_form.hide()
            Communication.login(my_id)
            User.u_id = my_id

        else:
            self.showdialog()

    def btnKaKaoClicked(self):

        #webbrowser.open('http://'+MyYaml.node_js_host+':'+str(MyYaml.node_js_port))
        webbrowser.open('https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fredirect_uri%3Dkakaojs%26response_type%3Dcode%26state%3Dufa89hrnbheqsau6u92cpu8fr%26client_id%3D3dee48e4ccc6b7755390974f30a54832')

    def showdialog(self):
        d = QDialog()
        b1 = QPushButton("Ok", d)
        b1.move(50, 50)
        d.setWindowTitle("Fail")
        d.setWindowModality(Qt.ApplicationModal)
        d.exec_()
