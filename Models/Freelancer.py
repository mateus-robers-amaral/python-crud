from Models.Funcionario import Funcionario
class FreeLancer(Funcionario):
    def __init__(self, codigo, nome, diasTrabalhados, valorDia):
        super().__init__(codigo, nome)
        self._diasTrabalhados = diasTrabalhados
        self._valorDia = valorDia                

    def get_diasTrabalhados(self):
        return self._diasTrabalhados

    def set_diasTrabalhados(self, diasTrabalhados):
        self._diasTrabalhados = diasTrabalhados

    def get_valorDia(self):
        return self._valorDia

    def set_valorDia(self, valorDia):
        self._valorDia = valorDia

    def calcularSalario(self):
        return self._valorDia * self._diasTrabalhados
