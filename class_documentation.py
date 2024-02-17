class Objet:
    """
    Les classes sont des manières simples de regrouper le code et les données liées à un objet.
    Elles rendent plus lisible le code et la maintenance plus facile.
    """

    def __init__(self, forme: str, couleur: str, masse: int):
        """
        Fonction qui définit les composantes à remplir du namedtuple Objet dans ce cas-ci.
        L'ajout d'un type hinting est possible pour chacune des composantes.
        """
        self.forme = forme
        self.couleur = couleur
        self.masse = masse

    def __str__(self):
        """
        :return: Retourne le string lorsque la fonction print() sera appelée.
        """
        return f"L'objet est {self.forme}, de couleur {self.couleur} et d'une masse de {self.masse} kg"


objet_un = Objet("Rond", "Rouge", 525)
print(objet_un)

