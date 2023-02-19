class Motor:

    def __init__(self,numeroCilindros:int,tipo:str,registro:int):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
        
    def cambiarRegistro(self, registro:int) -> None:
        self.registro = registro
    
    def asignarTipo(self, tipo:str) -> None:
        if tipo.lower() in ["electrico","gasolina"]:
            self.tipo = tipo 
        

#-------------------------------------------------------------------------        
    
    
class Asiento:
    
    def __init__(self,color:str,precio:int,registro:int):
        self.color = color
        self.precio = precio
        self.registro = registro
        
    def cambiarColor(self,color:str) -> None:
        allowColors = ["rojo","verde","amarillo","negro","blanco"]
        if color.lower() in allowColors:
            self.color = color
        
#-------------------------------------------------------------------------        


class Auto:
    CANTIDADCREADOS = 0
    
    def __init__(self,modelo:str,precio:int,asientos:list,marca:str,motor:Motor,registro:int):
        self.modelo = modelo
        self.precio = precio
        self.asientos =asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        
        
    def cantidadAsientos(self) -> int:
        con = 0 
        for i in range(len(self.asientos)):
            if (type(self.asientos[i]) == Asiento):
                con +=1
        return con
    
    def verificarIntegridad(self) -> str:
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        
        for i in range(len(self.asientos)):
            if self.asientos[i] != self.registro:
                return "Las piezas no son originales"
        
        return "Auto original"
    
        



        
        