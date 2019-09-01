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
for i in statfiles.candles: #по всем имеющимся типам свечей
    for line in statfiles.Qfiles[i]: #по каждой строке в сгенерированном файле истории
        y = getCandleFrom(line)
        st.updateVal(st.stat[i]['open'], str(y.openVal), int(y.auth), int(y.freq))
        st.updateVal(st.stat[i]['close'], str(y.closeVal), int(y.auth), int(y.freq))
        st.updateVal(st.stat[i]['hight'], str(y.hightVal), int(y.auth), int(y.freq))
        st.updateVal(st.stat[i]['low'], str(y.lowVal), int(y.auth), int(y.freq))
    st.writeVal(st.stat[i], statfiles.StatFiles, 'open', i)
    st.writeVal(st.stat[i], statfiles.StatFiles, 'hight', i)
    st.writeVal(st.stat[i], statfiles.StatFiles, 'low', i)
    st.writeVal(st.stat[i], statfiles.StatFiles, 'close', i)
statfiles.myShutdowm()
print("finish ;)")
