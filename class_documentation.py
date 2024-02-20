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

    def __repr__(self):
        """
        :return: Retourne le string lorsque la fonction print(repr()) sera appelée.
        """
        return f"Objet(\"{self.forme}\", \"{self.couleur}\", {self.masse})"

    def __int__(self):
        """
        :return: Retourne l'entier lorsque la fonction print(int()) sera appelée.
        """
        return self.masse ** 10  # On peut appliquer les opérations mathématiques désirées.

    def __float__(self):
        """
        :return: Retourne le nombre lorsque la fonction print(float()) sera appelée.
        """
        return self.masse / 453 + 1  # On peut appliquer les opérations mathématiques désirées.

    def __add__(self, other):
        """
        Attention, les deux éléments additionnés doivent provenir de la même classe.
        Attention, l'instance résultante doit posséder l'entièreté des composantes nécessaires par la fonction __init__
        :param other: Représente l'instance qui additionnera sa composante désirée à celle de l'instance.
        :return: Retourne une nouvelle instance avec, dans ce cas-ci, la nouvelle valeur associée à la masse
        """
        return Objet("Inconnue", "Inconnue", self.masse + other.masse)

    def __delete__(self, instance):

    def __del__(self):


class EnsembleObjet:
    def __init__(self, ensemble_alpha: list, ensemble_num: list):
        """
        Fonction qui définit les composantes à remplir de l'instance, Objet dans ce cas-ci.
        L'ajout d'un type hinting est possible pour chacune des composantes.
        """
        self.ensemble_alpha = ensemble_alpha
        self.ensemble_num = ensemble_num

    def __len__(self):
        """
        :return: Retourne le nombre d'éléments dans l'ensemble choisit.
        """
        return len(self.ensemble_alpha)  # On peut appliquer les opérations mathématiques désirées.

    def __contains__(self, item):
        """
        :param item: L'élément que nous souhaitons vérifier si la présence est vrai ou fausse.
        :return: True or False
        """
        return item in self.ensemble_alpha


# --------------------------------Class Objet-------------------------------------------
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

# __repr__
print(repr(objet_un))
print(repr(objet_deux))

# __int__
print(int(objet_un))
print(int(objet_deux))

# __float__
print(float(objet_un))
print(float(objet_deux))

# __add__
résultat_un = objet_un + objet_deux
print(résultat_un.masse)
print(résultat_un)


# -------------------------------Class EnsembleObjet-------------------------------------
# __init__
ensemble_un = EnsembleObjet(["a", "b", "c", "d", "e"], [1, 2, 3, 4, 5])
ensemble_deux = EnsembleObjet(["f", "g", "h", "i"], [6, 7, 8, 9])

# __len__
print(len(ensemble_un))
print(len(ensemble_deux))

# __contains__
print("a" in ensemble_un)
print(1 in ensemble_un)
print("a" in ensemble_deux)
print("f" in ensemble_deux)