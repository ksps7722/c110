from subprocess import TimeoutExpired
import time
def timer(seconds):
   while seconds>0:
       min=int(seconds/60)
       sec=int(seconds%60)
       timer=f'{min}:{sec}'
       print(timer,end='\r')
       time.sleep(1)
       seconds-=1
    
seconds=input("Enter Seconds")
timer(int(seconds))

