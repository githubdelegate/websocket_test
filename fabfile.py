from fabric.api import *
from fabric.operations import sudo

env.hosts = ['45.114.127.141']            # 指定 hosts 远程主机
# env.key_filename = '/path/to/id_rsa'     # 指定你的私钥文件
env.user = 'root'
env.password = '515298403849'

def deploy():
    project_folder = '/root/websocket_test'
    with cd(project_folder):
        run('pwd')
        run('git pull')
        # run('pipenv shell')
        # run('.venv/bin/gunicorn stop')
        # run('.venv/bin/gunicorn --reload -b 127.0.0.1:8000 manager:app')



