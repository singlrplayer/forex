currency = 'AUDJPY'

from decimal import *
#import time
import itertools
from updMytime import updMytime
from myParsLine import myParsLine
from myFile import myFile

files = myFile()
files.myInit()
f = open(currency + '.txt', 'r')
f_min = open(currency + '_min.txt', 'w') #min здесь и далее означает минуты, а не минимум
x = f.readline(); f_min.write(x)
x = f.readline(); y = myParsLine(x)
date = olddate = y.date;
time = oldtime = y.time
olDopenVal = openVal = y.openVal; olDhightVal = hightVal = y.hightVal; olDlowVal = lowVal = y.lowVal; olDcloseVal = closeVal = y.closeVal
f_min.close()
f_log = open (currency + '_log.txt', 'w')
f_log.close()
j = j_min = 1
itertools.islice(f,1)
for line in f:
    y = myParsLine(line)
    f_min = open(currency + '_min.txt', 'a')
    f_min.write(y.cur+','+str(olddate)+','+str(oldtime)+','+str(olDopenVal)+','+str(olDhightVal)+','+str(olDlowVal)+','+str(olDcloseVal)+','+y.lineEnd)
    f_min.close()
    date = y.date
    time = y.time
    openVal = y.openVal
    hightVal = y.hightVal
    lowVal = y.lowVal
    closeVal = y.closeVal
    j = j +1; j_min = j_min +1 
    val = updMytime(oldtime, olddate)
    oldtime = val.t
    olddate = val.d
    while ((time > oldtime or date > olddate)):
            j_min = j_min +1
            f_min = open(currency + '_min.txt', 'a') #текущие котировки дописываем в конец минутного файла
            f_min.write(y.cur+','+str(olddate)+','+str(oldtime)+','+str(olDopenVal)+','+str(olDhightVal)+','+str(olDlowVal)+','+str(olDcloseVal)+','+y.lineEnd)
            f_min.close()
            f_log = open (currency + '_log.txt', 'a')
            f_log.write("incerted time " + str (oldtime)+" at " + str(olddate) + ",   line " + str(j_min) + "\n")
            f_log.close()
            val = updMytime(oldtime, olddate)
            oldtime = val.t
            olddate = val.d
       #основная мысль: дыры в котировках появились за счет того, что в данный отрезок времени сделок небыло, следовательно мы их заполняем идентичными свечками, потому как ничего не менялось
       #возможны 100500 иных причин дырам в котировках, да ;)
       #возможно, апроксимация сработает лучше, но это будет видно уже при обучении
    olDopenVal = openVal
    olDhightVal = hightVal
    olDlowVal = lowVal
    olDcloseVal = closeVal
    oldtime = time
    olddate = date

f.close()
files.myShutdowm()

print ("old " + str(j) + '\nnew ' + str(j_min))
