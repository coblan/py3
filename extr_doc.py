#!python3
from __future__ import unicode_literals

import os
import re

import logging
logger = logging.getLogger(__name__)

config={
    'entry':'',
    'out':'',
    'ext':['txt'],
    'exclude':[''] 
}

def parse(config):
    """
    
    @entry:dir root that src file inside it
    @out:dir root that doc file should go to
    @ext: aware extension that file will be process
    @exclude : path to exclude
    
    .. Note:: 注意，程序不会扫描out和exclude中的文件夹
    """
    entry=config.get('entry')
    #encode=config.get('encode','utf-8')
    out= os.path.normpath(config.get('out'))
    exclude=[os.path.normpath(path) for path in config.get('exclude',[])]
    context={}
    for root,dirs,files in os.walk(entry):
        for d in list(dirs):
            next_level=os.path.normpath(os.path.join(root,d))
            if next_level==out or next_level in exclude:
                dirs.remove(d)
 
        for f in files:
            mt = re.search('\.(\w+)$',f)
            if not config.get('ext') or \
               ( mt and mt.group(1) in config.get('ext')):
                for order,file_name,v in extrac_doc(os.path.join(root,f)):
                    path_key=os.path.join(out,file_name)
                    context[path_key] = context.get(path_key,[])
                    context[path_key].append((order,v))                    
          
    doc_write(context)


   
def extrac_doc(file_path):
    with open(file_path,encoding='utf-8') as f:
        logger.debug(file_path)
        find=False
        for mt in re.finditer('^\s*>([-\d])+>([\w/\.]+)>(.+?)^\s*<-<',f.read(),re.M|re.S ):
            order=mt.group(1)
            if order=='-':
                order=0
            order=int(order)
            yield (order,mt.group(2), mt.group(3))
            find=True
        if find:
            logger.info('[get doc] %s'%file_path)
        

def doc_write(context):
    for path,value in context.items():
        ls=sorted(value,key=lambda x: x[0])
        v=[x[1] for x in ls]
        try:
            par = os.path.dirname(path)
            os.makedirs(par)
        except OSError:
            pass
        
        with open(path,'w',encoding='utf-8') as f:
            f.write(''.join(v))
    


if __name__=='__main__':
    #extrac_doc('d:/try/doc/test1.txt')
    #config={
        #'entry':'d:/try/doc',
        #'out':'d:/try/doc/gen',
        #'ext':['txt']
    #}
    logging.basicConfig(level=logging.INFO)
    
    config={
     'entry':'d:/coblan/webcode',
     'out':'d:/coblan/webcode/doc/source',
     'ext':['html','js'],
     'exclude':['d:/coblan/webcode/node_modules']
    }  
    
    parse(config)