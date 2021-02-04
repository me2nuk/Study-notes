import threading
print(threading.__file__)
from threading import Timer
import time
Loop = 1

def _TimerTesT(string, args):

    global Loop
    date = time.strftime("%H:%M:%S")
    print(f'{string}[{date}] : {Loop} / {args}')
    Loop += 1

    T1 = Timer(5, function=_TimerTesT, args=(string, args))
    T1.start()

_TimerTesT('hello Timer!', 'args')