import smbus   
import time
 
address = 0x48 
A0 = 0x40     
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1) 

test=A0
i=0
while i<10: 
    bus.write_byte(address,test)  
    value = bus.read_byte(address) 
    print("{0} Res:{1}".format(test,value)) 
    time.sleep(1) 
    i+=1
