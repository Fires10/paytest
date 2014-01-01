class taxes:
    _married 
    _dependents
    _grosspay
    _pretaxbenefits
    _taxablepay
    _taxtable
    _withholdingallowance = 151.90
        
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
        taxline = ''
        taxpay = self.taxablepay() - self._dependents * 151.90
        for line in self._taxtable:
            line = line.split(',')
            if self.taxablepay() < float(line[0]) && self.taxablepay() < float(line[1]):
                taxline = line
        
        fedtax = float(line[2]) + (taxpay - float(line[0])*float(line[3])
        return fedtax
            
        
        
        
    
        
    
       
