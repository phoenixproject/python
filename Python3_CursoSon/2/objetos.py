#!/usr/bin/python3

class Carro:
    # Metodo Construtor da classe
    def __init__(self, tipo ="Corsa"):
        # Criando uma variavel chamada tipo dentro do construtor
        self.tipo = tipo
        
    def tipoCarro(self):
        return self.tipo

def main():
    carro1 = Carro()
    print(carro1.tipoCarro())
    carro2 = Carro('Ka')
    print(carro2.tipoCarro())
    x = carro2.tipoCarro()
    print(x)
    
    
if __name__ == "__main__" : main()