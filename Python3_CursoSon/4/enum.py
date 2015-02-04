#!/usr/bin/python3

def main():
        arq = open('exemplo.txt')
        for index, linha in enumerate(arq.readlines()):    
            print(index,linha, end='')
            
        s = "esse e meu texto"
        for i, c in enumerate(s):
            print(i, c)
    
if __name__ == "__main__" : main()