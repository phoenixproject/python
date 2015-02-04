#!/usr/bin/python3

class Animal:
    def andar(self):
        print('Eu estou andando')
        
    def balancar(self):
        print('Eu balanco muito')
        
    def comer(self):
        print('Estou com fome. Vou comer!')

class Cachorro(Animal):
            
    def latir(self):
        print("Uow, Uow...")
        
    def balancar(self):
        super().balancar()
        print("Balancou o rabo")
        
    def get_cor(self):
        return self._cor
    
    def set_cor(self, cor):
        self._cor = cor
        
class Gato(Animal):
    
    def balancar(self):
        print('Gato balanca diferente')

class Miau(Gato):
    pass
        
def main():
    raffy = Cachorro()
    raffy.comer()    
    raffy.balancar()
    
    gatinha = Gato()
    gatinha.comer()
    gatinha.balancar()
    
    miau = Miau()
    miau.balancar()
    
if __name__ == "__main__" : main()