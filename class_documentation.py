class Objet:
    """
    Les classes sont des manières simples de regrouper le code et les données liées à un objet.
    Elles rendent plus lisible le code et la maintenance plus facile.
    """

    def __init__(self, forme: str, couleur: str, masse: int):
        """
        Fonction qui définit les composantes à remplir de l'instance, Objet dans ce cas-ci.
        L'ajout d'un type hinting est possible pour chacune des composantes.
        """
        self.forme = forme  # Permettra dorénavant l'utilisation de, exemple, forme_objet = objet.forme
        self.couleur = couleur  # Permettra dorénavant l'utilisation de, exemple, couleur_objet = objet.couleur
        self.masse = masse  # Permettra dorénavant l'utilisation de, exemple, masse_objet = objet.masse
        # Et ce, même en dehors de la classe

    def __str__(self):
        """
        :return: Retourne le string lorsque la fonction print() sera appelée.
        """
        return f"L'objet est {self.forme}, de couleur {self.couleur} et d'une masse de {self.masse} kg"

    def __eq__(self, other):
        """
        Fonction qui détermine les composantes de l'instance qui seront regardées lors d'une comparaison
        avec l'opérateur ==.
        :param other: Ce avec quoi l'instance, dans ce cas-ci Objet, sera comparée.
        :return: True or False
        """
        if isinstance(other,
                      Objet):  # L'opérateur isinstance sert à vérifier si la comparaison se fait entre deux
            # instances de la même classe.
            return self.forme == other.forme and self.masse == other.masse  # Ne regardera jamais si la couleur des
            # éléments est la même ou non.
        return False


# __init__
objet_un = Objet("Rond", "Rouge", 525)
objet_deux = Objet("Rond", "Bleu", 110)

# __str__
print(objet_un)
print(objet_deux)

# __eq__
print(objet_un == objet_deux)
objet_deux.masse = 525
print(objet_un)
print(objet_deux)
print(objet_un == objet_deux)
print(objet_un == 1)
