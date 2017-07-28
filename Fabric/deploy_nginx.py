# -*- encoding:utf-8 -*-
#加载Fabric API模块
from fabric.api import *

web_servers = ["ops@web-1","ops@web-2"]
db_servers = ["ops@db-1","ops@db-2"]

LOCAL_PATH = '/home/ops/data'
REMOTE_PATH = '/var/www/html'

#定义角色
env.roledefs = {
    "web" : web_servers,
    "db" : db_servers,
}

#安装nginx，并重启服务
@parallel
def install_nginx():
    sudo("apt-get -y update")
    sudo("apt-get -y install nginx")
    sudo("service nginx restart")

#打包本地网站源码
@parallel
def pack():
    with lcd(LOCAL_PATH):
        local("tar zcvf website.tar.gz .")   

#上传到远程服务器
@parallel
def put_task():
    with cd(REMOTE_PATH):
        result = put(LOCAL_PATH + "/website.tar.gz","/tmp")
        sudo("tar zxvf /tmp/website.tar.gz")
        sudo("rm -f /tmp/website.tar.gz")
        local("rm -f website.tar.gz")
    if result.failed and not confirm("上传文件失败，是否继续[y/n]?"):
        abort('忽略，继续进行。') 

@roles('web')
@parallel
def go():
    install_nginx()
    pack()
    put_task()



