from candleValues import candleValues

class myStat:
    stat = {}

    def myInit(self, files):
        #candle = candleValues()
        for i in files.candles:
            self.stat[i] = {}
            #for j in canlde.candleVal:
             #   self.stat[i][j] = {} #тут будет словарь по типу: ключ = значение свечи,  значение = частота выпадания. и такая хрень по каждому году отдельно. поправку на подлинность сделаю отдельно
            self.stat[i]['open'] = {}
            self.stat[i]['close'] = {}
            self.stat[i]['hight'] = {}
            self.stat[i]['low'] = {}
            self.stat[i]['auth'] = {}
        return self

    def updateVal(self, mydict, key): #если такое значение уже было, то инкриминируем. нет -- добавляем
        if (key in mydict): mydict[key] = mydict[key] + 1
        else: mydict[key] = 1
