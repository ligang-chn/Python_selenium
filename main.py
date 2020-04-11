from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By#简写用包
from selenium.webdriver.support.ui import WebDriverWait#等待用包
from selenium.webdriver.support import expected_conditions as EC#场景判断
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText


class Handle_Send_Email(object):
    def __init__(self):
        self.client=smtplib.SMTP_SSL("smtp.qq.com",465)
        # self.client.connect("smtp.qq.com",465)
        # #开启SSL
        # self.client.starttls()
        #登录邮箱
        self.myusername="1）邮箱"
        self.mypassword="2）密码（授权码）"##"olsolhakmrweebfd"
        self.client.login(user=self.myusername,password=self.mypassword)

    def send_email(self,contentStr,address="3）邮箱"):
        msg=MIMEMultipart()
        #邮件的主题
        msg['Subject']=Header("每日一报",'utf-8')
        #定义发送者
        msg['From']=Header(self.myusername)
        #定义邮件的内容
        content=MIMEText(contentStr,'plain','utf-8')
        msg.attach(content)
        self.client.sendmail(self.myusername,address,msg.as_string())
        self.client.close()


class Handle_webdriver(object):
    def __init__(self):
        self.driver=webdriver.Chrome()#谷歌浏览器
        self.driver.maximize_window()
        self.myemail = Handle_Send_Email()


    def handle_login(self):
        # 登录网站
        self.driver.get("https://newsso.shu.edu.cn/login")
        if WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located((By.ID,"username"))):
            self.driver.find_element_by_id("username").send_keys("4）账号")#填充账号和密码，显示等待
            if WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located((By.ID,"password"))):
                self.driver.find_element_by_id("password").send_keys("5）密码")
                self.driver.find_element_by_id("login-submit").click()

                self.checkLogin()
                # self.fillingForm()


    def checkLogin(self):
        """检查是否已经填报"""
        self.driver.get("http://selfreport.shu.edu.cn/Default.aspx")
        if WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, "报送历史"))):
            self.driver.get("http://selfreport.shu.edu.cn/ReportHistory.aspx")
            if WebDriverWait(self.driver, 5, 0.5).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "返回首页"))):
                result = self.driver.find_element_by_xpath(
                    '/html/body/form/div[5]/div/div[2]/div[1]/div/ul/li[1]/a')
                if "已填报" in result.text:
                    self.myemail.send_email("已填报")
                    time.sleep(5)
                    self.driver.quit()
                else:
                    # print("未填报，即将执行填报...")
                    time.sleep(2)
                    # print("开始填报*****")
                    self.driver.find_element_by_link_text("返回首页").click()
                    self.fillingForm()#开始填报


    def fillingForm(self):
        """进行填报"""
        # self.driver.get("http://selfreport.shu.edu.cn/Default.aspx")
        if WebDriverWait(self.driver, 5, 0.5).until(
                EC.presence_of_element_located((By.LINK_TEXT, "每日一报"))):
            self.driver.get("http://selfreport.shu.edu.cn/DayReport.aspx")
            if WebDriverWait(self.driver, 5, 0.5).until(
                    EC.presence_of_element_located((By.ID, "p1_ChengNuo-inputEl-icon"))):
                self.driver.find_element_by_id("p1_ChengNuo-inputEl-icon").click()#我承诺
                time.sleep(1)
                self.driver.find_element_by_id("p1_TiWen-inputEl").send_keys("36")#体温
                time.sleep(1)
                self.driver.find_element_by_id("p1_ddlSheng-inputEl").click() #省份
                time.sleep(2)
                self.driver.find_element_by_xpath("/html/body/ul[2]/li[11]").click()#江苏
                time.sleep(2)
                self.driver.find_element_by_id("p1_ddlShi-inputEl").click()  # 市
                time.sleep(2)
                self.driver.find_element_by_xpath("/html/body/ul[3]/li[8]").click()  #
                time.sleep(2)
                self.driver.find_element_by_id("p1_ddlXian-inputEl").click()  # 县
                time.sleep(2)
                self.driver.find_element_by_xpath("/html/body/ul[4]/li[5]").click()  #
                time.sleep(2)
                self.driver.find_element_by_id("p1_XiangXDZ-inputEl").send_keys("6）地址")  # 地址
                time.sleep(2)

                self.driver.find_element_by_id("p1_ctl00_btnSubmit").click()
                if WebDriverWait(self.driver, 5, 0.5).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "确定"))):
                    time.sleep(2)
                    self.driver.find_element_by_link_text("确定").click()
                    if WebDriverWait(self.driver, 10, 0.5).until(
                            EC.presence_of_element_located(
                                (By.CLASS_NAME, "f-messagebox-message"))):
                        if WebDriverWait(self.driver, 5, 0.5).until(
                                EC.presence_of_element_located((By.LINK_TEXT, "确定"))):
                            time.sleep(2)
                            self.driver.find_element_by_link_text("确定").click()
                            time.sleep(2)


        self.driver.get("http://selfreport.shu.edu.cn/Default.aspx")
        if WebDriverWait(self.driver, 5, 0.5).until(
                EC.presence_of_element_located((By.LINK_TEXT, "报送历史"))):
            self.driver.get("http://selfreport.shu.edu.cn/ReportHistory.aspx")
            if WebDriverWait(self.driver, 5, 0.5).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "返回首页"))):
                result = self.driver.find_element_by_xpath(
                    '/html/body/form/div[5]/div/div[2]/div[1]/div/ul/li[1]/a')
                if "已填报" in result.text:
                    self.myemail.send_email("填报成功")
                    # print("填报成功")
                    time.sleep(5)
                    self.driver.quit()
                else:
                    self.myemail.send_email("填报失败...")
                    time.sleep(5)
                    self.driver.quit()

if __name__=='__main__':
    shu=Handle_webdriver()
    shu.handle_login()



