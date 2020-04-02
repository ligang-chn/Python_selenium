#### Python实现自动填写、提交表单&发送邮件通知

##### 1 功能

- 自动填充并提交网页表单；
- 填写结果通过邮件通知用户；
- Windows定时运行计划任务。

##### 2 环境安装

1）Google浏览器

脚本中使用的是google浏览器，版本80；

2）安装Chrome WebDriver驱动程序

Windows下配置Chrome WebDriver:
>参考这篇博客
>https://blog.csdn.net/u013360850/article/details/54962248

3）下载脚本源码，按照脚本文件中标注的序号修改个人信息（共5处）；
>示例：
>
>self.myusername="1)发送邮箱"
>
>将个人邮箱添加到1）处，即可；

2）如果需要打包成exe程序，打开cmd窗口，使用如下命令：
>pyinstaller -F main.py --noconsole
>
>前提是已经安装了`pyinstaller`库；

3）如果是windows系统，需要执行自动化执行脚本程序，建议搜索windows的计划任务；

具体操作这里既不介绍了。

*****
###### 3 注意
1）执行该脚本，可能需要ChromeDriver程序的支持；如果是其他浏览器，如IE浏览器，需要相应的IEDriver程序的支持。

2）涉及库：`selenium`、`smtplib`、`pyinstaller`




