#!/usr/bin/python3

def main():
    numero = 40 / 9
    print(type(numero), numero)
    
    # Arredondamento
    numero = round(40 / 9)
    print(type(numero), numero)
    
    # Traz as casa decimais
    numero = round(40 / 15, 2)
    print(type(numero), numero)

    # Para tornar um numero diretamente em float
    numero = float(4)
    print(type(numero), numero)

    
if __name__ == "__main__" : main()