#!/usr/bin/python3

def main():
    func(10, 20)

# Neste caso abaixo valor2 eh opcional
def func(valor1, valor2=None):
# def func(valor1, valor2 = 20):
    # pass
    print(valor1, valor2)
    
if __name__ == "__main__" : main()