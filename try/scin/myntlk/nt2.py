import nltk

sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)



key_ls=[]

def compress_path(path, width):
    print "compress_path-------------------------------------"
    if not os.path.isdir(path):
        print "这不是一个文件夹，请输入文件夹的正确路径!"
        return
    else:
        fromFilePath = path 			# 源路径
        #toFilePath = path+"/tiny" 		# 输出路径
        toFilePath = path+"/tiny" 		# 输出路径与源路径相同则替换原始图片，反正有Git版本控制
        print "fromFilePath=%s" %fromFilePath
        print "toFilePath=%s" %toFilePath

        for root, dirs, files in os.walk(fromFilePath):
            print "root = %s" %root
            print "dirs = %s" %dirs
            print "files= %s" %files
            for name in files:
                fileName, fileSuffix = os.path.splitext(name)
                if fileSuffix == '.png' or fileSuffix == '.jpg' or fileSuffix == '.jpeg':
                    toFullPath = toFilePath + root[len(fromFilePath):]
                    toFullName = toFullPath + '/' + name
                    if os.path.isdir(toFullPath):
                        pass
                    else:
                        os.mkdir(toFullPath)
                    try:
                        compress_core(root + '/' + name, toFullName, width)
                    except:
                        tinify.key = key_ls.pop()		# API KEY
                        
# 			break	