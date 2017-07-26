from fabric.api import *
from fabric.tasks import execute
from fabric.context_managers import hide

web_servers = ["ops@web-1","ops@web-2"]
db_servers = ["ops@db-1","ops@db-2"]

env.roledefs = {
    "web" : web_servers,
    "db" : db_servers,
}

@roles("web")
@task
def get_ip():
    shell_command = ''' ifconfig |grep 'inet addr'|awk -F ":" '{print $2}'|awk '{print $1}' '''
    return run(shell_command)

@roles("db")
@task
def get_disk():
    return run("df -h /")

@task
def go():
    with hide('running', 'stdout', 'stderr'):
        result_web =  execute(get_ip)
        result_db = execute(get_disk)
        return result_web,result_db
    
if __name__ == '__main__':
    print go()
