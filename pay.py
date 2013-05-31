class grossincome:
    _payratehours = 7.25
    _overtimeafter = 40
    _totalhours = 0
    def __init__(payrate,overtimeafter)
    def totalhours(self, hours):
        if hours > self.overtimeafter:
            _self._totalhours = _self._totalhours + (hours - _self.overtimeafter)*1.5 + _self.overtimeafter
        else:
            _self._totalhours = _self._totalhours + hours
            
        
        
    def grosspay(self):
        return self._totalhours*self.payratehours







modela =  model()
modela.totalhours(11.5*6)
modela.totalhours(11.5*3)
#modela.totalhours(11.5*2)
modela.grosspay()
