#!/usr/bin/python3
from br.edu.ifes.poo2.adapter.cdp.FiltroInterface import FiltroInterface

class AbstractFiltro(FiltroInterface):
    
    def FiltrarAgua(self):        
        print('Filtrando agua')