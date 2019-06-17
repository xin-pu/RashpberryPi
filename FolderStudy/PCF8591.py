import smbus   
from matplotlib import pyplot as plt 
import time
 
address = 0x48 
A0 = 0x40   
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1) 

test=A0
i=0
x = range(1,51) 
y=[]
for i in x: 
    bus.write_byte(address,test)  
    value = bus.read_byte(address) 
    print("{0} Res:{1}".format(i,value)) 
    y.append(value)
    time.sleep(0.2) 
    i+=1
    i+=1

plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y) 
plt.show()
