##### Python实现自动填写、提交表单&发送邮件通知

###### 1 配置操作

1）按照脚本文件中的标准序号修改个人信息（共5处）；
>如 self.myusername="1)发送邮箱"
>
>将个人邮箱添加到1）处，即可；

2）如果需要打包成exe程序，打开cmd窗口，使用如下命令：
>pyinstaller -F main.py --noconsole

3）如果是windows系统，需要执行自动化执行脚本程序，建议搜索windows的计划任务；

*****
###### 2 注意
1）执行该脚本，可能需要ChromeDriver程序的支持；
2）库：selenium、smtplib

>如果存在问题或技术交流，欢迎留言&邮件联系（ligang_chn@163.com）！


