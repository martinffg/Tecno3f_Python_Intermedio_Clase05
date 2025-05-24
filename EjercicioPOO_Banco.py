# Práctica Clase 5
# Se debe modificar la clase CuentaBancaria para que sea abstracta , ademas los metodos extraer y depositar deben volverse abstractos,
# tambien se debe crear una clase CuentaAhorro que herede de CuentaBancaria y se le agregue un atributo privado de tasa de interes,
# el cual tendra un valor establecido de 0.001 y un metodo que nos calcule el interes.

from CuentaAhorro import CuentaAhorro
from CuentaCorriente import CuentaCorriente
from CuentaBancaria import CuentaBancaria

cuenta1 = CuentaAhorro("Gabriel", 333333, "1990/02/03", 15000, 1)

print(cuenta1)
print(cuenta1.obtener_edad())
cuenta1.depositar(1500)
cuenta1.extraer(200)
print(cuenta1.obtener_saldo())
print(cuenta1.calcular_interes_saldo())

cuenta2 = CuentaAhorro("Pedro", 1111111, "1909/03/03", 7000, 0.5)

print(cuenta2)

print(cuenta2.obtener_edad())
cuenta2.depositar(5500)
cuenta2.extraer(20000)
print(cuenta2.obtener_saldo())
print(cuenta2.calcular_interes_saldo())

cc1 = CuentaCorriente("Roberto", "4444444", "1998/04/03", 3000)

print(cc1)
print(cc1.obtener_edad())
cc1.depositar(1500)
cc1.extraer(200)
print(cc1.obtener_saldo())

cc2 = CuentaCorriente("Carlos", "22222", "1999/02/02", limite_extraccion=3100)

print(cc2)
print(cc2.obtener_edad())
cc2.depositar(5000)
cc2.extraer(2000)
print(cc2.obtener_saldo())
