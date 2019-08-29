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
    candleVal = ['open','close','hight','low', 'auth'] #ключи. не трогать. для некоторых других мест. переделать. последний параметр характеризирует подлинность свечки (0 значит подлинный)
    candle = {} #попытка все сделать красиво
    olddata = {'olddate':'','oldtime':'','olDopenVal':0,'olDhightVal':0,'olDlowVal':0,'olDcloseVal':0} #костыль с рюшечками
    
    def rememberOldDatatime(self, val):
        self.olddata['olddate'] = val.d
        self.olddata['oldtime'] = val.t

    def rememberOldCandle(self):
       self.olddata['olDopenVal'] = lineVal.candle['open']
       self.olddata['olDlowVal'] = lineVal.candle['low']
       self.olddata['olDhightVal'] = lineVal.candle['hight']
       self.olddata['olDcloseVal'] = lineVal.candle['close'] 

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
        lineVal.candle['open'] = lineVal.openVal = Decimal(s[0:i])
        s = s[i+1:len(s)]
        i = s.index(",",0,len(s))
        lineVal.candle['hight'] = lineVal.hightVal = Decimal(s[0:i])
        s = s[i+1:len(s)]
        i = s.index(",",0,len(s))
        lineVal.candle['low'] = lineVal.lowVal = Decimal(s[0:i])
        s = s[i+1:len(s)]
        i = s.index(",",0,len(s))
        lineVal.candle['close'] = lineVal.closeVal = Decimal(s[0:i])
        lineVal.lineEnd = s[i+1:len(s)]
        lineVal.candle['auth'] = 0
        return lineVal
    except Exception:
        print ("ошибка формата полученной строки: \n " + str(s) + "\nожидается формат: <TICKER>,<DTYYYYMMDD>,<TIME>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>")



