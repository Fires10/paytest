class grossincome:
    _payratehours = 7.25
    _overtimeafter = 40
    _totalhours = 0
    def __init__(self,payrate,overtimeafter):
        
        self._payratehours = float(payrate)
        self._overtimeafter = float(overtimeafter)
        
    def totalhours(self, hours):
        if hours > self._overtimeafter:
            self._totalhours = self._totalhours + (hours - self._overtimeafter)*1.5 + self._overtimeafter
        else:
            self._totalhours = self._totalhours + hours
            
        
        
    def grosspay(self):
        return self._totalhours*self._payratehours







modela =  grossincome(17.29,36)
modela.totalhours(11.5*6)
modela.totalhours(11.5*3)
#modela.totalhours(11.5*2)
print modela._payratehours
print modela._overtimeafter
print modela._totalhours
print modela.grosspay()
