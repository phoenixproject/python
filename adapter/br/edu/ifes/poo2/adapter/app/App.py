#!/usr/bin/python3
from br.edu.ifes.poo2.adapter.cdp.FiltroAguaNatural import FiltroAguaNatural
from br.edu.ifes.poo2.adapter.cdp.FiltroAguaGelada import FiltroAguaGelada
from br.edu.ifes.poo2.adapter.cdp.FiltroAguaESaiGelo import FiltroAguaESaiGelo
from br.edu.ifes.poo2.adapter.cdp.FiltroAguaGasosa import FiltroAguaGasosa

def main():
    
    #Padrao Adapter
    print('')
    filtro = FiltroAguaNatural()
    filtro.FiltrarAgua()
    
    print('')
    filtro = FiltroAguaGelada()
    filtro.FiltrarAgua()
    
    print('')
    filtro = FiltroAguaESaiGelo()
    filtro.FiltrarAgua()
    
    
    #Padrao Bridge
    print('')
    filtro = FiltroAguaGasosa()
    filtro.FiltrarAgua()
    filtro.AumentarVolumeDeAgua()
    filtro.DiminuirVolumeDeAgua()

if __name__ == "__main__" : main()