import numpy as np
import geo
# 121.111432,31.152124  -34360,-8977
# 121.403407,31.061876  -19020,-6538


# 121.278763,31.173616  -18380,-6614
# 121.315323,31.175311  -14940,6437

x1,y1=-34360,8977
# x2,y2=-18380,6614
x2,y2=-14940,6437

mx1,my1=geo.gcj02_to_wgs84(121.111432,31.152124)
mx2,my2=geo.gcj02_to_wgs84(121.315323,31.175311)

maped=np.mat([mx1,my1,mx2,my2])
m=np.mat([[x1,y1,1,0],
            [-y1,x1,0,1],
            [x2,y2,1,0],
            [-y2,x2,0,1]])


A = m.I * maped.T

a,b,c,d = np.array(A.T)[0]

def get_loc(x,y):
    o_x=a*x+b*y+c
    o_y=b*x-a*y+d
    
    return geo.wgs84_to_gcj02( o_x,o_y )

print(get_loc(-6538,-19020))