from CuentaBancaria import CuentaBancaria


class CuentaAhorro(CuentaBancaria):
    def __init__(
        self, nombre_titular, dni_titular, fecha_nacimiento, saldo, tasa_interes=0.001
    ):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._tasa_interes = tasa_interes

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(
                f"Se ha depositado {monto} a la Cuenta de Ahorro del Titular: {self._nombre_titular} y su saldo es de : {self.obtener_saldo()}"
            )
        else:
            print("El monto a depositar debeser mayor a 0")

    def extraer(self, monto):
        if monto <= self.obtener_saldo():
            self._saldo -= monto
            print(
                f"Se ha extraido {monto} de la cuenta de {self._nombre_titular}, su saldo acutal es de: {self.obtener_saldo()}"
            )
        else:
            print("No posee saldo suficiente para esta operación")

    def obtener_tasa_interes(self):
        return self._tasa_interes

    def set_tasa_interes(self, monto):
        if monto > 0 and monto < 1:
            self._tasa_interes = monto
            print(
                f"Se ha depositado {monto} a la Cuenta de Ahorro del Titular: {self._nombre_titular} y su saldo es de : {self.obtener_saldo()}"
            )
        elif monto >= 1:
            self._tasa_interes = monto / 100
            print(
                f"Se ha depositado {monto} a la Cuenta de Ahorro del Titular: {self._nombre_titular} y su saldo es de : {self.obtener_saldo()}"
            )
        else:
            print("El monto de la tasa de interes debe ser mayor a 0")

    def calcular_interes_saldo(self):
        return self._saldo * self.obtener_tasa_interes()
