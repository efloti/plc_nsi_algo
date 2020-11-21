"""
Une liste chaînée circulaire (simple ou double) a comme particularité de ne pas avoir de queue.
La «dernière» cellule a pour suivante celle de tête (si la liste n'est pas vide) et celle
de tete comme précédente la «dernière».

Traditionnellement, on utilise plutôt des cellules doubles (cf liste_double.py) pour les réaliser.

Une telle liste a la particularité de pouvoir être parcourue plusieurs fois simplement.

Exemple simpliste: imaginer que votre liste contienne `4 <-> 5 <-> 6`
vous souhaitez la parcourir en décrémentant chaque valeur d'une unité jusqu'à ce que l'une d'elle soit nulle...
"""


#  on peut ré-utiliser les cellules des listes doubles (décommenter... ou implémenter à nouveau cellule ici)
# from algo.struct.liste_double import Cellule

class ListeCirc:

    def __init__(self):
        pass

    @property
    def tete(self):
        pass

    def __len__(self):
        pass

    def __str__(self):
        pass

    def inserer(self, valeur):
        """insère valeur en tête et met à jour la tête de liste."""
        pass

    def supprimer(self):
        """supprimer la valeur en tête. Produit une IndexError si la liste est vide"""
        pass

    def avancer(self):
        """modifie la position du pointeur de tête d'une position «vers l'avant».
        N'a pas d'effet si la liste est vide."""
        pass

    def reculer(self):
        """modifie la position du pointeur de tête d'une position «vers l'arrière».
        N'a pas d'effet si la liste est vide."""
        pass

    def agir(self, actionfn, nb_tour=1):
        """parcours la liste entièrement autant de fois que l'indique `nb_tour`.
         À chaque itération, la valeur de la cellule courante est modifiée en utilisant la fonction `actionfn`.
         Cette fonction prend en argument une valeur et en renvoie une autre qui sert à actualiser la cellule.

         Ex: si `l` contient `*1 <-> 2 <-> 3` (`*` marque la tête) et qu'on a définit::

            def decrementer(x):
                return x - 1

         alors `l.agir(decrementer, 2)` modifie `l` de façon qu'elle contienne `*-1 <-> 0 <-> 1`.
         """
        pass

    def agir_nfois(self, actionfn, nfois):
        """Similaire à la méthode `.agir` mais `nfois` indique le nombre d'utilisation
        de la fonction `actionfn`. Le pointeur de tete est modifié en conséquence.

        Ex: Si une liste circulaire `l` contient `*1 <-> 2 <-> 3` (`*` marque la tête) et qu'on a définit::

            def decrementer(x):
                return x - 1

        alors `l.agir_nfois(decrementer, 5)` modifie `l` de façon qu'elle contienne `-1 <-> *0 <-> 2`
        ou, si l'on met toujours la cellule de tete en première position `*0 <-> 2 <-> -1`.
        """
        pass
