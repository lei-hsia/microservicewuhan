from message.api import MessageService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# thrift自动生成的MessageService接口,我们自己手动实现
class MessageServiceHandler:
    def sendSMS(self, phone, message):
        print("send SMS ")
        return True

    def sendEmail(self, email, message):
        print("send email")
        return True

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