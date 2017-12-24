from mlab import *
from models.river import *

mlab_connect()

e2_rivers = River.objects(continent = 'Africa')

for river in e2_rivers:
    print(river)

print("*" *10)
e3_rivers = River.objects(continent = 'S. America', length__lt = 1000)


for river in e3_rivers:
    print(river)
