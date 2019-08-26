
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
    
