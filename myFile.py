
class myFile:
    source = {'path':'', 'pretext':'','f':False} #путь, название, и переменная исходного файла (здесь и везде: название исходного файла идентично с аббревиатурой валютной пары)
    QfilePath = {} #пути к файлам со свечками
    Qfiles = {} #переменные файлов со свечками
    LogfilePath = {} #пути к файлам с логами
    Logfiles = {} #переменные файлов с логами
    candles = ['minFile','min5File','min15File','min30File','hourFile','hour4File','dayFile','weekFile','monthFile'] #названия свечек. добавляется к названию файла

   
    def myInit (self):
        self.takeFromCfg() #берем значения из конфига
        try:
            self.source['f'] = open(self.source['pretext'] + '.txt','r')
        except Exception:
            print ("ошибка чтения исходного файла котировок. убедитесь, что файл " +self.source['pretext'] + ".txt существует (и желательно не пуст)")
            self.myShutdowm()
        for i in self.candles:
            self.QfilePath[i] = self.fileCreate(self.source['pretext'] + "_" + i + ".txt")
            self.LogfilePath[i] = self.fileCreate(self.source['pretext'] + "_log_" + i + ".txt")
            try:
                self.Qfiles[i] = open(self.QfilePath[i], 'a')
                self.Logfiles[i] = open(self.LogfilePath[i], 'a')
            except Exception:
                print ("ошибка открытия файлов " + self.QfilePath[i] + " и\или " + self.QlogfilePath[i])
                self.myShutdowm()
        return self

    def myShutdowm(self):
        for i in self.candles:
            if(self.Qfiles[i]): self.Qfiles[i].close()
            if(self.Logfiles[i]): self.Logfiles[i].close()
            self.QfilePath[i] = ''
            self.LogfilePath[i] = ''
        self.source['f'].close()
        self.source['pretext'] = ''     
        
    def takeFromCfg(self):
        try:
            f = open('config.txt','r')
            z = f.readline()
            self.source['pretext'] = str(z)
            return self
        except Exception:
            print ("ошибка конфига. убедитесь, что файл 'config.txt' существует (и желательно не пуст).")
            self.myShutdowm()
    
    def fileCreate(self, s):
        try:
            f = open(s,'w')
            return s
        except Exception:
            print ("ошибка попытки создания\перезаписи файла " + s)
            self.myShutdowm()

