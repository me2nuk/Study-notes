from threading import Thread

def _ThreadTesT(args, args2):
    print(f'args : {args}')
    print(f'args2 : {args2}')

T1 = Thread(target=_ThreadTesT, args=(1,2))
T1.start()