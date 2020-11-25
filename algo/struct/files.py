from algo.struct.liste_simple import Liste

class File1:
    """ File implémentée sur la base d'une liste chainée simple"""

    def __init__(self):
        """Création d'une file vide."""
        self.file = Liste()

    def __len__(self):
        """Renvoie la longueur de la file."""
        return len(self.file)

    def enfiler(self, valeur):
        """Enfile un objet à la fin de la file."""
        self.file.inserer_queue(valeur)

    def defiler(self):
        """Retire le premier objet de la file."""
        self.file.supprimer_tete()

    def __str__(self):
        """Convertis la file en une chaîne de caractères."""
        return self.file.__str__()

    def __getitem__(self, index):
        """Renvoie l'objet demandé par rapport à son index."""
        return self.file.__getitem__(index)

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
    from algo.struct.piles import Pile1 as Pile

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


class File4:
    """ File implémentée sur la base d'un tableau de taille fixe.
    Pour cela, on prend une list python mais on s'interdit les méthodes
    append, pop, insert. 
    """

    def __init__(self, taille=1024):
        pass
