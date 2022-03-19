class Animal ():
    def __init__(self,nombre,peso):
        self.nombre = nombre
        self.peso = peso

    def saluda(self):
        return f"Guag, soy {self.nombre}"

    def caminar(self,pasos):
        self.pasos=pasos
        return f"Hoy di {self.pasos} pasitos"