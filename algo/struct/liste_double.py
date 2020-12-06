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
    def __init__(self, valeur):
        self.valeur = valeur
        self._precedente = None
        self._suivante = None


class ListeDbl:

    def __init__(self):
        self._tete = None
        self._queue = None
        self._taille = 0

    @property
    def tete(self):
        return self._tete

    @property
    def queue(self):
        return self._queue

    def __len__(self):
        return self._taille

    def __str__(self):
        val = self._tete
        afficher = []
        while val:
            afficher.append(val.valeur)
            val = val._suivante
        return str(afficher)

    def _inserer(self, valeur, cellule=None):
        """insere valeur juste après la cellule précisée
        Si elle n'est pas précisé, l'insertion a lieue en tête."""
        self._taille += 1
        cell = Cellule(valeur)

        # insertion en tête
        if cellule is None:
            cell._suivante = self._tete
            self._tete = cell
            # si la cellule est seule, elle est aussi la queue!
            if self._tete._suivante is None:
                self._queue = cell
            return

        # insertion queue
        if cellule._suivante is None:
            cellule._suivante = cell
            self._queue = cell
            return

        # insertion ailleurs
        cell._suivante = cellule._suivante
        cellule._suivante = cell


    def _supprimer(self, cellule):
        """Supprime la cellule indiquée et renvoie sa valeur"""



    def inserer(self, valeur, tete=True):
        """insertion en tete ou en queue si l'argument optionnel vaut False"""




    def supprimer(self, valeur, tete=True):
        """suppression en tete ou en queue si l'argument optionnel vaut False
        Renvoie la valeur de la cellule supprimée."""


    # on peut ajouter - bonus - d'autres méthodes utiles (voir liste simple)
