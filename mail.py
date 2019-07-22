#coding=utf-8

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from datetime import datetime
import os

class MailSend:
    def __init__(self, host_server):
        self.host_server = host_server
        self.msg = MIMEMultipart('related')

    #邮件中添加文本
    def addText(self, message, text):
        msgText = (MIMEText(text, 'html', 'utf-8'))
        message.attach(msgText)

    #邮件中添加附件
    def addAttach(self, message, filename):
        print(filename)
        attach_name = os.path.basename(filename)
        att1 = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="{attach_name}"'.format(attach_name = attach_name)
        message.attach(att1)

    #邮件正文插入图片
    #PS：当前存在bug，图片会在附件中显示，且附件图片无名称
    def addImage(self, message, image):
        image_body =  '''<p><img src="cid:%s"></p>''' % image
        msgText = (MIMEText(image_body, 'html', 'utf-8'))
        message.attach(msgText)
        print("#######%s#########" % image)
        fp = open(image, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        # 定义图片 ID，在 HTML 文本中引用
        msgImage.add_header('Content-ID', '<%s>' % image)
        message.attach(msgImage)

    #添加图片附件并在正文中显示
    def addImageAttach(self, message, image):
        filename = os.path.basename(image)
        with open(image, 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase('image', 'png', filename = filename)
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename = filename)
            mime.add_header('Content-ID', '<%s>' % filename)
            mime.add_header('X-Attachment-Id', '%s' % filename)
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            message.attach(mime)
            image_body = '''<p><img src="cid:%s"></p>''' % filename
            msgText = (MIMEText(image_body, 'html', 'utf-8'))
            message.attach(msgText)

    def createEmail(self, mail_body, attachs, images):
        mail_title = 'JIRA缺陷统计'
        # 邮件正文内容

        self.msg["Subject"] = Header(mail_title, 'utf-8')
        #msg["From"] = sender_mail
        #msg["To"] = receiver
        self.addText(self.msg, mail_body)
        #插入图片
        for image in images:
            if not os.path.exists(image):
                print("文件%s不存在" % image)
                continue
            self.addImageAttach(self.msg, image)
        #插入附件
        for attach in attachs:
            if not os.path.exists(attach):
                print("文件%s不存在" % attach)
                continue
            self.addAttach(self.msg, attach)
        return self.msg

    def sendEmail(self,msg, sender_mail, pwd, receiver):
        # ssl登录
        smtp = SMTP_SSL(self.host_server)
        # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.set_debuglevel(0)
        smtp.ehlo(self.host_server)
        smtp.login(sender_mail, pwd)

        smtp.sendmail(sender_mail, receiver, msg.as_string())
        smtp.quit()
        print("邮件发送结束.")
