# 代码管理平台

**Author**: Casey Lee :kiwi_fruit:

---

## 功能

### 1. 打开数据库失败会有提示

![](pics\1.png)

### 2. 正确显示表内数据，能筛选部分数据

![](pics\2.png)

![](pics\3.png)

### 3. 添加功能

![](pics\4.png)

![](pics\5.png)

可以看到，此时已经是submit后已存在于数据库的数据了，星号已经消失了。

![](pics\6.png)

### 4. 删除功能

![](pics\7.png)

![](pics\8.png)

### 5. 更新功能

#### 第一种更新方式

![](pics\9.png)

![](pics\10.png)

![](pics\11.png)

![](pics\12.png)

#### 第二种更新方式

直接改

![](pics\13.png)

点击保存

![](pics\14.png)

### 6. 保存功能

之前已经展示完毕

### 7. 取消功能

![](pics\15.png)

![](pics\16.png)

### 8. 批量修改功能

![](pics\17.png)

![](pics\18.png)

### 9. 退出功能

正常运行，无误

### 10. 工具栏，菜单栏都很齐全

![](pics\19.png)

### 11. 状态栏一切正常

![](pics\20.png)

### 12. 资源文件

能正常显示图标

![](pics\21.png)

### 13. 可视化功能

![](pics\22.png)

![](pics\23.png)

### 14. 布局功能

![](pics\1.gif)



## 前端

由于不同的功能有不同的适用，换了2次数据模型，最后选择了 QSqlQueryModel 作为数据模型； QItemSelectionModel 作为选择模型。为了加剩下的取消，保存和数据筛选的功能，我只能换一个模型，所有的功能都得重写。好在的是， issues 表的画图是和 PR 表分开的，因此 issues 表以及画图部分不需要动它。我使用了 css 样式进行美化， css 是在github找的：

https://github.com/chenwen1126/Qss

### qss 的使用总结

> 第一个set是把css文件放进一个对象
>
> 1. 不需要qt的c++文件，咱们这里是直接 python 拿到的 css
>
> 2. 读取到 css 的内容，主动 set 进 app 里面，样式自动就变了，不需要再 import
>   就是说，只需要在 appMain import 这个工具类，只需要这个媒介就可以拿到
>   工具类已有的 css 了。
>
>   ---
>
>   它的 **本质** 是这样的：
>
>   - 读取 css
>   - 把 css set 到 app 里
>   - 工具类不是必须的，工具类只是把这两步封装起来。其实完全可以在 appMain.py 中读取 css 和 set css