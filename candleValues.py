
class candleValues:
    openVal = {}
    closeVal = {}
    hightVal = {}
    lowVal = {}
    candles = ['min','5min', '15min', '30min', 'hour', '4hour', 'day', 'month']


    def myInit (self, y):
        for i in self.candles:
            self.openVal[i] = y.openVal
            self.closeVal[i] = y.closeVal
            self.hightVal[i] = y.hightVal
            self.lowVal[i] = y.lowVal
        return self

    def updVal(self,y,i):
        try:
            self.openVal[self.candles[i]] = y.openVal
            self.closeVal[self.candles[i]] = y.closeVal
            self.hightVal[self.candles[i]] = y.hightVal
            self.lowVal[self.candles[i]] = y.lowVal
        except Exception:
            print ("свечи бывают такие: ['min','5min', '15min', '30min', 'hour', '4hour', 'day', 'month'], а ты просишь такую: "+ str(self.candles[i]))
                
