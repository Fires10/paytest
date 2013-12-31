class taxes:
    _married 
    _dependents
    _grosspay
    _pretaxbenefits
    _taxablepay
        
    def __init__(married=0,dependents=0):
         
         self.married = married
         self._dependents = dependents
    def pretaxbenefits(ben=0):
        
        self._pretaxbenefits = ben
        
    def grosspay(pay):
        
        self._grosspay = pay
    
    def taxablepay():
        return self._grosspay - self._pretxbenefits
        
        
    def medicare():
        return self.taxablepay() * 0.0145
        
    def socialsecuritytax():
        return self.taxablepay() * 0.062
        
        
    
        
    
       
