#!/usr/bin/python3

def main():
    # dicionario = { 'um' : 1, 'dois' : 2, 'tres' : 3, 'quatro' : 4 }
    dicionario = dict(
                      um = 1, dois = 2, tres = 3, quatro = 'quatro'
                      )
    dicionario['cinco'] = 5
    
    print(dicionario)
    
    for k in dicionario:
        print(k, dicionario[k])
        
    for k in dicionario:
        print(k)
        
    for k in sorted(dicionario.keys()):
        print(k, dicionario[k])        
    
if __name__ == "__main__" : main()