# thrift脚本, 定义namespace和service(接口)
namespace java com.imooc.thrift.message
namespace py message.api

service MessageService {
    bool sendSMS(1:string phone, 2:string message);
    bool sendEmail(1:string email, 2:string message);
}