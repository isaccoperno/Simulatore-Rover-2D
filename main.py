import math

class Rover:
    def __init__(self, x, y, angolo_orientamento=0.0):
        self.x = float(x)
        self.y = float(y)
        self.angolo_orientamento = float(angolo_orientamento)  # In gradi (0-360)
        self.velocita_attuale = 0.0

    def sterza(self, delta_angolo):
        """Modifica l'angolo di orientamento aggiungendo un valore (in gradi)."""
        self.angolo_orientamento = (self.angolo_orientamento + delta_angolo) % 360
        print(f"-> Rover sterzato. Nuovo orientamento: {self.angolo_orientamento}°")

    def imposta_velocita(self, velocita):
        """Imposta la velocità di marcia del rover."""
        self.velocita_attuale = float(velocita)
        print(f"-> Velocità impostata a: {self.velocita_attuale} m/s")

    def aggiorna_posizione(self, tempo=1.0):
        """Aggiorna le coordinate x e y in base alla velocità, all'angolo e al tempo trascorso."""
        # Conversione dell'angolo da gradi a radianti per la trigonometria
        rad = math.radians(self.angolo_orientamento)
        
        # Calcolo dello spostamento lungo gli assi X e Y
        spostamento = self.velocita_attuale * tempo
        self.x += spostamento * math.cos(rad)
        self.y += spostamento * math.sin(rad)
        
        print(f"-> Posizione aggiornata: X = {self.x:.2f}, Y = {self.y:.2f}")

    def mostra_stato(self):
        """Stampa lo stato attuale del rover."""
        print(f"\n[STATO] X: {self.x:.2f} | Y: {self.y:.2f} | Orientamento: {self.angolo_orientamento}° | Velocità: {self.velocita_attuale}")


# Acquisizione dei dati iniziali dall'utente
x = float(input("Inserisci la posizione iniziale della x: "))
y = float(input("Inserisci la posizione iniziale della y: "))
angolo_iniziale = float(input("Inserisci l'angolo di orientamento iniziale (gradi): "))

# Creazione dell'istanza del rover
mio_rover = Rover(x, y, angolo_iniziale)
mio_rover.mostra_stato()

# Esempio di utilizzo dei comandi
print("\n--- Esempio di movimento ---")
mio_rover.imposta_velocita(5.0)  # Muovi a 5 m/s
mio_rover.aggiorna_posizione(2.0) # Muovi per 2 secondi
mio_rover.sterza(90)             # Sterza di 90 gradi a sinistra
mio_rover.aggiorna_posizione(1.0) # Muovi per un altro secondo
mio_rover.mostra_stato()