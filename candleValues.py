
class candleValues:
    openVal = {}
    closeVal = {}
    hightVal = {}
    lowVal = {}
    candles = ['min','5min', '15min', '30min', 'hour', '4hour', 'day', 'month']


    def myInit (self):
        for i in self.candles:
            self.openVal[i] = self.closeVal[i] = self.hightVal[i] = self.lowVal[i] = 0
        return self
    
