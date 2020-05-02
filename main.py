from candlecreate import candlecreateASIS
from myFile import myFile
from myStat import myStat
from myParsLine import getCandleFrom
from decimal import *

statfiles = myFile('AUDUSD')
for i in statfiles.candles: #по всем имеющимся типам свечей
    if(statfiles.QfilePath[i] == ''): continue
    f = candlecreateASIS(statfiles.Qfiles[i], statfiles.TmpFiles[i], 1000) #сделали файлы со свечами всех нужных типов без пробелов
statfiles = statfiles.getStatFiles() #подготовка файлов для записи статистики
#f = candlecreate() #сделали файлы со свечами всех нужных типов без пробелов
st = myStat()
st.myInit(statfiles)
const = 10000 #коэфициент перевода производной цены в пункты
#intervals = 6 #нужное количество интервалов 
counter = {} #количества тел и теней
for i in statfiles.candles: #по всем имеющимся типам свечей
    if(statfiles.QfilePath[i] == ''): continue
    print (i)
    statfiles.Qfiles[i].seek(0)
    for line in statfiles.Qfiles[i]: #по каждой строке в сгенерированном файле истории
        y = getCandleFrom(line)
        st.updateVal(st.stat[i]['open'], str(y.openVal), int(y.auth), int(y.freq))
        st.updateVal(st.stat[i]['close'], str(y.closeVal), int(y.auth), int(y.freq))
        st.updateVal(st.stat[i]['hight'], str(y.hightVal), int(y.auth), int(y.freq))
        st.updateVal(st.stat[i]['low'], str(y.lowVal), int(y.auth), int(y.freq))
        tmp = int((y.closeVal - y.openVal) * const)
        if (tmp > 0): #TODO: убедиться в работоспособности и переделать
            st.updateVal(st.statVal[i]['bodyup'], int(tmp), int(y.auth), int(y.freq))
        else:
            if(tmp < 0): 
                st.updateVal(st.statVal[i]['bodydown'], int(tmp), int(y.auth), int(y.freq))
            else:
                st.updateVal(st.statVal[i]['bodyzero'], int(tmp), int(y.auth), int(y.freq))
        if (y.closeVal < y.openVal):
            tmp = int((y.hightVal - y.openVal) * const) # верхняя тень считается максимум минус верхзняя часть тела (верхняя часть тела разная в зависимости какая у нас свеча)
            tmp1 = int((y.closeVal - y.lowVal) * const) # нижняя тень считается аналогично
        else:
            tmp = int((y.hightVal - y.closeVal) * const)
            tmp1 = int((y.openVal - y.lowVal) * const)
        st.updateVal(st.statVal[i]['up'], int(tmp), int(y.auth), int(y.freq))
        st.updateVal(st.statVal[i]['down'], int(tmp1), int(y.auth), int(y.freq))
        st.updateVal(st.statVal[i]['upopen'], int((y.hightVal - y.openVal) * const), int(y.auth), int(y.freq))
        st.updateVal(st.statVal[i]['upclose'], int((y.hightVal - y.closeVal) * const), int(y.auth), int(y.freq))
        st.updateVal(st.statVal[i]['minopen'], int((y.openVal - y.lowVal) * const), int(y.auth), int(y.freq))
        st.updateVal(st.statVal[i]['minclose'], int((y.closeVal - y.lowVal) * const), int(y.auth), int(y.freq))
        st.updateVal(st.statVal[i]['vol'], int((y.hightVal - y.lowVal) * const), int(y.auth), int(y.freq))
        
      
    st.writeVal(st.stat[i], statfiles.StatFiles, 'open', i)
    st.writeVal(st.stat[i], statfiles.StatFiles, 'hight', i)
    st.writeVal(st.stat[i], statfiles.StatFiles, 'low', i)
    st.writeVal(st.stat[i], statfiles.StatFiles, 'close', i)
    
    for key in st.statVal[i]: 
       counter[key] = st.writeVal(st.statVal[i], statfiles.StatFiles, key, i) 
    bo = st.getBorders(counter, 6, st.statVal[i], const)
    st.saveBorders(bo, statfiles.source['borders'], i, 6)
    bo = st.getBorders(counter, 5, st.statVal[i], const)
    st.saveBorders(bo, statfiles.source['borders'], i, 5)
    bo = st.getBorders(counter, 4, st.statVal[i], const)
    st.saveBorders(bo, statfiles.source['borders'], i, 4)
statfiles.myShutdowm()
print("finish ;)")
