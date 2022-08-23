import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QMessageBox, QDialog
from PyQt5.QtCore import Qt, pyqtSlot, QItemSelectionModel,  QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPainter, QPen
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel,  QSqlTableModel
from PyQt5.QtChart import *
from myDialogData import QmyDialogData
from Ui_MainWindow import Ui_MainWindow
import time

class QmyMainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        self.is_tab0 = 1
        self.is_generate = 0
        super().__init__(parent)        #调用父类构造函数，创建窗体
        self.ui=Ui_MainWindow()     #创建UI对象
        self.ui.setupUi(self)       #构造UI界面
        
        self.setWindowTitle("代码托管平台")
        
        #隔行变色
        self.ui.PR_view.setAlternatingRowColors(True)
        self.ui.Issues_view.setAlternatingRowColors(True)
        self.ui.treeWidget.setAlternatingRowColors(True)
        self.setStyleSheet("QTreeWidget,QTableView{"
        + "alternate-background-color:rgb(170,241,190)}")
        
        self.qryModel=QSqlQueryModel(self)
        self.dataModel=QItemSelectionModel(self.qryModel)    #关联选择模型
        self.ui.PR_view.setModel(self.qryModel)   #设置数据模型           # 注意这两行的区别
        
        self.dataModel_issues = QStandardItemModel(self)   #数据模型
        self.ui.Issues_view.setModel(self.dataModel_issues)      #设置数据模型
        
        self.ui.tabWidget_2.currentChanged.connect(self.tabchange)
        
#        self.__iniBarChart()    #柱状图初始化
#        self.__iniStackedBar()     #堆积图初始化
        self.__iniPercentBar()      #百分比图初始化
        self.__iniPieBar()      #饼图初始化
        
        
    def on_actOpenDB_triggered(self):
        #打开数据库
        self.DB = QSqlDatabase.addDatabase("QODBC")
        self.DB.setDatabaseName("Driver={Sql Server};Server=localhost;Database=LSX25pyqt5;Uid=sa;Pwd=123")
        if self.DB.open():  #打开数据库
#            QMessageBox.warning(self, "正确", "打开数据库成功")
#            self.__openTable()      #旧的打开数据库
            self.__generateData()   #初始化数据
            self.__surveyData() #统计issues分布段位
            if self.is_tab0 == 1:
                self.tabchange(0)
        else:
            QMessageBox.warning(self, "错误", "打开数据库失败")
            
    def __getFieldNames(self):  ##获取所有字段的名称
        emptyRec = self.tabModel.record()  #获取空记录，只有字段名
        self.fldNum = {}   #字段名与序号的字典
        for i in range(emptyRec.count()):
            fieldName = emptyRec.fieldName(i)
#            self.ui.comboFields.addItem(fieldName)
            self.fldNum.setdefault(fieldName)
            self.fldNum[fieldName] = i

    def do_currentRowChanged(self,current, previous):   ##行切换时触发
        if (current.isValid()==False):
            return
        curRec=self.tabModel.record(current.row())      #获取当前记录,QSqlRecord类型
        time=curRec.value("PR_time")     #不需要加toInt()函数
        
        person=curRec.value("UNO")     #不需要加toInt()函数
        self.ui.statusbar.showMessage("当前记录：提交时间：" + str(time) + " 提交者：" + str(person))

    def tabchange(self, x):
        # 下标从0开始
        if x == 0:
            self.ui.actRecInsert.setEnabled(True)
            self.ui.actRecDelete.setEnabled(True)
            self.ui.actRecEdit.setEnabled(True)
            self.ui.actScan.setEnabled(True)
            if self.is_generate == 1:
                self.ui.groupBoxFilter.setEnabled(True)
        else:
            self.ui.actRecInsert.setEnabled(False)
            self.ui.actRecDelete.setEnabled(False)
            self.ui.actRecEdit.setEnabled(False)
            self.ui.actScan.setEnabled(False)
            self.ui.groupBoxFilter.setEnabled(False)
            
    def __generateData(self):       ##生成分数数据
        #PR表
        self.dataModel.clear()
        
        self.qryModel=QSqlQueryModel(self) # 就是这个东西 打开数据库的时候用的好像 看看你的代码数据库那里
        self.qryModel.setQuery("select PR_time, PR.UNO, users.career, is_merge, code from PR, users where PR.UNO = users.UNO")
        
        # 把 qryModel 传给 QItemSelectionModel 得到 那个关联的选择模型
        self.tabModel=QSqlTableModel(self, self.DB) #数据模型
        self.tabModel.setTable("PR")  #设置数据表
        self.tabModel.setEditStrategy(QSqlTableModel.OnManualSubmit)  # 数据保存方法，OnManualSubmit，OnRowChange
        self.tabModel.setSort(self.tabModel.fieldIndex("PR_time"), Qt.AscendingOrder)     #排序
        
        
        self.ui.PR_view.setModel(self.tabModel)   #设置数据模型           # 注意这两行的区别
        self.dataModel=QItemSelectionModel(self.tabModel)    # 关联选择模型
        self.ui.PR_view.setSelectionModel(self.dataModel)  #设置选择模型
        self.dataModel.currentChanged.connect(self.do_currentChanged)     #当前项变化时触发
        self.dataModel.currentRowChanged.connect(self.do_currentRowChanged)
        
        
        self.__getFieldNames()  #获取字段名和序号，查询数据后立即调用
            
        self.tabModel.setHeaderData(0, Qt.Horizontal, "提交时间")
        self.tabModel.setHeaderData(1, Qt.Horizontal, "提交者")
        self.tabModel.setHeaderData(2, Qt.Horizontal, "是否合并")
        self.tabModel.setHeaderData(3, Qt.Horizontal, "代码路径")
        
        if (self.tabModel.select() == False):       #查询数据失败
            QMessageBox.critical(self, "错误信息", 
                "打开数据库错误，错误信息\n" + self.tabModel.lastError().text())
            return
        
        self.ui.PR_view.resizeColumnsToContents()   #调整
        self.is_generate = 1
    
        #issues表
        self.dataModel_issues.clear()
        headerList=["提交时间", "提交者", "提交者职业", "是否解决", "优先级",  "bug内容"]
        self.dataModel_issues.setHorizontalHeaderLabels(headerList)        #设置表头文字
        
        qryStudList=QSqlQuery(self.DB)      #学生信息列表
        qryStudList.exec("select INO, issues.UNO, users.career, is_solve, priority, content from issues, users where issues.UNO = users.UNO")
        
        qryStudList.first()
        while (qryStudList.isValid()):      #当前记录有效
            itemList=[]
            INO=qryStudList.value("INO")
            item=QStandardItem(INO)        #创建item
            item.setTextAlignment(Qt.AlignCenter)
            itemList.append(item)      #添加到列表
            
            UNO=qryStudList.value("UNO")
            item=QStandardItem(UNO)        #创建item
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(item.flags() & (not Qt.ItemIsEditable))
            itemList.append(item)       #添加到列表
            
            career=qryStudList.value("career")
            item=QStandardItem(career)        #创建item
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(item.flags() & (not Qt.ItemIsEditable))
            itemList.append(item)       #添加到列表

            is_solve=qryStudList.value("is_solve")
            if is_solve == 0:
                item=QStandardItem("否")     #创建item
            else:
                item=QStandardItem("是")     #创建item
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(item.flags() & (not Qt.ItemIsEditable))
            itemList.append(item)       #添加到列表
            
            priority =qryStudList.value("priority")
            item=QStandardItem(str(priority))     #创建item
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(item.flags() & (not Qt.ItemIsEditable))
            itemList.append(item)       #添加到列表
            
            content =qryStudList.value("content")
            item=QStandardItem(content)     #创建item
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(item.flags() & (not Qt.ItemIsEditable))
            itemList.append(item)       #添加到列表
            
            self.dataModel_issues.appendRow(itemList)      #添加到数据模型
            if not qryStudList.next():      #移动到下一条记录，并判断是否到末尾了
                break
        
    def __surveyData(self):     ##统计各分数段人数
        for i in range(1, 6):       #range(1,6)即从1到5
            solve,  unsolve=0, 0
            for j in range(self.dataModel_issues.rowCount()):      #行数等于人数
                val=int(self.dataModel_issues.item(j,4).text())      #优先级
                if val == i:
                    if self.dataModel_issues.item(j,3).text() == '是':     #已解决
                        solve = solve + 1
                    else:
                        unsolve = unsolve + 1
            
            item=self.ui.treeWidget.topLevelItem(i - 1)     #第i - 1行，60
            item.setText(1,str(solve))          #第i列
            item.setTextAlignment(1,Qt.AlignHCenter)
            
            item.setText(2,str(unsolve))          #第i列
            item.setTextAlignment(2,Qt.AlignHCenter)
            
            
    @pyqtSlot()  ##过滤，未合并
    def on_radioBtnMan_clicked(self):
        self.tabModel.setFilter("is_merge=0")

    @pyqtSlot()  ##过滤，已合并
    def on_radioBtnWoman_clicked(self):
        self.tabModel.setFilter("is_merge=1")

    @pyqtSlot()  ##取消数据过滤
    def on_radioBtnBoth_clicked(self):
        self.tabModel.setFilter("")
    
    @pyqtSlot()
    def on_actRecEdit_triggered(self): 
        curRecNo=self.dataModel.currentIndex().row()
        # print("没有选中吗" + str(curRecNo))
        self.__updateRecord(curRecNo)
#        self.__generateData() # 罪魁祸首 
        
#    def on_PR_view_doubleClicked(self, index):
        #self.__updateRecord(index) 
            
    def __updateRecord(self,recNo):
        print(recNo)
        curRec = self.tabModel.record(recNo)  # 获取当前记录
        PR_time = curRec.value("PR_time")
        UNO = curRec.value("UNO")
        
        query = QSqlQuery(self.DB)
        query.prepare('''select PR_time, PR.UNO, users.career, is_merge, code 
                from PR, users where PR.UNO = users.UNO and PR_time = :PR_time and users.UNO = :UNO''')
        query.bindValue(":PR_time", PR_time)
        query.bindValue(":UNO", UNO)
        query.exec()
        query.first()
        if (not query.isValid()):
            print("查询无效")
            return

        curRec = query.record()  # 获取当前记录的数据，QSqlRecord模型
        dlgData = QmyDialogData(self)  # 创建对话框
        dlgData.setUpdateRecord(curRec)  # 调用对话框函数更新数据和界面
        ret = dlgData.exec()  # 以模态方法显示对话框
        if (ret != QDialog.Accepted):
            print("对话框不被接受")
            return

        print("对话框接受")
        
        recData = dlgData.getRecordData()  # 获取对话框的返回记录
        
        record = self.tabModel.record(recNo)
       
        record.setValue("is_merge",  recData.value("is_merge"))
        record.setValue("code",  recData.value("code"))
        # 在这里判断那个是否就可以然后set 不对我想想
        if (recData.value("is_merge") == "是"):
            record.setValue("is_merge",  1)
        else:
            record.setValue("is_merge",  0)
        self.tabModel.setRecord(recNo,  record) # 修改模型
        
        # 更新 UI
        self.ui.PR_view.reset()
        self.ui.PR_view.setModel(self.tabModel)
            
    @pyqtSlot()  ##添加记录
    def on_actRecAppend_triggered(self):
        self.tabModel.insertRow(self.tabModel.rowCount(),QModelIndex())     #在末尾添加一个记录

        curIndex = self.tabModel.index(self.tabModel.rowCount()-1, 1)       #创建最后一行的ModelIndex
        self.dataModel.clearSelection()      #清空选择项
        self.dataModel.setCurrentIndex(curIndex,QItemSelectionModel.Select)      #设置刚插入的行为当前选择行

        currow = curIndex.row()     #获得当前行
        time.time()
        nowTime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.tabModel.setData(self.tabModel.index(currow,self.fldNum["PR_time"]), nowTime)    #自动生成编号
        
    @pyqtSlot()     ##插入记录
    def on_actRecInsert_triggered(self):
        curIndex = self.ui.PR_view.currentIndex()     #QModelIndex
        self.tabModel.insertRow(curIndex.row(), QModelIndex())
        self.dataModel.clearSelection     #清除已有选择
        self.dataModel.setCurrentIndex(curIndex,QItemSelectionModel.Select)
        
        currow = curIndex.row()     #获得当前行
        time.time()
        nowTime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.tabModel.setData(self.tabModel.index(currow,self.fldNum["PR_time"]), nowTime)    #自动生成编号
            
    @pyqtSlot()  ##删除记录
    def on_actRecDelete_triggered(self):
        curIndex = self.dataModel.currentIndex()  ##获取当前选择单元格的模型索引
        self.tabModel.removeRow(curIndex.row())  ##删除当前行（没删掉，没有 submit）
            
    @pyqtSlot()
    def on_actScan_triggered(self):     #一键合并 
        if(self.tabModel.rowCount()==0):  #无数据，直接返回
            return
        
        for i in range(self.tabModel.rowCount()):
            aRec = self.tabModel.record(i)  #获取当前记录
            aRec.setValue("is_merge",  1)
            self.tabModel.setRecord(i, aRec)

        if(self.tabModel.submitAll()):
            print("123")
            QMessageBox.information(self,"消息","已合并所有的pull request")
        
    @pyqtSlot()  ##保存修改
    def on_actSubmit_triggered(self):
        res=self.tabModel.submitAll()
        if(res == False):
            QMessageBox.information(self,"消息",
                "数据保存错误，错误信息\n" + self.tabModel.lastError().text())
        else:
            self.ui.actSubmit.setEnabled(False)
            self.ui.actRevert.setEnabled(False)

    @pyqtSlot()  ##取消修改
    def on_actRevert_triggered(self):
        self.tabModel.revertAll()
        self.ui.actSubmit.setEnabled(False)
        self.ui.actRevert.setEnabled(False)
        
    ###########槽函数
    def do_currentChanged(self,current,previous):   ##更新actPost和actCancel的状态
        self.ui.actSubmit.setEnabled(self.tabModel.isDirty())  #有未保存修改时可用
        self.ui.actRevert.setEnabled(self.tabModel.isDirty())
            
##==============page 1，柱状图===================
#    def __iniBarChart(self):    ##初始化柱状图
#        chart = QChart()
#        chart.setTitle( "Barchart 演示")
#        self.ui.chartViewBar.setChart(chart)        #为ChartView设置chart
#        self.ui.chartViewBar.setRenderHint(QPainter.Antialiasing)       #打开 QPainter 的反走样功能（在计算机中绘制一条直线，会有明显的锯齿现象，这就叫走样）
#        self.ui.chartViewBar.setCursor(Qt.CrossCursor)      #设置鼠标指针为十字星
#        
#    @pyqtSlot()     ##绘制柱状图
#    def on_btnBuildBarChart_clicked(self):
#        self.draw_barChart()
#    
#    @pyqtSlot()     ##绘制水平柱状图
#    def on_btnBuildBarChartH_clicked(self):
#        self.draw_barChart(False)
#        
#    def draw_barChart(self,isVertical=True):        ##绘制柱状
#        chart = self.ui.chartViewBar.chart()
#        chart.removeAllSeries()     #删除所有序列
#        chart.removeAxis(chart.axisX())      #删除坐标轴
#        chart.removeAxis(chart.axisY())     #删除坐标轴
#        
#        if isVertical:
#            chart.setTitle("Barchart 演示")
#            chart.legend().setAlignment(Qt.AlignBottom)
#        else:
#            chart.setTitle("Horizontal Barchart 演示")
#            chart.legend().setAlignment(Qt.AlignRight)
#        
#        setTongshuai = QBarSet("统帅")
#        setWuli = QBarSet("武力")
#        setZhili = QBarSet("智力")
#        setZhengzhi = QBarSet("政治")
#        setMeili = QBarSet("魅力")
#        
#        seriesLine = QLineSeries()      #QLineSeries序列用于显示平均分
#        seriesLine.setName("平均分")
#        pen=QPen(Qt.red)
#        pen.setWidth(2)
#        seriesLine.setPen(pen)
#        seriesLine.setPointLabelsVisible(True)      #数据点标签可见
#        if isVertical:
#            seriesLine.setPointLabelsFormat("@yPoint")      #显示y数值标签
#        else:
#            seriesLine.setPointLabelsFormat("@xPoint")      #显示x数值标签
#        font=seriesLine.pointLabelsFont()
#        font.setPointSize(10)
#        font.setBold(True)
#        seriesLine.setPointLabelsFont(font)
#
#
#        stud_Count = self.dataModel.rowCount()
#        nameList = []
#        for i in range(stud_Count):     #从数据模型获取数据
#            item = self.dataModel.item(i, 0)    #第0列姓名
#            nameList.append(item.text())    #姓名，用作坐标轴标签
#        
#            item = self.dataModel.item(i, 1)    #第1列统帅
#            setTongshuai.append(float(item.text()))
#            
#            item = self.dataModel.item(i, 2)    #第2列武力
#            setWuli.append(float(item.text()))
#            
#            item = self.dataModel.item(i, 3)    #第3列智力
#            setZhili.append(float(item.text()))
#            
#            item = self.dataModel.item(i, 4)    #第4列政治
#            setZhengzhi.append(float(item.text()))
#            
#            item = self.dataModel.item(i, 5)    #第5列魅力
#            setMeili.append(float(item.text()))
#            
#            item = self.dataModel.item(i, 6)    #第6列平均
#            if isVertical:
#                seriesLine.append(i, float(item.text()))    #平均分，用于柱状图
#            else:
#                seriesLine.append(float(item.text()), i)    #平均分，用于水平柱状图
#        
#        #创建一个序列 QBarSeries，并加数据集
#        if isVertical:
#            seriesBar = QBarSeries()       #柱状图
#        else:
#            seriesBar = QHorizontalBarSeries()  #水平柱状图
#            
#        seriesBar.append(setTongshuai)      #添加数据集
#        seriesBar.append(setWuli)
#        seriesBar.append(setZhili)
#        seriesBar.append(setZhengzhi)
#        seriesBar.append(setMeili)
#        
#        seriesBar.setLabelsVisible(True)    #数据点标签可见
#        seriesBar.setLabelsFormat("@value")      #显示数值标签
#        seriesBar.setLabelsPosition(QAbstractBarSeries.LabelsCenter)        #数据标签显示位置
#        
#        seriesBar.hovered.connect(self.do_barSeries_Hovered)    #hovered信号
#        seriesBar.clicked.connect(self.do_barSeries_Clicked)    #clicked信号
#        
#        chart.addSeries(seriesBar)      #添加柱状图序列
#        
#        ##学生姓名坐标轴
#        axisStud = QBarCategoryAxis()
#        axisStud.append(nameList)   #添加横坐标文字
#        axisStud.setRange(nameList[0], nameList[stud_Count - 1])    #坐标轴范围
#        
#        #数值型坐标轴
#        axisValue = QValueAxis()
#        axisValue.setRange(0, 100)
#        axisValue.setTitleText("分数")
#        axisValue.setTickCount(6)       #刻度线数量
#        axisValue.applyNiceNumbers()        #让刻度线更好看
#        
#        if isVertical:
#            chart.setAxisX(axisStud, seriesBar)
#            chart.setAxisY(axisValue, seriesBar)
#            chart.setAxisX(axisStud, seriesLine)
#            chart.setAxisY(axisValue, seriesLine)
#        else:
#            chart.setAxisX(axisValue, seriesBar)
#            chart.setAxisY(axisStud, seriesBar)
#            chart.setAxisY(axisStud, seriesLine)
#            chart.setAxisX(axisValue, seriesLine)
#            
#        for marker in chart.legend().markers():       #QLegendMarker类型列表
#            marker.clicked.connect(self.do_LegendMarkerClicked)
#    
#            
    def do_barSeries_Hovered(self, status, index, barset):    # #关联hovered信号
        hint = "hovered barSet=" + barset.label()
        if status:
            hint = hint + ", index=%d, value=%.2f"%(index, barset.at(index))
        else:
            hint=""
        self.ui.statusbar.showMessage(hint)
        
    def do_barSeries_Clicked(self, index, barset):    # #关联clicked信号
        hint = "clicked barSet=" + barset.label()
        hint = hint + ", count=%d, sum=%.2f"%(barset.count(), barset.sum())
        self.ui.statusbar.showMessage(hint)
        
    def do_LegendMarkerClicked(self):       ##点击图例小方块
        #maker：信号的发射者
        marker =self.sender()       #QLegendMarker
        
        #maker关联的序列：显示变隐藏；隐藏变显示
        marker.series().setVisible(not marker.series().isVisible())
        #maker本身总是显示
        marker.setVisible(True)
        alpha = 1.0
        if not marker.series().isVisible():
            alpha = 0.5
            
        brush = marker.labelBrush()     #QBrush
        color = brush.color()       #QColor
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setLabelBrush(brush)
        
        brush = marker.brush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setBrush(brush)

        pen = marker.pen()      #QPen
        color = pen.color()
        color.setAlphaF(alpha)
        pen.setColor(color)
        marker.setPen(pen)
        
###==================page 2.StackedBar================
#    def __iniStackedBar(self):      ##初始化堆叠柱状图
#        chart = QChart()
#        chart.setTitle("stackedBar 演示")
#        self.ui.chartViewStackedBar.setChart(chart)     #为ChartView设置chart
#        self.ui.chartViewStackedBar.setRenderHint(QPainter.Antialiasing)
#        self.ui.chartViewStackedBar.setCursor(Qt.CrossCursor)       #设置鼠标指针为十字星
#    
#    @pyqtSlot()     ##绘制stackedBar
#    def on_btnBuildStackedBar_clicked(self):
#        self.draw_stackedBar()
#    
#    @pyqtSlot()     ##绘制水平StackedBar
#    def on_btnBuildStackedBarH_clicked(self):
#        self.draw_stackedBar(False)
#
#    def draw_stackedBar(self,isVertical=True):        ##堆叠柱状图
#        chart = self.ui.chartViewStackedBar.chart()
#        chart.removeAllSeries()     #删除所有序列
#        chart.removeAxis(chart.axisX())      #删除坐标轴
#        chart.removeAxis(chart.axisY())     #删除坐标轴
#        
#        if isVertical:
#            chart.setTitle("StackedBar 演示")
#            chart.legend().setAlignment(Qt.AlignBottom)
#        else:
#            chart.setTitle("Horizontal StackedBar 演示")
#            chart.legend().setAlignment(Qt.AlignRight)
#        
#        setTongshuai = QBarSet("统帅")
#        setWuli = QBarSet("武力")
#        setZhili = QBarSet("智力")
#        setZhengzhi = QBarSet("政治")
#        setMeili = QBarSet("魅力")
#        
#        stud_Count = self.dataModel.rowCount()
#        nameList = []
#        for i in range(stud_Count):     #从数据模型获取数据
#            item = self.dataModel.item(i, 0)    #第0列姓名
#            nameList.append(item.text())    #姓名，用作坐标轴标签
#        
#            item = self.dataModel.item(i, 1)    #第1列统帅
#            setTongshuai.append(float(item.text()))
#            
#            item = self.dataModel.item(i, 2)    #第2列武力
#            setWuli.append(float(item.text()))
#            
#            item = self.dataModel.item(i, 3)    #第3列智力
#            setZhili.append(float(item.text()))
#            
#            item = self.dataModel.item(i, 4)    #第4列政治
#            setZhengzhi.append(float(item.text()))
#            
#            item = self.dataModel.item(i, 5)    #第5列魅力
#            setMeili.append(float(item.text()))
#            
#        
#        #创建一个序列
#        if isVertical:
#            seriesBar = QStackedBarSeries()       #柱状图
#        else:
#            seriesBar = QHorizontalStackedBarSeries()  #水平柱状图
#            
#        seriesBar.append(setTongshuai)      #添加数据集
#        seriesBar.append(setWuli)
#        seriesBar.append(setZhili)
#        seriesBar.append(setZhengzhi)
#        seriesBar.append(setMeili)
#        
#        seriesBar.setLabelsVisible(True)    #数据点标签可见
#        seriesBar.setLabelsFormat("@value")      #显示数值标签
#        seriesBar.setLabelsPosition(QAbstractBarSeries.LabelsCenter)        #数据标签显示位置
#        
#        seriesBar.hovered.connect(self.do_barSeries_Hovered)    #hovered信号
#        seriesBar.clicked.connect(self.do_barSeries_Clicked)    #clicked信号
#        
#        chart.addSeries(seriesBar)      #添加柱状图序列
#        
#        ##学生姓名坐标轴
#        axisStud = QBarCategoryAxis()
#        axisStud.append(nameList)   #添加横坐标文字
#        axisStud.setRange(nameList[0], nameList[stud_Count - 1])    #坐标轴范围
#        
#        #数值型坐标轴
#        axisValue = QValueAxis()
#        axisValue.setRange(0, 500)
#        axisValue.setTitleText("总分")
#        axisValue.setTickCount(6)       #刻度线数量
#        axisValue.applyNiceNumbers()        #让刻度线更好看
#        
#        if isVertical:
#            chart.setAxisX(axisStud, seriesBar)
#            chart.setAxisY(axisValue, seriesBar)
#        else:
#            chart.setAxisX(axisValue, seriesBar)
#            chart.setAxisY(axisStud, seriesBar)
#            
#        for marker in chart.legend().markers():       #QLegendMarker类型列表
#            marker.clicked.connect(self.do_LegendMarkerClicked)

##==================page 3.百分比柱状图 ================
    def __iniPercentBar(self):    ##初始化百分比柱状图
        chart = QChart()
        chart.setTitle( "Percent 演示")
        self.ui.chartViewPercentBar.setChart(chart)        #为ChartView设置chart
        self.ui.chartViewPercentBar.setRenderHint(QPainter.Antialiasing)       #打开 QPainter 的反走样功能（在计算机中绘制一条直线，会有明显的锯齿现象，这就叫走样）
        self.ui.chartViewPercentBar.setCursor(Qt.CrossCursor)      #设置鼠标指针为十字星
        
    @pyqtSlot()     ##绘制柱状图
    def on_btnPercentBar_clicked(self):
        self.draw_percentBar()
    
    @pyqtSlot()     ##绘制水平柱状图
    def on_btnPercentBarH_clicked(self):
        self.draw_percentBar(False)

    def draw_percentBar(self,isVertical=True):
        chart = self.ui.chartViewPercentBar.chart()
        chart.removeAllSeries()     #删除所有序列
        chart.removeAxis(chart.axisX())      #删除坐标轴
        chart.removeAxis(chart.axisY())     #删除坐标轴
        chart.legend().setAlignment(Qt.AlignRight)
        
        if isVertical:
            chart.setTitle("PercentBar 演示")
        else:
            chart.setTitle("Horizontal PercentBar 演示")
        
        scoreBarSets = []   #QBarSet对象列表
        sectionCount = 5    #5个分数段，分数段是数据集

        for i in range(sectionCount):     #从数据模型获取数据
            item = self.ui.treeWidget.topLevelItem(i)
            barSet = QBarSet(item.text(0))
            scoreBarSets.append(barSet)

        catagories = ["未解决", "已解决"]
        courseCount = 2

        for i in range(sectionCount):   #5个分数段
            item = self.ui.treeWidget.topLevelItem(i)
            barSet = scoreBarSets[i]
            for j in range(courseCount):
                barSet.append(float(item.text(j + 1)))
        
        #创建一个序列
        if isVertical:
            seriesBar = QPercentBarSeries()       #柱状图
        else:
            seriesBar = QHorizontalPercentBarSeries()  #水平柱状图
            
        seriesBar.append(scoreBarSets)      #添加数据集
        seriesBar.setLabelsVisible(True)    #显示百分比

        seriesBar.hovered.connect(self.do_barSeries_Hovered)    #hovered信号
        seriesBar.clicked.connect(self.do_barSeries_Clicked)    #clicked信号
        
        chart.addSeries(seriesBar)      #添加柱状图序列
        
        ##学生姓名坐标轴
        axisSection = QBarCategoryAxis()
        axisSection.append(catagories)
        axisSection.setTitleText("优先级")
        axisSection.setRange(catagories[0], catagories[courseCount - 1])    #坐标轴范围
        
        #数值型坐标轴
        axisValue = QValueAxis()
        axisValue.setRange(0, 100)
        axisValue.setTitleText("累积百分比")
        axisValue.setTickCount(6)       #刻度线数量
        axisValue.setLabelFormat("%.0f")
        axisValue.applyNiceNumbers()        #让刻度线更好看
        
        if isVertical:
            chart.setAxisX(axisSection, seriesBar)
            chart.setAxisY(axisValue, seriesBar)
        else:
            chart.setAxisX(axisValue, seriesBar)
            chart.setAxisY(axisSection, seriesBar)
            
        for marker in chart.legend().markers():       #QLegendMarker类型列表
            marker.clicked.connect(self.do_LegendMarkerClicked)

##==================page 4.饼图 ==================
    def __iniPieBar(self):    ##初始化百分比柱状图
        chart = QChart()
        chart.setTitle( "Pie 演示")
        chart.setAnimationOptions(QChart.SeriesAnimations)
        self.ui.chartViewPie.setChart(chart)        #为ChartView设置chart
        self.ui.chartViewPie.setRenderHint(QPainter.Antialiasing)       #打开 QPainter 的反走样功能（在计算机中绘制一条直线，会有明显的锯齿现象，这就叫走样）
        self.ui.chartViewPie.setCursor(Qt.CrossCursor)      #设置鼠标指针为十字星

    @pyqtSlot(int)
    def on_comboCourse_currentIndexChanged(self,index):
        self.draw_PieChart()

    @pyqtSlot()
    def on_btnDrawPieChart_clicked(self): 
        self.draw_PieChart()

    @pyqtSlot(float)
    def on_spinHoleSize_valueChanged(self,arg1):
        seriesPie = self.ui.chartViewPie.chart().series()[0]
        seriesPie.setHoleSize(arg1)

    @pyqtSlot(float)
    def on_spinPieSize_valueChanged(self,arg1):
        seriesPie = self.ui.chartViewPie.chart().series()[0]
        seriesPie.setPieSize(arg1)

    @pyqtSlot(bool)
    def on_chkBoxPieLegend_clicked(self,checked):
        self.ui.chartViewPie.chart().legend().setVisible(checked)

    def do_pieHovered(self,pieSlice,state):     ##鼠标在饼图上移入移出
        pieSlice.setExploded(state)
        if state:
            self.__oldLabel = pieSlice.label()   #保存原来的label
            pieSlice.setLabel(self.__oldLabel + "%.1f%%"
                    %(pieSlice.percentage() * 100))
        else:
            pieSlice.setLabel(self.__oldLabel)

    def draw_PieChart(self):    #绘制饼图
        chart = self.ui.chartViewPie.chart()
        chart.legend().setAlignment(Qt.AlignRight)
        chart.removeAllSeries()

        colNo = 1 + self.ui.comboCourse.currentIndex()

        seriesPie = QPieSeries()
        seriesPie.setHoleSize(self.ui.spinHoleSize.value())
        sec_count = 5
        seriesPie.setLabelsVisible(True)
        for i in range(sec_count):
            item = self.ui.treeWidget.topLevelItem(i)
            sliceLabel = item.text(0) + "（%s个）" %item.text(colNo)
            sliceValue = int(item.text(colNo))
            seriesPie.append(sliceLabel, sliceValue)

        seriesPie.setLabelsVisible(True)
        seriesPie.hovered.connect(self.do_pieHovered)
        chart.addSeries(seriesPie)
        chart.setTitle("Pievhart---" + self.ui.comboCourse.currentText())

##==================工具栏按钮==================
    @pyqtSlot()     ##重新生成数据
    def on_toolBtn_GenData_clicked(self):
        
        self.__generateData()
        self.__surveyData()
        
    @pyqtSlot()     ##重新统计
    def on_toolBtn_Counting_clicked(self):
        self.__surveyData()
        
    @pyqtSlot(int)     ##设置图表主题
    def on_comboTheme_currentIndexChanged(self, index):
        chart = self.__getCurrentChart()
        chart.setTheme(QChart.ChartTheme(index))
    
    @pyqtSlot(int)     ##设置动画下拉框
    def on_comboAnimation_currentIndexChanged(self, index):
        chart = self.__getCurrentChart()
        chart.setAnimationOptions(QChart.AnimationOption(index))
        
    def __getCurrentChart(self):
        page = self.ui.tabWidget.currentIndex()
        if page == 0:
            chart = self.ui.chartViewPercentBar.chart()
        else:
            chart = self.ui.chartViewPie.chart()
        return chart

## =================窗体测试程序===================
if __name__== "main_":      #用于当前窗体测试
    app = QApplication(sys.argv)    #创建GUI应用程序
    form=QmyMainWindow()    #创建窗体
    form.show()
    sys.exit(app.exec_())
