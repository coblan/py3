# encoding:utf-8
import numpy as np
import geo
import math
def millerXY(lon, lat):
    L = 6381372 * math.pi * 2
    W = L
    H = L / 2
    mill =1 # 2.3
    x = lon * math.pi / 180
    y = lat * math.pi / 180
    y = 1.25 * math.log(math.tan( 0.25 * math.pi + 0.4 * y ))
    x = ( W / 2 ) + ( W / (2 * math.pi) ) * x
    y = ( H / 2 ) - ( H / ( 2 * mill ) ) * y
    return (x,y)


def XYmiller(x,y):
    L = 6381372 * math.pi * 2
    W = L
    H = L / 2
    mill = 1# 2.3    
    lon=360/W * (x-W/2)
    lat=180/(0.4*math.pi)*(math.atan( math.exp( (H-2*y)*mill/(1.25*H) ) ) -0.25*math.pi)
    return lon,lat


def mercator(lon,lat):
    x=lon*20037508.34/180
    y=math.log(math.tan((90+lat)*math.pi/360))/(math.pi/180)
    y=y*20037508.34/180
    return x,y

def un_mercator(x,y):
    x1=x/20037508.34*180
    y1=y/20037508.34*180
    lat=180/math.pi*(2*math.atan(math.exp(y1*math.pi/180))-math.pi/2)
    return x1,lat

def get_loc(x,y):
    o_x=a*x+b*y+c
    o_y=b*x-a*y+d
    lon=o_x
    lat=o_y
    #lon,lat = XYmiller(o_x,o_y)
    lon,lat = un_mercator(o_x,o_y)
    #return geo.wgs84_to_gcj02( lon,lat )
    return lon,lat

## 121.111432,31.152124  -34360,-8977
## 121.315323,31.175311  -14940,6437
## 121.160877,31.164138  -29640,7648
## 121.156393,31.140912  -30090,10240

#121.153663,31.174931 -30330,6443
#121.051354,31.109524 -40090,13670

##121.473052,31.233868  116.40,-39.92
##121.00467,30.963377 -44590,29830

#############################
# 输入对应的坐标点
#监督员的坐标映射
x1,y1=-30330,6443
mx1,my1= 121.153663,31.174931

x2,y2= -40090,13670
mx2,my2= 121.051354,31.109524


#
x1,y1 = -31611.9212399590 ,4085.6624696340
mx1,my1= 121.140153,31.270066

x2,y2=-26217.9018395287,449.235189262312
mx2,my2= 121.196344,31.237263


x1,y1 = -26185.1604368266,-9319.806212714190
mx1,my1= 121.222438264371, 31.138758177758017

x2,y2=-25906.79,-9276.14
mx2,my2= 121.22322646804434, 31.13917871824248



###########################################
#mx1,my1= geo.gcj02_to_wgs84(121.473052,31.233868)
#mx1,my1=millerXY(mx1,my1)
mx1,my1=mercator(mx1,my1)

#mx2,my2=geo.gcj02_to_wgs84(121.00467,30.963377)
#mx2,my2=millerXY(mx2,my2)
mx2,my2=mercator(mx2,my2)

maped=np.mat([mx1,my1,mx2,my2])
m=np.mat([[x1,y1,1,0],
          [-y1,x1,0,1],
            [x2,y2,1,0],
            [-y2,x2,0,1]])


A = m.I * maped.T

a,b,c,d = np.array(A.T)[0]


print(get_loc(-6538,-19020))