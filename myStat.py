from candleValues import candleValues
import math

class myStat:
    stat = {}
    statVal = {}#значения пока еще не размытых характеристик свечи для обучения нейронной сети: по всем тимам свечей по всем 3-м параметрам(размер тела, размер верхней тени, размер нижней тени)

    def myInit(self, files):
        #candle = candleValues()
        for i in files.candles:
            self.stat[i] = {}
            self.statVal[i] = {}
            #for j in canlde.candleVal:
             #   self.stat[i][j] = {} #тут будет словарь по типу: ключ == значение свечи,  значение == частота выпадания. и такая хрень по каждому году отдельно. поправку на подлинность сделаю отдельно
            self.stat[i]['open'] = {}
            self.stat[i]['close'] = {}
            self.stat[i]['hight'] = {}
            self.stat[i]['low'] = {}
           # self.stat[i]['auth'] = {}
            self.statVal[i]['bodyzero'] = {}
            self.statVal[i]['bodyup'] = {}
            self.statVal[i]['bodydown'] = {}
            self.statVal[i]['up'] = {}
            self.statVal[i]['down'] = {}
            self.statVal[i]['upopen'] = {}
            self.statVal[i]['upclose'] = {}
            self.statVal[i]['minopen'] = {}
            self.statVal[i]['minclose'] = {}
            self.statVal[i]['vol'] = {}
        return self

    def updateVal(self, mydict, key, auth, freq): #если такое значение уже было, то инкриминируем. нет -- добавляем
        if (key in mydict):
            mydict[key][0] = mydict[key][0] + 1 #количество совпадений цены
            mydict[key][1] = mydict[key][1] + int(auth) #количество неподнинных свечей (нижнего порядка). неподлинные === не на 100% подлинные
            mydict[key][2] = mydict[key][2] + int(freq) #количество неподлинных минутных свечей в данном значении
        else:
            mydict[key] = [1,0,0]
            #mydict[key][0] = 1
            mydict[key][1] = int(auth)
            mydict[key][2] = int(freq)


    def writeVal(self, mydict, file, key, filekey):
        count = 0
        for j in mydict[key]:
            file[filekey].write(key + ' ' + str(j) + ' ')
            count = count + mydict[key][j][0]
            for k in mydict[key][j]:
                file[filekey].write(str(k) + ' ')
            file[filekey].write('\n')
        return count
        
        
    def getBorders(self, counts, intervals, candles, const):
        ro = math.log(const, 10) # round 
        borders = {}
        if (intervals < 2): return -1 #нужное количество интервалов слмшком мало
        counts['bodyup'] = counts['bodyup'] + counts['bodyzero'] / 2 #разбиваем ноль поровну ;) 
        counts['bodydown'] = counts['bodydown'] + counts['bodyzero'] / 2
        counts.pop('bodyzero')
        for key in counts:
            borders[key] = [0.0]
        for key in counts: 
            count = counts[key] / intervals
            list_keys = list(candles[key].keys())
            if(key == 'bodydown'):
                list_keys.sort(reverse=True)
            else:
                list_keys.sort()
            i = 0
            for key2 in list_keys: 
                i = i + int(candles[key][key2][0])
                if(i > count):
                    i = 0
                    borders[key].append(float(key2)/const)
        return borders
    
    def saveBorders(self, borders, f, candletype):
        f.write(str(candletype) + "\n")
        for key in borders: 
            f.write(str(key) + ": " + str(borders[key]) + "\n")
            
    def makeConfig(self, borders, candletype): #TODO: дописать
        return 1
        
