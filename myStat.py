from candleValues import candleValues

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
            self.stat[i]['open'] = self.stat[i]['close'] = self.stat[i]['hight'] = self.stat[i]['low'] = {}
            self.stat[i]['auth'] = {}
            self.statVal[i]['body'] = self.statVal[i]['up'] = self.statVal[i]['down'] = {}
        return self

    def updateVal(self, mydict, key, auth, freq): #если такое значение уже было, то инкриминируем. нет -- добавляем
        if (key in mydict):
            mydict[key][0] = mydict[key][0] + 1 #количество совпадений цены
            mydict[key][1] = mydict[key][1] + int(auth) #количество неподнинных свечей (нижнего порядка). неподлинные === не на 100% подлинные
            mydict[key][2] = mydict[key][2] + int(freq) #количество неподлинных минутных свечей в данном значении
        else:
            mydict[key] = [0,0,0]
            mydict[key][0] = 1
            mydict[key][1] = int(auth)
            mydict[key][2] = int(freq)
        return self

    def writeVal(self, mydict, file, key, filekey):
        for j in mydict[key]:
            file[filekey].write(key + ' ' + str(j) + ' ')
            for k in mydict[key][j]:
                file[filekey].write(str(k) + ' ')
            file[filekey].write('\n')
        
