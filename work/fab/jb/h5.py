from fabric import Connection
c = Connection('root@192.168.40.145')
with c.cd('/home/pypro/H5'):
    c.run('git pull')

