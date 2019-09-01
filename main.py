from candlecreate import candlecreate
from myFile import myFile
from myStat import myStat

f = candlecreate() #сделали файлы со свечами без пробелов
statfiles  = myFile()
statfiles = statfiles.getStatFiles(f) #подготовка файлов для записи статистики
stat = myStat()
stat.myInit(statfiles)


print("finish ;)")
