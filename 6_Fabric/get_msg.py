# -*- encoding:utf-8 -*-
#加载Fabric API模块
from fabric.api import *
#加载execute方法，用于获取task返回值。
from fabric.tasks import execute
#加载hide方法，用于隐藏Fabric各级别输出信息。
from fabric.context_managers import hide

web_servers = ["ops@web-1","ops@web-2"]
db_servers = ["ops@db-1","ops@db-2"]

#定义角色
env.roledefs = {
    "web" : web_servers,
    "db" : db_servers,
}

@roles("web")
@task
@parallel
def get_ip():
    shell_command = ''' ifconfig ens33 |grep 'inet addr'|awk -F ":" '{print $2}'|awk '{print $1}' '''
    return run(shell_command)

@roles("db")
@task
@parallel
def get_disk():
    shell_command = ''' df -h / | awk '{print $4}' | grep '^[0-9].*' '''
    return run(shell_command)

@runs_once
@task
def go():
    #隐藏Fabric输出信息。
    with hide('running', 'stdout', 'stderr'):
        result_web =  execute(get_ip)
        result_db = execute(get_disk)
        return result_web,result_db
    
if __name__ == '__main__':
    print go() 
