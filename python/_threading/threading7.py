from threading import Timer

def _LoopTest():
    print('Loop')
    T1 = Timer(3,_LoopTest)