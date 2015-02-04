#!/usr/bin/python3

class Cachorro():
            
    def latir(self):
        print("Uow, Uow...")
        
    def balancar(self):
        super().balancar()
        print("Balancou o rabo")
        
    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, cor):
        self._cor = cor
        
    @cor.deleter
    def cor(self):
        del self._cor
                
def main():
    raffy = Cachorro()
    raffy.cor = 'Preto'
    print(raffy._cor)
    
    
if __name__ == "__main__" : main()