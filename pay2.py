class grossincome:
    _payratehours = 7.25
    _overtimeafter = 40
    _totalhours = 0
    def __init__(self,payrate,overtimeafter):
        
        self._payratehours = float(payrate)
        self._overtimeafter = float(overtimeafter)
        
    def totalhours(self, hours):
        hours = float(hours)
        if hours > self._overtimeafter:
            self._totalhours = self._totalhours + (hours - self._overtimeafter)*1.5 + self._overtimeafter
        else:
            self._totalhours = self._totalhours + hours
            
        
        
    def grosspay(self):
        return self._totalhours*self._payratehours
    

payr = raw_input( "What is your pay rate?")





modela =  grossincome(payr,36)
w1w = raw_input("how many hours did you work week one?")

modela.totalhours(w1w)
w1o = raw_input("how many hours nonworked hours do you have week one?")

modela.totalhours(w1o)
w2w = raw_input("how many hours did you work week two?")
modela.totalhours(w2w)
w2o = raw_input("how many hours nonworked hours do you have?")
modela.totalhours(w2o)
#print modela._payratehours
#print modela._overtimeafter
#print modela._totalhours
print "Your grosspay:$" + str(modela.grosspay())
