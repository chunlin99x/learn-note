## 关闭/开启防火墙出现
```
service iptables start/stop  
```

会报错Failed to start iptables.service: Unit iptables.service failed to load: No such file or directory.
在CentOS 7或RHEL 7或Fedora中防火墙由firewalld来管理，
如果要添加范围例外端口 如 1000-2000语法命令如下：启用区域端口和协议组合firewall-cmd [--zone=<zone>] --add-port=<port>[-<port>]/<protocol> [--timeout=<seconds>]此举将启用端口和协议的组合。端口可以是一个单独的端口 <port> 或者是一个端口范围 <port>-<port> 。协议可以是 tcp 或 udp。实际命令如下：
firewall-cmd --permanent --add-port=1000-2000/tcp

####  执行可以成功用该命令查询
firewall-cmd --permanent --query-port=1000/tcp

#### 当然你可以还原传统的管理方式。
#### 执行一下命令：
```
systemctl stop firewalld  
systemctl mask firewalld  
```
#### 并且安装iptables-services：
```
yum install iptables-services  
```

#### 设置开机启动：
```
systemctl enable iptables  
systemctl stop iptables  
systemctl start iptables  
systemctl restart iptables  
systemctl reload iptables  
```

#### 保存设置：
```
service iptables save  
```

OK，再试一下应该就好使了
开放某个端口 在/etc/sysconfig/iptables里添加
```
-A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 8080 -j ACCEPT
```
