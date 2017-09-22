# -*- encoding:utf-8 -*-
#加载Fabric API模块
from fabric.api import *
#加载execute方法，用于获取task返回值。
from fabric.tasks import execute

web_servers = ["ops@web-1","ops@web-2"]
db_servers = ["ops@db-1","ops@db-2"]

LOCAL_PATH = '/home/ops/data'
REMOTE_PATH = '/var/www/html'

SHELL_SCRIPT = 'check.sh'

#定义角色
env.roledefs = {
    "web" : web_servers,
    "db" : db_servers,
}

@parallel
def collect():
    put(SHELL_SCRIPT, "/tmp")
    result = run('bash /tmp/' + SHELL_SCRIPT)
    run('rm -f /tmp/' + SHELL_SCRIPT)
    return result

@parallel
def go():
    msg = execute(collect,roles = ['web'])
    print msg
    with open('messages.txt','a+') as f:
        for hostname in msg:
            content = 'HOSTNAME:{0}\n{1} \n\n'.format(hostname, msg[hostname])
            f.write(content)
