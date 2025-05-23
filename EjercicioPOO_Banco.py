# Práctica Clase 5
# Se debe modificar la clase CuentaBancaria para que sea abstracta , ademas los metodos extraer y depositar deben volverse abstractos,
# tambien se debe crear una clase CuentaAhorro que herede de CuentaBancaria y se le agregue un atributo privado de tasa de interes,
# el cual tendra un valor establecido de 0.001 y un metodo que nos calcule el interes.


import CuentaBancaria
import CuentaAhorro
import CuentaCorriente

cuenta1 = CuentaAhorro("Gabriel", 333333, "1990/02/03", 15000, 1)

print(cuenta1)

##print(cuenta1.obtener_edad())
