from decimal import *

class lineVal:
    cur = '' #валютная пара
    date = '' #дата
    time = '' #время
    openVal = 0.0 #начало свечки
    hightVal = 0.0 #верхняя тень свечки
    closeVal = 0.0 #конец свечки
    lowVal = 0.0 #нижняя тень свечки
    lineEnd = '' #херня какая-то
    
def myParsLine(s):
    try:
        i = s.index(",",0,len(s))
        lineVal.cur = s[0:i]
        s = s[i+1:len(s)]
        i = s.index(",",0,len(s))
        lineVal.date = s[0:i]
        s = s[i+1:len(s)]
        i = s.index(",",0,len(s))
        lineVal.time = s[0:i]
        s = s[i+1:len(s)]
        i = s.index(",",0,len(s))
        lineVal.openVal = Decimal(s[0:i])
        s = s[i+1:len(s)]
        i = s.index(",",0,len(s))
        lineVal.hightVal = Decimal(s[0:i])
        s = s[i+1:len(s)]
        i = s.index(",",0,len(s))
        lineVal.lowVal = Decimal(s[0:i])
        s = s[i+1:len(s)]
        i = s.index(",",0,len(s))
        lineVal.closeVal = Decimal(s[0:i])
        lineVal.lineEnd = s[i+1:len(s)]
        return lineVal
    except Exception:
        print ("ошибка формата полученной строки: \n " + str(s) + "\nожидается формат: <TICKER>,<DTYYYYMMDD>,<TIME>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>")

