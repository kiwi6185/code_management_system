# 封装修改样式工具
# 定义一个专门用来操作qss样式的类
class QSSTool():
 # 静态方法
 @staticmethod
 def setQssToObj(file_path,obj):
     with open(file_path, 'r',  encoding='utf-8') as f: # 以只读，utf8 的方式打开 css 文件
         content = f.read()
         obj.setStyleSheet(content) # 其实是这里，set app 的样式
