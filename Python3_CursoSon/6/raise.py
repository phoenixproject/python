#!/usr/bin/python3

def main():
    try:        
        for linha in ler('exemplo.doc'): print(linha.strip())
    except IOError as e:
        print("Arquivo nao encontrado", e)
    except ValueError as e:
        print('Tipo de arquivo invalido')
            
def ler(nomearquivo):
    if nomearquivo.endswith('.txt'):
        arquivo = open(nomearquivo)
        return arquivo.readlines()
    else: raise ValueError('A extensao do arquivo deve ser .txt')
    
if __name__ == "__main__" : main()