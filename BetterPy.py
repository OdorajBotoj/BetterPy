# -*-coding:utf-8 -*-
from time import time
__version__ = '1.0.0.20201229'
__another__ = 'OdorajBotoj'
def betterpyInfo():
    print('BetterPy:',__version__,'By:',__another__)
def _BK(t=''):
    input(t)
def _DEBUG(*x):
    for i in x:
        print(i,type(i))
    _BK('按下回车以继续...')
def _QUIT(t='按下回车键以退出...'):
    _BK(t)
    exit()
def _PLUS(a,b):
    a=float(a)
    b=float(b)
    if len(str(a).split('.')[-1]) >+ len(str(b).split('.')[-1]):
        lenth = len(str(a).split('.')[-1])
    else:
        lenth = len(str(b).split('.')[-1])
    a=int(a*(10**lenth))
    b=int(b*(10**lenth))
    out=float((a+b)/(10**lenth))
    return out
def _RUN_CLOCK(command='10**10'):
    start = time()
    try:
        out=eval(command)
    except:
        return 1
    return out,time()-start
def _CASE(i,d):
    d=dict(d)
    if i in d.keys():
        for a in d.keys():
            if i==a:
                out = eval(d[a])
                break
            else:pass
    else:raise KeyError('ERROR:{} is not in {}'.format(i,d))
    return out
