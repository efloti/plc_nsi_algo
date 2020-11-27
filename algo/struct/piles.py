from algo.struct.liste_simple import Liste


class Pile1:
    """ Pile implémentée sur la base d'une liste chainée simple"""

    def __init__(self):
        self.__liste = Liste()

    def __len__(self):
        return len(self.__liste)

    def empiler(self, valeur):
        """ à faire """
        self.__liste._inserer_apres(valeur)

    def depiler(self):
        """ à faire """
        if len(self.__liste) == 0:
            raise IndexError("Pile vide!")
        return self.__liste._supprimer_apres()

    def __str__(self):
        return str(self.__liste)


class Pile2:
    """ Pile implémentée sur la base d'une list python ordinaire. """

    def __init__(self):
        self.__liste = []

    def __len__(self):
        return len(self.__liste)

    def sommet(self):
        return self.__liste[-1]

    def empiler(self, valeur):
        """ Ajoute la valeur à la fin de la liste """
        self.__liste.append(valeur)

    def depiler(self):
        """ Si la liste est vide on envoie une erreur,
         sinon on enlève la dernière valeur de la liste"""
        if len(self.__liste) == 0:
            raise IndexError("Pile vide !")
        return self.__liste.pop()

    def __str__(self):
        if len(self.__liste) == 0 :
            return "Pile vide !"
        ch = ""
        for v in self.__liste:
            ch += f"{v},"
        return ch[:-1]


class Pile3:
    """ Pile implémentée sur la base d'un tableau de taille fixe.
    Pour cela, on prend une list python mais on s'interdit les méthodes
    append et pop (voir notebook du cours).
    """

    def __init__(self, taille=2**10):
        pass

    def __len__(self):
        pass

    def empiler(self, valeur):
        """ à faire """
        pass

    def depiler(self):
        """ à faire """
        pass

    def __str__(self):
        pass
