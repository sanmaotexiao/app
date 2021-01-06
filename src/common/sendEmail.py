from config.globalparameter import project_path
import smtplib
from email.mime.text import MIMEText #构建邮件格式
from email.mime.multipart import MIMEMultipart  #带附件
from email.header import Header
from src.common.Config_Data import ConfigData


class SendEmail(object):

    conf = ConfigData()

    def __init__(self):
        self.host = self.conf.get_email("host")
        print(self.host)
        self.sender_eml = self.conf.get_email("sender_email")
        print(self.send_email)
        self.passwd = self.conf.get_email("password")
        print(self.passwd)
        self.recipient_list = self.conf.get_recipients("recipients")
        print(self.recipient_list)
        self.subject = self.conf.get_email('subject')
        print(self.subject)
        self.content = self.conf.get_email('emicontent')
        print(self.content)

    def send_email(self,reports):
        sender = self.sender_eml
        print(sender)
        message = MIMEMultipart() #带附件实例
        message.attach(MIMEText(self.content, 'plain', 'utf-8'))
        message['Subject'] = Header(self.subject,'utf-8')
        message['From'] = Header(sender,'utf-8')
        message['To'] = Header(';'.join(self.recipient_list),'utf-8') #收件人
        # 构造附件
        with open(reports, 'rb') as f:
            mail_body = f.read()
        f.close()
        att1 = MIMEText(mail_body, 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="01.html"'
        message.attach(att1)
        try:
            server = smtplib.SMTP()
            server.connect(self.host)
            server.login(sender,self.passwd)
            server.sendmail(sender,self.recipient_list,message.as_string())
        except Exception as e:
            return e
        else:
            server.quit()


# if __name__ == "__main__":
#     s = SendEmail()
#     s.send_email(project_path+r'\report\2021-01-04_10_18_27_Report.html')