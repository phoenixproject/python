#!/usr/bin/python3

def main():
    
    # Desta forma os dados sao imutaveis
    # Um tipo tuple nao eh mutavel
    x = (1, 2, 3)
    print(type(x),x)
    
    # Desta forma os dados sao uma lista e
    # de dados mutaveis, podendo ser manipulada
    x = [1, 2, 3]
    x.append(4)
    x.insert(0,10)
    x.insert(2,11)
    print(type(x),x)
    
    y = (1, 2, 3, 4)
    for i in y:
        print(i)
       

    k = "Curso de Python"
    for i in k:
        print(i)
    print(k[3])    
    
if __name__ == "__main__" : main()