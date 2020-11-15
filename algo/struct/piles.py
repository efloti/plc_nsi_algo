from algo.struct.liste_simple import Liste

class Pile1:
    """ Pile implémentée sur la base d'une liste chainée simple"""

    def __init__(self):
        self._liste = Liste()
        self._taille = 0

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
    """ Pile implémentée sur la base d'une list python """
    pass

class Pile3:
    """ Pile implémentée sur la base d'un tableau de taille fixe.
    Pour cela, on prend une list python mais on s'interdit les méthodes
    append et pop. 
    """
    def __init__(self, taille=1024):
        pass

    # etc
