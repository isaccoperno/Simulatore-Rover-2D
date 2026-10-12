class Rover:
    def __init__(self, x, y, angolo_orientamento):
        self.x = x
        self.y = y
        self.angolo_orientamento = angolo_orientamento

    def velocita(self):
        pass

    def sterza(self):
        pass

    def aggiorna_posizione(self):
        pass


x = int(input("Inserisci la posizione iniziale della x: "))
y = int(input("Inserisci la posizione iniziale della y: "))

rover = Rover(x, y, 45)


