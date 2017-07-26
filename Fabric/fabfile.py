#-*- encoding:utf-8 -*-
#加载fabric api接口。
from fabric.api import *                

#定义要远程执行任务的主机列表。
env.hosts = ['ops@web-1','ops@web-2']   

#定义SSH密码（已配置秘钥认证的看忽略本条）。
env.password = 'yourpassword'          

#定义一个任务用于显示uname信息。
def print_uname():                      
    #使用run()方法来执行远程命令    
    run("uname -a")                     

def print_hostname():
    run("hostname")

#定义一个msg()方法来整合任务。
def go():                              
    print_uname()
    print_hostname()
