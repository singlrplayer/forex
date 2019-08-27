
class candleValues:
    openVal = {}
    closeVal = {}
    hightVal = {}
    lowVal = {}
    candles = ['min','5min', '15min', '30min', 'hour', '4hour', 'day', 'month']
    candleVal = ['open','close','hight','low']
    candle_tmp = {}


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


    def updateMe(self, y, ind):
        self.updVal(y.openVal, y.closeVal, y.hightVal, y.lowVal,0) #3-й аргумент является индексом вот этой штуки ['min','5min', '15min', '30min', 'hour', '4hour', 'day', 'month']
        for i in self.candles:
            for j in self.candleVal:
                self.candle_tmp[i][j].append(y.candle[j]) #добавляем значений во все свечи
        for j in self.candleVal:
            self.candle_tmp['min'][j] = [] #TODO: сделать более изящное рещшение
        if (ind == 0): return #TODO придумать что-то другое
        if (not ind%5):# return #иначе пришло время делать пятиминутную свечку
            self.updVal(self.candle_tmp['5min']['open'][0],self.candle_tmp['5min']['close'][4],max(self.candle_tmp['5min']['hight']), min(self.candle_tmp['5min']['low']),1)
            for j in self.candleVal:
                self.candle_tmp['5min'][j] = [] #TODO: сделать более изящное рещшение
        if (not ind%15):
            self.updVal(self.candle_tmp['15min']['open'][0],self.candle_tmp['15min']['close'][14],max(self.candle_tmp['15min']['hight']), min(self.candle_tmp['15min']['low']),2)
    
                
