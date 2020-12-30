# -*-coding:utf-8 -*-
from time import time
__version__ = '1.0.1.20201230'
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
    else:raise KeyError('ERROR:{} is not in {}'.format(i,d));out='ERR'
    return out

def _HELP(name=''):
    d=dict({'betterpyInfo':'betterpyInfo()\n打印程序信息','_BK':'_BK(<提示信息>)\n设置程序中断','_DEBUG':'_DEBUG(<一个或多个变量>)\n输出变量信息并中断','_QUIT':'_QUIT(<提示信息>)\n中断并退出','_PLUS':'_PLUS(<变量a>,<变量b>)\n高精度加法','_RUN_CLOCK':'_RUN_CLOCK(<代码>)\n执行代码并计算运行所耗时间','_CASE':'_CASE(<变量>,<目标字典>)\n当变量等于字典中的某个键时,执行该键对应的值.\n例:_CASE(1,{1:\'print(\'1\')\',2:\'print(\'2\')\'})的输出为:1.\n当变量不在目标字典的范围内时，会引发KeyError','_HELP':'_HELP(<函数名>)\n输出该函数对应的帮助.当函数名不在模块的范围内时，会引发KeyError'})
    if name:
        if name in d.keys():
            print(d[name])
        else:print('ERR');raise KeyError('ERROR:There is not a function named {} in this module.'.format(name))
    else:
        for i in d.keys():
            print(d[i])
    return
