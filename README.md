### 整体: 
1. client
2. APIGateway
3. (REST) 用户EdgeService(单点登录), (REST) 课程EdgeService
4. (Thrift) 用户服务(j),信息服务(p) (Dubbo) 课程服务(j) 
5. 三个服务，每个都有自己的DB
6. 用户服务,用来完成用户登录,如果有session一般会把用户信息存到session,但是这个要去session,
所以最好提供集中式存储，这里用redis作为集中式缓存
7. 用户服务单点登录之后能访问课程服务
8. 课程服务访问用户服务单点登录系统(使用单点登录系统的,有一步都是需要
   携带token/ticket访问单点登录系统，检验这个token是不是正确的，
   然后拿这个token换取单点登陆系统/用户系统的信息)
9. 即, 课程edgeservice要调用 用户edgeservice (访问单点登录系统)
10. 课程服务要调用 用户服务(看课程的老师) (通过Thrift调用)
11. 总结一下就是, 有三种服务的调用:
     - edgeService之间的调用(调用单点登录系统)
     - edgeService调用微服务(通过Thrift, Dubbo)
     - 微服务之间的调用(Thrift)

### 用户服务
- 用户服务
- 用户注册
- 用户基本信息查询
- 无状态，无session
- 单点登录

向外提供一个Thrift接口,

### 课程服务
- 登录验证
- 课程的CRUD

课程服务选用Dubbo这个RPC, 用Zookeeper进行发现和注册服务; Dubbo用KV的形式作为服务发布订阅方式

课程服务也通过Thrift调用用户服务

### 信息服务
- 发送邮件
- 发送短信

### 用户 edgeservice
### 课程　edgeservice
### API GATEWAY