class taxes:
    _married 
    _dependents
    _grosspay
    _pretaxbenefits
    _taxablepay
    _taxtable
        
    def __init__(married=0,dependents=0):
         
         self._married = married
         self._dependents = dependents
         if self._married == 1:
            with open("married.table", 'r') as lin:
                self._taxtable = lin.read()
         else:
             with open("single.table", 'r') as lin:
                 self._taxtable = lin.read()
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
        
        
    def federaltax():
        return "this is insane"
        
        
        
    
        
    
       
