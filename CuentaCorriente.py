from CuentaBancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(
        self,
        nombre_titular,
        dni_titular,
        fecha_nacimiento,
        saldo=0,
        limite_extraccion=1000,
    ):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._limite_extraccion = limite_extraccion

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(
                f"Se ha depositado {monto} a la Cuenta Corriente del Titular: {self._nombre_titular} y su saldo es de : {self.obtener_saldo()}"
            )
        else:
            print("El monto a depositar en la cuenta corriente debe ser mayor a 0")

    def extraer(self, monto):
        if monto <= self.obtener_saldo() and monto <= self._limite_extraccion:
            self._saldo -= monto
        else:
            if monto > self._limite_extraccion:
                print("Usted no puede extraer ese monto de la cuenta corriente.")
            else:
                print(
                    "Usted no posee saldo suficiente en la cuenta corriente para realizar la operación."
                )
