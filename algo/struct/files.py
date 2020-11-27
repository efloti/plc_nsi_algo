class File1:
    """ File implémentée sur la base d'une liste chainée simple"""
    from algo.struct.liste_simple import Liste

    def __init__(self):
        pass

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


class File2:
    """ File implémentée sur la base d'une deque (file double) python """
    from collections import deque

    def __init__(self):
        pass

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


class File3:
    """ File implémentée sur la base de deux piles."""

    def __init__(self):
        from algo.struct.piles import Pile1 as Pile
        self._entree = Pile()
        self._sortie = Pile()

    def __len__(self):
        return len(self._entree) + len(self._sortie)

    def enfiler(self, valeur):
        """ à faire """
        self._entree.empiler(valeur)

    def defiler(self):
        """ à faire """
        if len(self) == 0:
            raise IndexError("File vide")
        
        if len(self._sortie):
            return self._sortie.depiler()

        long = len(self._entree)

        if long == 1:
            return self._entree.depiler()
        
        for _ in range(long-1):
            self._sortie.empiler(self._entree.depiler())

        return self._entree.depiler()

    def copy(self):
        for _ in range(len(self._sortie)):
            self._entree.empiler(self._sortie.depiler())
        result = File3()
        result._entree = self._entree
        return result

    def __str__(self):
        for _ in range(len(self._sortie)):
            self._entree.empiler(self._sortie.depiler())
        return str(self._entree)

    def __eq__(self, other):
        return str(self) == str(other)


class File4:
    """ File implémentée sur la base d'un tableau de taille fixe.
    Pour cela, on prend une list python mais on s'interdit les méthodes
    append, pop, insert. 
    """

    def __init__(self, taille=1024):
        pass
