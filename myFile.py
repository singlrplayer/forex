
import os

class myFile:
    source = {'candlepath':'', 'logpath':'', 'pretext':'','f':False} #путь, название, и переменная исходного файла (здесь и везде: название исходного файла идентично с аббревиатурой валютной пары)
    QfilePath = {} #пути к файлам со свечками
    Qfiles = {} #переменные файлов со свечками
    LogfilePath = {} #пути к файлам с логами
    Logfiles = {} #переменные файлов с логами
    candles = ['minFile','min5File','min15File','min30File','hourFile','hour4File','dayFile','weekFile','monthFile'] #названия свечек. добавляется к названию файла

   
    def myInit (self):
        self.takeFromCfg() #берем значения из конфига
        try:
            self.source['f'] = open(self.source['pretext'] + '.txt','r')
            os.chdir(self.source['candlepath'])
        except Exception:
            print ("ошибка чтения исходного файла котировок. убедитесь, что файл " +self.source['pretext'] + ".txt существует (и желательно не пуст)")
            self.myShutdowm()
        for i in self.candles:
            self.LogfilePath[i] = self.fileCreate(self.source['pretext'] + "_log_" + i + ".txt")
            self.QfilePath[i] = self.fileCreate(self.source['pretext'] + "_" + i + ".txt")
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

    def dircreate(self, s,ind):
        path = os.getcwd()
        path = path + "\\" + s
        try:
            self.source[ind] = path
            os.makedirs(path)
        except OSError:
            if(os.path.isdir(path)):return
            print ("Создать директорию %s не удалось" % path)
        
    def takeFromCfg(self):
        try:
            f = open('config.txt','r')
            z = f.readline()
            z = z[0:len(z)-1]
            self.source['candlepath'] = self.source['pretext'] = str(z)
            self.dircreate(self.source['candlepath'], 'candlepath')
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

