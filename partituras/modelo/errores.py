class ErrorPartitura(Exception):
    pass

class ContieneNumero(ErrorPartitura):
    pass

class ContieneCaracterInvalido(ErrorPartitura):
    pass

class SinNotas(ErrorPartitura):
    pass

class EspacioMultiple(ErrorPartitura):
    pass

class EspacioBordes(ErrorPartitura):
    pass