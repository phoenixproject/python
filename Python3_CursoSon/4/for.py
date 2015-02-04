#!/usr/bin/python3

def main():
    arq = open('exemplo.txt')
    for linha in arq.readlines():
    # for linha in [1, 2, 3, 4]:
        print(linha, end='')
    
    
if __name__ == "__main__" : main()