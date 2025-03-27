# Exemple : Système complet avec 2 cartouches
class SystemeAudio:
    def __init__(self):
        self.cartouches = {}  # Dictionnaire des cartouches
    
    def ajouter_cartouche(self, id_cartouche):
        self.cartouches[id_cartouche] = CartoucheVLC()
    
    def jouer_cartouche(self, id_cartouche, fichier):
        self.cartouches[id_cartouche].play(fichier)

# Utilisation
systeme = SystemeAudio()
systeme.ajouter_cartouche("fond_sonore")
systeme.ajouter_cartouche("jingles")
systeme.jouer_cartouche("fond_sonore", "ambiance.mp3")
