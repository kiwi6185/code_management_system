import sys
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.QtSql import QSqlRecord
from PyQt5.QtCore import pyqtSlot
from Ui_QWDialogData import Ui_QWDialogData


class QmyDialogData(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)        #调用父类构造函数，创建窗体
        self.ui=Ui_QWDialogData()       #创建UI对象
        self.ui.setupUi(self)       #构造UI界面
        
        self.__record=QSqlRecord()       #用于存储一条记录的数据
        
    def setUpdateRecord(self,recData):##设置更新记录的数据
        self.__record=recData
        self.ui.dbEditBirth.setEnabled(False)       #员工编号不允许编辑
        self.ui.dbEditName.setEnabled(False)       #员工编号不允许编辑
        self.ui.dbComboCareer.setEnabled(False)       #员工编号不允许编辑
        self.setWindowTitle("更新记录")
        
        birth = recData.value("PR_time")
        self.ui.dbEditBirth.setText(str(birth))
        
        self.ui.dbEditName.setText(recData.value( "UNO"))
        self.ui.dbComboCareer.setCurrentText(recData.value("career"))
        
        self.ui.dbComboIsMerge.setCurrentText(str(recData.value("is_merge")))
        self.ui.dbEditCodePath.setPlainText(recData.value( "code"))
        
    @pyqtSlot()
    def setInsertRecord(self,recData):      ##设置插入记录的数据
        self.__record=recData
        self.setWindowTitle("插入新记录")
        self.ui.dbComboCareer.setEnabled(False)
        self.ui.dbEditBirth.setEnabled(False)
        

    @pyqtSlot()
    def getRecordData(self):        ##返回界面编辑的数据
#        print("这是可以收到的 " + self.ui.dbEditBirth.text())
#        print("这是可以收到的 " + self.ui.dbEditName.text())
#        print("这是可以收到的 " + self.ui.dbComboCareer.currentText())
#        print("这是可以收到的 " + self.ui.dbComboIsMerge.currentText())
#        print("这是可以收到的 " + self.ui.dbEditCodePath.toPlainText())
        # 这里没问题都收到了
        self.__record.setValue("PR_time", self.ui.dbEditBirth.text())
        self.__record.setValue( "UNO", self.ui.dbEditName.text())
        self.__record.setValue("career",self.ui.dbComboCareer.currentText())
        self.__record.setValue("is_merge",self.ui.dbComboIsMerge.currentText())
        self.__record.setValue("code",self.ui.dbEditCodePath.toPlainText())
        return self.__record     #以记录作为返回值
        
if __name__== "__main__":       #用于当前窗体测试
    app = QApplication(sys.argv)        #创建GUI应用程序
    form=QmyDialogData()        #创建窗体
    form.show()     
    sys.exit(app.exec_())
