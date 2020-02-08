from message.api import MessageService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'leiipadforpdf@163.com'
authCode = 'authcodelei18'

# thrift自动生成的MessageService接口,我们自己手动实现
class MessageServiceHandler:
    def sendSMS(self, phone, message):
        print("send SMS, phone:"+phone+", message: "+message)
        return True

    def sendEmail(self, email, message):
        # 创建邮件信息对象，用SMTP服务器对象发送邮件信息对象
        print("send email, email:"+email+", message:"+message)
        messageObj = MIMEText(message, "plain", "utf-8")
        messageObj['From'] = sender
        messageObj['To'] = email
        messageObj['Header'] = Header('夏雷服务器端发送的邮件', 'utf-8')
        try:
            smtpObj = smtplib.SMTP('smtp.163.com')
            smtpObj.auth_login(sender, authCode)
            smtpObj.sendmail(sender, [email], messageObj.as_string())
            print('send email success')
            return True
        except smtplib.SMTPException as ex:
            print('send email failed')
            print(ex)
            return False


# 对接 thrift 和 自己写好的类
if __name__ == "__main__":
    handler = MessageServiceHandler()
    processor = MessageService.Processor(handler) # 接口类创建出来的对象,和java类似
    transport = TSocket.TServerSocket("localhost", "9090")
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("python thrift server start")
    server.serve()
    print("python thrift server exit")