from threading import Thread
import time

def _ThreadTesT():
    for _ in range(5):
        print('ThreadTest Function Message : HelloWorld!')
    time.sleep(2)
    
T1 = Thread(target = _ThreadTesT)
T1.start()
T1.join()
print('T1 : hello')

T2 = Thread(target= _ThreadTesT)
T2.start()
print('T2 : hello')