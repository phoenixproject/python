#!/usr/bin/python3
from br.edu.ifes.poo2.adapter.cdp.FiltroInterface import FiltroInterface

class AbstractFiltroPlus(FiltroInterface):
    
    def FiltrarAgua(self):
        print("Filtrando agua gasosa no filtro de Agua Gasosa")
        
    def AumentarVolumeDeAgua(self):
        print("Aumentando volume de agua para uma filtragem rapida")
        
    def DiminuirVolumeDeAgua(self):
        print("Diminuindo o volume de agua. A filtragem sera mais lenta")