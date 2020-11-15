from algo.struct.liste_simple import Liste

class File1:
    """ File implémentée sur la base d'une liste chainée simple"""

    def __init__(self):
        self._liste = Liste()
        self._taille = 0

    def __len__(self):
        pass

    def enfiler(self, valeur):
        """ à faire """
        pass

    def defiler(self):
        """ à faire """
        pass

    def __str__(self):
        pass

from collections import deque

class File2:
    """ File implémentée sur la base d'une deque (file double) python """


from algo.struct.piles import Pile1 as Pile

class File3:
    """ File implémentée sur la base de deux piles"""


class File4:
    """ File implémentée sur la base d'un tableau de taille fixe.
    Pour cela, on prend une list python mais on s'interdit les méthodes
    append, pop, insert. 
    """

    def __init__(self, taille=1024):
        pass

