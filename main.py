currency = 'AUDJPY'

from decimal import *
#import time
import itertools
from updMytime import updMytime
from myParsLine import myParsLine
from myFile import myFile

files = myFile()
files.myInit()
files.Qfiles['minFile'].write(files.source['f'].readline()) #первую строку переписываем, но только в минутный файл. мне надо, чтобы его понимал форексовый терминал
y = myParsLine(files.source['f'].readline()) #вторую парсим чтоб задать стартовые значения (надо будет сделать это как-то изящнее)
date = olddate = y.date;
time = oldtime = y.time
olDopenVal = openVal = y.openVal; olDhightVal = hightVal = y.hightVal; olDlowVal = lowVal = y.lowVal; olDcloseVal = closeVal = y.closeVal
j = j_min = 1
itertools.islice(files.source['f'],1)
for line in files.source['f']:
    y = myParsLine(line)
    files.Qfiles['minFile'].write(y.cur+','+str(olddate)+','+str(oldtime)+','+str(olDopenVal)+','+str(olDhightVal)+','+str(olDlowVal)+','+str(olDcloseVal)+','+y.lineEnd)
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
            files.Qfiles['minFile'].write(y.cur+','+str(olddate)+','+str(oldtime)+','+str(olDopenVal)+','+str(olDhightVal)+','+str(olDlowVal)+','+str(olDcloseVal)+','+y.lineEnd)
            files.Logfiles['minFile'].write("incerted time " + str (oldtime)+" at " + str(olddate) + ",   line " + str(j_min) + "\n")
            val = updMytime(oldtime, olddate)
            oldtime = val.t
            olddate = val.d
       #основная мысль: дыры в котировках появились за счет того, что в данный отрезок времени сделок небыло, следовательно мы их заполняем идентичными свечками, потому как ничего не менялось
       #возможны 100500 иных причин дырам в котировках, да ;) выходные и всяческие bank holydays например
       #возможно, апроксимация сработает лучше, но это будет видно уже при обучении
    olDopenVal = openVal
    olDhightVal = hightVal
    olDlowVal = lowVal
    olDcloseVal = closeVal
    oldtime = time
    olddate = date

files.myShutdowm()

print ("old " + str(j) + '\nnew ' + str(j_min))
