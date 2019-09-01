from candlecreate import candlecreate
from myFile import myFile
from myStat import myStat
from myParsLine import getCandleFrom
from decimal import *

f = candlecreate() #сделали файлы со свечами всех нужных типов без пробелов
statfiles = myFile()
statfiles = statfiles.getStatFiles(f) #подготовка файлов для записи статистики
st = myStat()
st.myInit(statfiles)
statfiles.StatFiles['minFile'].write("hello")
for i in statfiles.candles: #по всем имеющимся типам свечей
    for line in statfiles.Qfiles[i]: #по каждой строке в сгенерированном файле истории
        y = getCandleFrom(line)
        st.updateVal(st.stat[i]['open'], str(y.openVal))
        st.updateVal(st.stat[i]['close'], str(y.closeVal))
        st.updateVal(st.stat[i]['hight'], str(y.hightVal))
        st.updateVal(st.stat[i]['low'], str(y.lowVal))
        #print(st.stat[i])
    for j in st.stat[i]['open']:
        statfiles.StatFiles[i].write("open " + str(j) + " " + str(st.stat[i]['open'][j]))
statfiles.myShutdowm()
print("finish ;)")
