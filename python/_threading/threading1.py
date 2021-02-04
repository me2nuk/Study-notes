from threading import Thread

def _ThreadTesT():
    print('ThreadTest Function Message : HelloWorld!')

T1 = Thread(target = _ThreadTesT)
T1.start()