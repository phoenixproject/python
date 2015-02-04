#!/usr/bin/python3

def main():

    x, y = 2, 2
    a, b =  3, 2
    
    resultado = "menor que" if a < b else "maior que"
    print(resultado)
    
    if x < y:
        print("X e menor que Y")
    elif x > y:
        print("X e maior que Y")
    else:
        print("X e igual a Y")
    
if __name__ == "__main__" : main()