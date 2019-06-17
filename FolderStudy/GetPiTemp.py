import os,time
import smbus
from matplotlib import pyplot as plt 

def GetCPUTemp():
    result=os.popen('vcgencmd measure_temp').readline()
    result=result.replace("temp=","").replace("'C\n","")
    return float(result)


x=range(1,101)
y=[]
for i in x:
    print(GetCPUTemp())
    y.append(GetCPUTemp())
    time.sleep(1)
plt.plot(x,y) 
plt.show()
