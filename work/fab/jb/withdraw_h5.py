from fabric import Connection
from invoke import run

c = Connection('root@192.168.40.198',port=22, connect_kwargs={'password':'cdqg@1215'})

def commit():
    #c.local(r'd: && cd D:\work\withdraw\H5 && git -v')
    #run(r'd: && cd D:\work\withdraw\H5 && git -v')
    with c.prefix(r'd: && cd D:\work\withdraw\H5'):
        run('git add .')
        run('git commit -m auto_commit')
        run('git push')
        #c.local('git add .')
        #c.local('git commit -m auto_commit')
        #c.local('git push')

def deploy():
    with c.cd('/home/pypro/H5'):
        c.run('git remote set-url origin http://hyl:he123456@192.168.40.229:18082/DDD/H5.git')
        c.run('git pull')
        c.run('git remote set-url origin http://192.168.40.229:18082/DDD/H5.git')
    
    #c.run('git pull')

if __name__ =='__main__':
    commit()
    #deploy()
    