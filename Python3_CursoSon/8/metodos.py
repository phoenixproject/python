#!/usr/bin/python3

class Cachorro:
    def __init__(self, numero):
        self._numero = numero
        # print('Criando cachorro!')
        
    def latir(self):
        print(self._numero,"Uow, Uow...")
        
    def balancar(self):
        print(self._numero,"Balancou o rabo")
        
def main():
    raffy = Cachorro(1)
    raffy.latir()
    raffy.balancar()
    
    scrappy = Cachorro(2)
    scrappy.latir()
    scrappy.balancar()
    
if __name__ == "__main__" : main()