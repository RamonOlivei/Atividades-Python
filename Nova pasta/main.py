from Automovel import *

carro1 = Carro("Chevrolet", "Vectra", "Branco", "Manual", "2020")   
carro2 = Carro("Fiat", "Uno com Escada", "Branco", "Manual", "2004") 

print(carro1)
print("____________________________________________________")
carro1.ligar()
carro1.acelerar(150)
carro1.stop()




print(carro2)
carro2.ligar()
carro2.acelerar(150)
carro2.stop()



print("_________________________________________________________________________________")

moto1 = Moto("Honda", "CB300", "Vermelha", "2015")

print(moto1)
