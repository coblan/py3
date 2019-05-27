from fabric import Connection
c = Connection('root@192.168.40.145')
with c.cd('/home/pypro/Backendplus'):
    c.run('git pull')
    c.run('git submodule update')
    c.run('touch run/Backendplus.reload')

