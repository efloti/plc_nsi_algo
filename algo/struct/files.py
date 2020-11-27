from algo.struct.liste_simple import Liste

class File1:
    """ File implémentée sur la base d'une liste chainée simple"""

    def __init__(self):
        """Création d'une file vide."""
        self.__liste = Liste()

    def __len__(self):
        """Renvoie la longueur de la file."""
        return len(self.___liste)

    def enfiler(self, valeur):
        """Enfile un objet au début de la file."""
        self.__liste.inserer_queue(valeur)

    def defiler(self):
        """Retire le premier objet de la file."""
        if len(self.__liste) == 0:
            raise IndexError("File vide !")
        else:
            self.__liste.supprimer_tete()

    def __str__(self):
        """Convertis la file en une chaîne de caractères."""
        chaine = ""
        longueur_file = len(self.__liste)
        for i in reversed(range(longueur_file)):
            if i == 0:
                chaine += f"{self.__liste[i]}"
            else:
                chaine += f"{self.__liste[i]} → "
        return chaine

    def __getitem__(self, index):
        """Renvoie l'objet demandé par rapport à son index."""
        return self.__liste.__getitem__(index)

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
        self.__tableau = [None]*taille
        self.__entree = 0
        self.__sortie = 0
        self.__est_pleine = False
        self.__longueur = 0

    def est_vide(self):
        return self.__longueur == 0

    def enfiler(self, valeur):
        if self.__est_pleine:
            raise IndexError("On ne peut pas ajouter de valeur à une file pleine")
        self.__tableau[self.__entree] = valeur
        self.__entree += 1
        if self.__entree >= len(self.__tableau):
            self.__entree = 0
        if self.__entree == self.__sortie:
            self.__est_pleine = True
        self.__longueur += 1

    def defiler(self):
        if self.est_vide():
            raise IndexError("On ne peut pas enlever une valeur à une file vide")
        if self.__est_pleine:
            self.__est_pleine = False
        self.__sortie += 1
        if self.__sortie >= len(self.__tableau):
            self.__sortie = 0
        self.__longueur -= 1
        return self.__tableau[self.__sortie - 1]

    def __len__(self):
        return self.__longueur

    def __str__(self):
        chaine = ""
        if self.__sortie < self.__entree:
            for i in range(self.__sortie, self.__entree - 1):
                chaine += f"{self.__tableau[self.__sortie + i]} -> "
            chaine += str(self.__tableau[self.__entree - 1])
        else:
            if not self.est_vide():
                for i in range(self.__sortie, len(self.__tableau)):
                    chaine += f"{self.__tableau[i]} -> "
                for i in range(self.__entree - 1):
                    chaine += f"{self.__tableau[i]} -> "
                chaine += str(self.__tableau[self.__entree - 1])
        return chaine