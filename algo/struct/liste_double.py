"""
Une liste chaînée double est similaire à une liste simple à cela près que chaque cellule pointe
vers une suivante et aussi une précédente dans la chaîne (ou sur None aux bouts):
chercher des images sur internet.

L'intérêt est qu'on peut ajouter ou supprimer très rapidement O(1) une valeur
en début ou en fin de liste (pour implémenter par exemple une «file double»).

Note: pour une liste simple, il n'est pas possible de supprimer la dernière cellule
rapidement...
"""


class Cellule:
    pass


class ListeDbl:

    def __init__(self):
        pass

    @property
    def tete(self):
        pass

    @property
    def queue(self):
        pass

    def __len__(self):
        pass

    def __str__(self):
        pass

    def _inserer(self, valeur, cellule=None):
        """insere valeur juste après la cellule précisée
        Si elle n'est pas précisé, l'insertion a lieue en tête."""
        pass

    def _supprimer(self, cellule):
        """Supprime la cellule indiquée et renvoie sa valeur"""
        pass

    def inserer(self, valeur, tete=True):
        """insertion en tete ou en queue si l'argument optionnel vaut False"""
        pass

    def supprimer(self, valeur, tete=True):
        """suppression en tete ou en queue si l'argument optionnel vaut False
        Renvoie la valeur de la cellule supprimée."""
        pass

    # on peut ajouter - bonus - d'autres méthodes utiles (voir liste simple)
