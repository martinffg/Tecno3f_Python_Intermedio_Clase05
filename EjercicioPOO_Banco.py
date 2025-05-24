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

cc1 = CuentaCorriente("Gabriel", "1111111", "1990/02/03", 1000)
cc2 = CuentaCorriente("Gabriel2", "22222", "1990/02/03", limite_extraccion=1000)


print(cc1.obtener_saldo())
print(cc2.obtener_saldo())