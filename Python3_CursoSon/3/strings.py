#!/usr/bin/python3

def main():
    
    texto = "Curso de Python"
    print(texto)
    
    # Como tudo em Python 3 eh objeto, entao eh possivel chamar um metodo na string
    texto = "{} Curso de Python".format(2)
    print(texto)
    
    # No `Python 2 eh parecido com a sintaxe do C
    numero = 2
    texto = "%s Curso de Python" % numero
    print(texto)
    
    # Caracter de salto de linha \n inserido na string
    texto = "{} Curso \nde Python".format(2)
    print(texto)
    
    # Colocando a string r na frente da string, ele entende 
    # que este eh um formato raw (cru) e nao vai interpreta o caracter especial,
    # mas sim como texto
    texto = r"{} Curso \nde Python".format(2)
    print(texto)
    
    # Um texto sem precisar dar o \n
    texto = '''
    Meu texto em Python
    com varias linhas
    com mais linhas
    '''
    print(texto)
    
    # Um texto sem precisar dar o \n com o caracter de escape para nao
    # contabilizar a primeira linha
    texto = '''\
    Meu texto em Python
    com varias linhas
    com mais linhas
    '''
    print(texto)    
    
if __name__ == "__main__" : main()