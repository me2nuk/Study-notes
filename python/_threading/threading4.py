from threading import Thread

def _ThreadTesT(kwargs, kwargs2):
    print(f'kwargs : {kwargs}')
    print(f'kwargs2 : {kwargs2}')

_kwargs = {
    'kwargs':'kwargs_dict',
    'kwargs2':'kwargs2_dict'
}

T1 = Thread(target=_ThreadTesT, kwargs=_kwargs)
T1.start()