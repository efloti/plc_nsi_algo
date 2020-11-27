from algo.struct.liste_simple import Liste


class Pile1:
    """ Pile implémentée sur la base d'une liste chainée simple"""

    def __init__(self):
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


class Pile2:
    """ Pile implémentée sur la base d'une list python ordinaire. """

    def __init__(self):
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


class Pile3:
    """ Pile implémentée sur la base d'un tableau de taille fixe.
    Pour cela, on prend une list python mais on s'interdit les méthodes
    append et pop (voir notebook du cours).
    """

    def __init__(self, taille=2**10):
        self._liste = taille*[None]
        self._taille = 0
        pass

    def __len__(self):
        return self._taille
        pass

    def empiler(self, valeur):
        if self._taille == 2**10:
            return "Pile remplie!"
        self._liste[self._taille] = valeur
        self._taille += 1
        pass

    def depiler(self):
        if self._taille == 0:
            return "Pile vide!"
        r = self._liste[self._taille - 1]
        self._liste[self._taille - 1] = []
        self._taille -= 1
        return r
        pass

    def __str__(self):
        if self._taille == 0:
            return "Pile vide!"
        ch = ""
        i = self._taille
        while i > 0:
            ch += f"{self._liste[i]}\n"
            i -= 1
        return ch[:-1]
        pass
