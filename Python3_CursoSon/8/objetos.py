#!/usr/bin/python3

class Cachorro:
    def __init__(self, cor = 'branco'):
        self._cor = cor
        
    def latir(self):
        print(self._numero,"Uow, Uow...")
        
    def balancar(self):
        print(self._numero,"Balancou o rabo")
        
    def get_cor(self):
        return self._cor
    
    def set_cor(self, cor):
        self._cor = cor
        
def main():
    raffy = Cachorro(1)
    raffy.set_cor('preto')
    print(raffy.get_cor())
    raffy.set_cor('vermelho')
    print(raffy.get_cor())    
    
    
if __name__ == "__main__" : main()