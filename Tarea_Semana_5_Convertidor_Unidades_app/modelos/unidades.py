# modelos/unidades.py
from abc import ABC, abstractmethod

class ConversorBase(ABC):
    # ABSTRACCIÓN: Clase abstracta que define la estructura básica de cualquier conversión
    def __init__(self, valor: float):
        # ENCAPSULAMIENTO: El atributo __valor es privado
        self.__valor = valor

    # Getter para acceder al valor privado
    def get_valor(self):
        return self.__valor

    @abstractmethod
    def convertir(self):
        #Método abstracto que las clases hijas deben implementar obligatoriamente
        pass

    @abstractmethod
    def obtener_simbolo(self):
        #Retorna el string del símbolo de la unidad resultante
        pass


class CelsiusAFahrenheit(ConversorBase):
    #HERENCIA: Hereda de ConversorBase. Realiza la conversión de temperatura
    def convertir(self) -> float:
        # Fórmula: (0 °C × 9/5) + 32 = 32 °F
        resultado = (self.get_valor() * 9/5) + 32
        return round(resultado, 2)

    def obtener_simbolo(self) -> str:
        return "°F"


class MetrosAPies(ConversorBase):
  #HERENCIA: Hereda de ConversorBase.Realiza la conversión de longitud.
   
    def convertir(self) -> float:
        # 1 metro = 3.28084 pies
        resultado = self.get_valor() * 3.28084
        return round(resultado, 2)

    def obtener_simbolo(self) -> str:
        return "ft"