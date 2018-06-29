def get_factor(cor1,loc1,cor2,loc2):
    corx1,cory1=cor1
    locx1,locy1=loc1
    corx2,cory2=cor2
    locx2,locy2=loc2
    a=(locx1-locx2)/(corx1-corx2)
    c=locx1-a*corx1
    
    b=(locy1-locy2)/(cory1-cory2)
    d=locy1-b* cory1
    return a,b,c,d

def get_loc(corx,cory):
    lon = a* corx +c
    lat = b * cory +d
    lon,lat=un_mercator(lon,lat)
    return lon,lat
from num_zhaoxiang import mercator,un_mercator
#######################
x1,y1 = -31611.9212399590 ,4085.6624696340
mx1,my1= 121.140153,31.270066
mx1,my1=mercator(mx1,my1)

x2,y2=-26217.9018395287,449.235189262312
mx2,my2= 121.196344,31.237263
mx2,my2=mercator(mx2,my2)
############################
a,b,c,d=get_factor((x1,y1),(mx1,my1),(x2,y2),(mx2,my2))

print(get_loc(x1,y1))