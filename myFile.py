
import os

class myFile:
    source = {'candlepath':'', 'logpath':'', 'pretext':'','f':False} #путь, название, и переменная исходного файла (здесь и везде: название исходного файла идентично с аббревиатурой валютной пары)
    QfilePath = {} #файлы со свечками
    Qfiles = {} #переменные файлов со свечками
    LogfilePath = {} #пфайлы с логами
    Logfiles = {} #переменные файлов с логами
    StatFilePath = {} #файлы статистики
    StatFiles = {} # переменные файлов статистики
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
            if(i in self.Qfiles): self.Qfiles[i].close()
            if(i in self.Logfiles): self.Logfiles[i].close()
            if(i in self.StatFiles): self.StatFiles[i].close()
            #self.QfilePath[i] = ''
            #self.LogfilePath[i] = ''
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
            z = z[0:len(z)-1] #некрасивое удаление знака конца строки. переделать
            self.source['candlepath'] = self.source['pretext'] = str(z)
            self.dircreate(self.source['candlepath'], 'candlepath')
            return self
        except Exception:
            print ("ошибка конфига. убедитесь, что файл 'config.txt' существует (и желательно не пуст).")
            self.myShutdowm()
    
    def fileCreate(self, s):
        try:
            f = open(s,'w')
            f.close()
            return s
        except Exception:
            print ("ошибка попытки создания\перезаписи файла " + s)
            self.myShutdowm()

    def getStatFiles(self, candlefiles):
        for i in self.candles:
            try:
                self.Qfiles[i] = open(candlefiles.QfilePath[i], 'r') #теперь, когда уже все сделано, мы открываем файлы на чтение для сбора статистики значений свечей за весь период
            except Exception:
                print ("ошибка открытия файл " + candlefiles.QfilePath[i])
                self.myShutdowm()
                candlefiles.myShutdowm()
            try:
                self.StatFilePath[i] = self.fileCreate(candlefiles.source['pretext'] + "_stat_" + i + ".txt") #сюда складывать будем статистику значений
            except Exception:
                print ("создания файла статистики " + candlefiles.QfilePath[i])
                self.myShutdowm()
                candlefiles.myShutdowm()
            try:
                self.StatFiles[i] = open(self.StatFilePath[i], 'a') #и открываем на дозапись
            except Exception:
                print ("ошибка открытия файл " + self.StatFilePath[i])
                self.myShutdowm()
                candlefiles.myShutdowm()
        return self
                
        

