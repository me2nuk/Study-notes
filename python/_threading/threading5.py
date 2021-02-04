from threading import Thread

def loopfor(string, loop):
    print(f'{string} loop : {loop}')

for i in range(1,5):
    variable = Thread(target=loopfor, args = (i, i))
    variable.start()