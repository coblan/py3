from PIL import Image
import os
import io

min_size = 200

import sqlite3
conn = sqlite3.connect(r'D:\work\files\team_icon_optimize\info.db')
c = conn.cursor()

# Create table
#c.execute('''CREATE TABLE info
             #(name text, img_size text,img_size_after text, file_size text, file_size_after text,final_ext text)''')


def run(): 
    parDir = r'D:\work\files\team_icon'
    dc = {}
    
    for flName in os.listdir(parDir):
        if is_proccessed(flName):
            continue
        flPath = os.path.join(parDir, flName)
        
        flSize = os.path.getsize(flPath)
        
        try:
            img = Image.open(flPath)
            imgSize = ','.join([str(x) for x in img.size])
            jpg = try_jpg(img)
            png = try_png(img)
            flContent, ext = (jpg, 'jpg') if len(jpg) < len(png) else (png, 'png')
            
            if len(flContent) > 15 * 1024:
                if min(img.size) > min_size:
                    ratio =  float(min_size) / min(img.size)
                    img.resize(tuple([int(x * ratio) for x in img.size]), Image.ANTIALIAS)
                    jpg = try_jpg(img)
                    png = try_png(img)                    
                    flContent = jpg if len(jpg) < len(png) else png
            if len(flContent) < flSize:
                
                writeFile(flContent, flName)
                c.execute('INSERT INTO info VALUES (?,?,?,?,?,?)', (flName, imgSize, ','.join([str(x) for x in img.size]), flSize, len(flContent), ext))
                conn.commit()
                print(flName)
        except OSError:
            pass

def try_jpg(img): 
    catch = io.BytesIO()
    img.save(catch, format = 'JPEG', optimize = True, progressive=True)
    return catch.getvalue()

def try_png(img): 
    catch = io.BytesIO()
    img.save(catch, format = 'PNG', optimize = True )
    return catch.getvalue()

def writeFile(flContent, flName): 
    with open(os.path.join(r'D:\work\files\team_icon_optimize', flName), 'wb') as f:
        f.write(flContent)


def is_proccessed(name): 
    #c2 = conn.cursor()
    c.execute('SELECT name FROM info WHERE name = "%s"' % name)
    if c.fetchone():
        return True
    else:
        return False

run()

#def lower_res(flPath): 
    #img = Image.open(flPath)
    #img.
