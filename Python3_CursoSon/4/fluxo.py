#!/usr/bin/python3

def main():
        s = "esse e meu texto"
        for c in s:
            # if c == 't': continue
            if c == 't': break
            print(c, end='')
    
if __name__ == "__main__" : main()