class KyokoLoggingkun():
    def __init__(self,baseoutkun,nocrkun):
        self.logginkun=baseoutkun
        self.nocrlogging=nocrkun
    def normalout(self,strkun:str):
        self.nocrlogging(strkun)
    def colorout(self,color:str,strkun:str):
        self.logginkun(color,strkun)
    def errout(self,strkun:str):
        self.logginkun("#FF0000",strkun)
    def successout(self,strkun:str):
        self.logginkun("#00FF00",strkun)
    def warnout(self,strkun:str):
        self.logginkun("#FFFF00",strkun)
    def debugout(self,strkun:str):
        self.logginkun("#FF00FF",strkun)
    def blueout(self,strkun:str):
        self.logginkun("#0000FF",strkun)
