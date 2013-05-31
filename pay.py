class model:
    week1hours = 0
    week2hours = 0
    payratehours = 23.0
    overtimeafter = 36
    _totalhours = 0
    def totalhours(self, hours):
        if hours > self.overtimeafter:
            self._totalhours = self._totalhours + (hours - self.overtimeafter)*1.5 + self.overtimeafter
        else:
            self._totalhours = self._totalhours + hours
            
        
        
    def grosspay(self):
        print self._totalhours*self.payratehours
    

modela =  model()
modela.totalhours(11.5*6)
modela.totalhours(11.5*3)
#modela.totalhours(11.5*2)
modela.grosspay()
