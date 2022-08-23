# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QWDialogData.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QWDialogData(object):
    def setupUi(self, QWDialogData):
        QWDialogData.setObjectName("QWDialogData")
        QWDialogData.resize(538, 306)
        self.gridLayout_2 = QtWidgets.QGridLayout(QWDialogData)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBoxRight = QtWidgets.QGroupBox(QWDialogData)
        self.groupBoxRight.setTitle("")
        self.groupBoxRight.setObjectName("groupBoxRight")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxRight)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.groupBoxRight)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 2)
        self.dbEditBirth = QtWidgets.QLineEdit(self.groupBoxRight)
        self.dbEditBirth.setObjectName("dbEditBirth")
        self.gridLayout.addWidget(self.dbEditBirth, 0, 2, 1, 1)
        self.dbComboCareer = QtWidgets.QComboBox(self.groupBoxRight)
        self.dbComboCareer.setObjectName("dbComboCareer")
        self.dbComboCareer.addItem("")
        self.dbComboCareer.addItem("")
        self.dbComboCareer.addItem("")
        self.gridLayout.addWidget(self.dbComboCareer, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBoxRight)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBoxRight)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 2)
        self.dbEditCodePath = QtWidgets.QPlainTextEdit(self.groupBoxRight)
        self.dbEditCodePath.setObjectName("dbEditCodePath")
        self.gridLayout.addWidget(self.dbEditCodePath, 5, 2, 1, 1)
        self.dbComboIsMerge = QtWidgets.QComboBox(self.groupBoxRight)
        self.dbComboIsMerge.setObjectName("dbComboIsMerge")
        self.dbComboIsMerge.addItem("")
        self.dbComboIsMerge.addItem("")
        self.gridLayout.addWidget(self.dbComboIsMerge, 3, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBoxRight)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.dbEditName = QtWidgets.QLineEdit(self.groupBoxRight)
        self.dbEditName.setObjectName("dbEditName")
        self.gridLayout.addWidget(self.dbEditName, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBoxRight)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBoxRight, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(QWDialogData)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnOK = QtWidgets.QPushButton(self.frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/kiwi_ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOK.setIcon(icon)
        self.btnOK.setObjectName("btnOK")
        self.verticalLayout.addWidget(self.btnOK)
        self.btnClose = QtWidgets.QPushButton(self.frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/kiwi_cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClose.setIcon(icon1)
        self.btnClose.setObjectName("btnClose")
        self.verticalLayout.addWidget(self.btnClose)
        spacerItem = QtWidgets.QSpacerItem(20, 329, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 1)

        self.retranslateUi(QWDialogData)
        self.btnClose.clicked.connect(QWDialogData.reject) # type: ignore
        self.btnOK.clicked.connect(QWDialogData.accept) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(QWDialogData)

    def retranslateUi(self, QWDialogData):
        _translate = QtCore.QCoreApplication.translate
        QWDialogData.setWindowTitle(_translate("QWDialogData", "编辑记录"))
        self.label_6.setText(_translate("QWDialogData", "是否合并"))
        self.dbEditBirth.setInputMask(_translate("QWDialogData", "9999-99-99 99:99:99"))
        self.dbComboCareer.setItemText(0, _translate("QWDialogData", "开发者"))
        self.dbComboCareer.setItemText(1, _translate("QWDialogData", "测试人员"))
        self.dbComboCareer.setItemText(2, _translate("QWDialogData", "产品经理"))
        self.label_3.setText(_translate("QWDialogData", "提 交 者"))
        self.label_4.setText(_translate("QWDialogData", "职    业"))
        self.dbComboIsMerge.setItemText(0, _translate("QWDialogData", "是"))
        self.dbComboIsMerge.setItemText(1, _translate("QWDialogData", "否"))
        self.label_7.setText(_translate("QWDialogData", "代码路径"))
        self.label_2.setText(_translate("QWDialogData", "提交时间"))
        self.btnOK.setText(_translate("QWDialogData", "确定"))
        self.btnClose.setText(_translate("QWDialogData", "取消"))
import res_rc
