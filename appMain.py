## GUI应用程序主程序入口
import sys

from PyQt5.QtWidgets import QApplication
from myMainWindow import QmyMainWindow
from tool import QSSTool  # 这里只是为了使用工具类

app = QApplication(sys.argv)    #创建GUI应用程序
# 我把工具类那堆代码搬到这里来效果也是一样的，乱而已 ，所以封装了一下
QSSTool.setQssToObj('qss.css',app) # 这里只是把路径和app 传进去
mainform = QmyMainWindow()      #创建主窗体
mainform.show()         #显示主窗体

sys.exit(app.exec_())
