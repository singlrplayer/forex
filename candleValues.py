
class candleValues:
    openVal = {}
    closeVal = {}
    hightVal = {}
    lowVal = {}
    candles = ['min','5min', '15min', '30min', 'hour', '4hour', 'day', 'month'] #типы свечей. не трогать. TODO: переделать их так, чтоб брать из конфига. переделать во всех местах 
    candleVal = ['open','close','hight','low'] #четыре параметра, характеризирующие одну (каждую) свечку
    candle_tmp = {} #структура следующая: для каждой свечи (типы свечей две строчки выше) записываем временно значения более мелких(читать "быстрых") свечек, чтоб потом из полученного подобия массива взять минимум\максимум для теней, и открытие\закрытие с первой\послейней мелкой свечки. значения пишем по всем четырем параметрам (см строчку выше)


    def myInit (self, y):
        for i in self.candles:
            self.openVal[i] = y.openVal
            self.closeVal[i] = y.closeVal
            self.hightVal[i] = y.hightVal
            self.lowVal[i] = y.lowVal
            self.candle_tmp[i] = {}
            for j in self.candleVal:
                self.candle_tmp[i][j] = []
        return self

    def updVal(self,a,b,c,d,i):
        try:
            self.openVal[self.candles[i]] = a
            self.closeVal[self.candles[i]] = b
            self.hightVal[self.candles[i]] = c
            self.lowVal[self.candles[i]] = d
        except Exception:
            print ("свечи бывают такие: ['min','5min', '15min', '30min', 'hour', '4hour', 'day', 'month'], а ты просишь такую: "+ str(self.candles[i]))
            print (Exception)

    def updateTMP(self,j): #тут свежеполученную свечку добавляем в темпари, из которых потом делаем следующую, и очищаем значения текущей
                self.candle_tmp[self.candles[j+1]]['open'].append(self.openVal[self.candles[j]]) #TODO переделать всё к черту в едином стиле пока сама еще понимаю
                self.candle_tmp[self.candles[j+1]]['close'].append(self.closeVal[self.candles[j]]) #TODO переделать всё к черту в едином стиле пока сама еще понимаю
                self.candle_tmp[self.candles[j+1]]['hight'].append(self.hightVal[self.candles[j]]) #TODO переделать всё к черту в едином стиле пока сама еще понимаю
                self.candle_tmp[self.candles[j+1]]['low'].append(self.lowVal[self.candles[j]]) #TODO переделать всё к черту в едином стиле пока сама еще понимаю
                for k in self.candleVal:
                    self.candle_tmp[self.candles[j]][k] = [] 


    def updateMe(self, y, ind): #TODO: убедиться в работоспособности и переписать всё красиво. помумать на счет красивого решения месячных и годовых свечей
        try:
            self.updVal(y.openVal, y.closeVal, y.hightVal, y.lowVal,0) #3-й аргумент является индексом вот этой штуки ['min','5min', '15min', '30min', 'hour', '4hour', 'day', 'month']
            for j in self.candleVal:
                self.candle_tmp['5min'][j].append(y.candle[j]) #добавляем значений во все свечи
            if (not ind%5):# пришло время делать пятиминутную свечку из пяти штук минутных  
                self.updVal(self.candle_tmp['5min']['open'][0],self.candle_tmp['5min']['close'][4],max(self.candle_tmp['5min']['hight']), min(self.candle_tmp['5min']['low']),1)
                self.updateTMP(1) # 1 means '5min'
            if (not ind%15): # пришло время делать четвертную свечку из трех штук пятиминутных
                self.updVal(self.candle_tmp['15min']['open'][0],self.candle_tmp['15min']['close'][2],max(self.candle_tmp['15min']['hight']), min(self.candle_tmp['15min']['low']),2)
                self.updateTMP(2) # 2 means '15min'
            if (not ind%30): # пришло время делать получасовую свечку из двух штук минутных
                self.updVal(self.candle_tmp['30min']['open'][0],self.candle_tmp['30min']['close'][1],max(self.candle_tmp['30min']['hight']), min(self.candle_tmp['30min']['low']),2)
                self.updateTMP(3) # 3 means '30min'
            if(not ind%60): # пришло время делать часовую свечку из двух штук получасовых
                self.updVal(self.candle_tmp['hour']['open'][0],self.candle_tmp['hour']['close'][1],max(self.candle_tmp['hour']['hight']), min(self.candle_tmp['hour']['low']),2)
                self.updateTMP(4) # 4 means 'hour'
            if(not ind%240):# пришло время делать четырехчасовую свечку из четырех штук часовых
                self.updVal(self.candle_tmp['4hour']['open'][0],self.candle_tmp['4hour']['close'][3],max(self.candle_tmp['4hour']['hight']), min(self.candle_tmp['4hour']['low']),2)
                self.updateTMP(5) # 5 means '4hour'
        except Exception:
            if (ind == 0): return #TODO придумать что-то другое
            print ("непонятная ошибка в обновлении свечей в строке почучаемого минутного файла " + str(ind))
            print (Exception)
    
                
