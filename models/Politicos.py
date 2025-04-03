class Politico:
    def __init__(self, id: int, valor_a_robar: int, edad: int):
        self._id = id
        self._valor_robo = valor_a_robar
        self._edad = edad
        
    @property
    def valor_robo(self):
        return self._valor_robo
    
    @property
    def id(self):
        return self._id
    
    @property
    def edad(self):
        return self._edad
    
    @id.setter
    def id(self, id: int):
        self._id = id
    
    @valor_robo.setter
    def valor_robo(self, valor_robo: int):
        self._valor_robo = valor_robo
        
    @edad.setter
    def edad(self, edad: int):
        self._edad = edad
    
    def __str__(self):
        return f"{self._id}  ||  {self._edad}  ||  {self._valor_robo}"
    
        
    