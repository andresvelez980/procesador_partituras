from abc import ABC, abstractmethod

from partituras.modelo.errores import (
    ContieneNumero,
    ContieneCaracterInvalido,
    SinNotas,
    EspacioMultiple,
    EspacioBordes,
)

class ReglaTransformacion(ABC):

    def __init__(self, token: int):
        self.token = token

    @abstractmethod
    def transformar(self, partitura: str) -> str:
        pass

    @abstractmethod
    def revertir(self, partitura: str) -> str:
        pass

    @abstractmethod
    def partitura_valida(self, partitura: str) -> bool:
        pass

    def encontrar_numeros_partitura(self, partitura: str):
        return [
            (i, c)
            for i, c in enumerate(partitura)
            if c.isdigit()
        ]

    def encontrar_caracteres_invalidos(self, partitura: str):

        return [
            (i, c)
            for i, c in enumerate(partitura)
            if ord(c) > 127
        ]

class ReglaTransposicion(ReglaTransformacion):

    NOTAS = ["do", "re", "mi", "fa", "sol", "la", "si"]

    def partitura_valida(self, partitura: str) -> bool:

        errores = []

        numeros = self.encontrar_numeros_partitura(partitura)

        if numeros:
            mensaje = ", ".join(
                [f"{c} en posición {i}" for i, c in numeros]
            )

            errores.append(
                ContieneNumero(mensaje)
            )

        invalidos = self.encontrar_caracteres_invalidos(partitura)

        if invalidos:
            mensaje = ", ".join(
                [f"{c} en posición {i}" for i, c in invalidos]
            )

            errores.append(
                ContieneCaracterInvalido(mensaje)
            )

        partitura = partitura.lower()

        tokens = partitura.split()

        validos = self.NOTAS + ["|", "-"]

        for token in tokens:

            if token not in validos:

                errores.append(
                    ContieneCaracterInvalido(
                        f"Token inválido: {token}"
                    )
                )

        notas = [t for t in tokens if t in self.NOTAS]

        if not notas:
            errores.append(
                SinNotas("La partitura no contiene notas")
            )
        if errores:
            raise ExceptionGroup(
                "Errores de validación",
                errores
            )

        return True