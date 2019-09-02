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
print (st.statVal['minFile']['body'])
for i in statfiles.candles: #по всем имеющимся типам свечей
    for line in statfiles.Qfiles[i]: #по каждой строке в сгенерированном файле истории
        y = getCandleFrom(line)
        st.updateVal(st.stat[i]['open'], str(y.openVal), int(y.auth), int(y.freq))
        st.updateVal(st.stat[i]['close'], str(y.closeVal), int(y.auth), int(y.freq))
        st.updateVal(st.stat[i]['hight'], str(y.hightVal), int(y.auth), int(y.freq))
        st.updateVal(st.stat[i]['low'], str(y.lowVal), int(y.auth), int(y.freq))
        tmp = y.closeVal - y.openVal
        st.updateVal(st.statVal[i]['body'], str(tmp), int(y.auth), int(y.freq))
        if (y.closeVal < y.openVal):
            tmp = y.hightVal - y.openVal # верхняя тень считается максимум минус верхзняя часть тела (верхняя часть тела разная в зависимости какая у нас свеча)
            tmp1 = y.closeVal - y.lowVal # нижняя тень считается аналогично
        else:
            tmp = y.hightVal - y.closeVal
            tmp1 = y.openVal - y.lowVal
        st.updateVal(st.statVal[i]['up'], str(tmp), int(y.auth), int(y.freq))
        st.updateVal(st.statVal[i]['down'], str(tmp1), int(y.auth), int(y.freq))
    st.writeVal(st.stat[i], statfiles.StatFiles, 'open', i)
    st.writeVal(st.stat[i], statfiles.StatFiles, 'hight', i)
    st.writeVal(st.stat[i], statfiles.StatFiles, 'low', i)
    st.writeVal(st.stat[i], statfiles.StatFiles, 'close', i)
    st.writeVal(st.statVal[i], statfiles.StatFiles, 'body', i)
    st.writeVal(st.statVal[i], statfiles.StatFiles, 'up', i)
    st.writeVal(st.statVal[i], statfiles.StatFiles, 'down', i)
statfiles.myShutdowm()
print("finish ;)")
