# NSI-PLC: Algorithmique avec python

Travail collaboratif des élèves de terminale NSI au lycée Paul-Louis Courier de Tours.

## Présentation 

L'objectif est de développer, par un *travail collaboratif*, un **paquet** python regroupant toutes les structures algorithmiques et tous les algorithmes du programme de première/terminale NSI sous la forme de paquets/modules.

Celui-ci doit pouvoir s'installer «simplement» dans l'environnement de l'utilisateur via:

    pip install --user -i https://test.pypi.org/simple/ plc_nsi_algo
    
Une fois le paquet installé, on peut importer le **package** algo ainsi que ses sous-packages et/ou sous-modules comme suit:

    import algo # ou encore
    from algo.struct.liste_simple import Liste

Pour le désinstaller («nécessaire» pendant le développement - car il risque d'entrer en conflit avec les sources):

    pip uninstall plc_nsi_algo

## Outils utilisés

Outre **git** et **github** pour la collaboration,

1. **pytest** pour tester le code produit,

2. **TestPyPI** ([voir](https://test.pypi.org/) - [dépot pour ce paquet](https://test.pypi.org/project/plc-nsi-algo/)), un système de distribution de paquet python:
    - *Note*: pour celles et ceux qui voudraient savoir comment procéder pour «packager un projet», voir [ce tutoriel - packaging python project](https://packaging.python.org/tutorials/packaging-projects/)

3. (à venir) un outil de **documentation** automatique - sous la forme d'un site web - comme [sphinx](https://www.sphinx-doc.org/en/master/).

Bien sûr, il est encore utile de disposer d'un **outil d'édition** - comme [**Pycharm**](https://www.jetbrains.com/pycharm/) - qui intègre simplement les outils précédents. Comme le code ne dépend d'aucune interface graphique, il peut même être facilement réalisé (et testé) dans une interface du type **Jupyterlab**.

## Organisation

Le **package** python est situé dans le dossier *algo*; les tests dans le dossier **tests**.

L'enseignant produit une interface minimale pour chaque structure et/ou algorithme.

Chaque élève a réalisé un fork du dépôt dans son espace personnel. Il l'a ensuite cloné dans son espace de travail qu'il a configuré correctement de façon: 
- à pouvoir synchroniser sa branche *master* locale avec celle de ce dépôt (principal)
- à pouvoir pousser sa branche *contrib* sur son fork (nommé origin).

> Voir [cette vidéo sous windows 10 pour configurer son environnement de travail](https://vimeo.com/480681990) avec **pycharm** (et quelques indications pour visual studio).

Les élèves implémentent, sur cette base, les fonctions ou méthodes, les tests correspondants; ils produisent aussi les docstring et/ou commentaires appropriés.

Ils procèdent «par petit bout d'un seul tenant» (ex: une méthode, sa documentation, son test), à la fin duquel ils produisent un commit sur leur branche contrib.

Pour contribuer, ils poussent leur commit sur leur fork (de ce dépôt) puis envoie une PR - «pull request» via github.

## Pour faire fonctionner **pytest**

1. Commencer par l'installer sur votre ordinateur de travail:

        python -m pip install pytest # ou pip install pytest

2. Régler votre environnement:

   - **Pycharm**(conseillé): intègre presque tout automatiquement - [voir tout de même cette vidéo pour windows](https://vimeo.com/480681990).
   - **Jupyterhub**: On définit la variable d'environnement **PYTHONPATH** qui permet de préciser le chemin de recherche d'un paquet/module. Malheureusement, il faut le faire à chaque fois qu'on ouvre un terminal (mais voir note plus bas pour Jupyterhub):
    
        ```
        $ export PYTHONPATH=<chemin_absolu_du_depot_git_local>
        # on peut vérifier en lançant python
        $ python
        >>> import sys; print(sys.path) # liste les répertoire où python cherche les paquets/modules.
        >>> exit() # pour sortir de l'interpréteur.
        ```
   - **Visual Studio**: pas évident (mais la solution du jupyterhub fonctionne)

3. Si vous implémentez la fonction/méthode `<truc>` dans le module `algo.<mod>`, ajoutez une fonction `test_<truc>` dans le fichier `tests/test_<mod>.py`. Ne pas oublier d'importer la fonction `truc` ou la classe qui contient cette méthode si c'en est une.

   Pour des exemples, voir `tests/test_liste_simple.py`.

4. Lancer les tests:

    - **pycharm**: se fait par simple clic,
    - **jupyterhub** et **visual-studio**: utiliser la commande pytest dans un terminal.
    
**Note complémentaire pour jupyterhub ou pour git-bash sous windows**: Pour éviter de reconfigurer à chaque fois `PYTHONPATH`, il est possible d'ajouter les deux lignes qui suivent à la toute fin du fichier `~/.bashrc` (chargé de configurer le terminal lorsqu'il démarre):

    # Pour pytest avec plc_nsi_algo
    export PYTHONPATH=~/<chemin_vers_plc_nsi_alog_a_adapter>

Pour vérifier que lorsque le terminale redémarre, la variable est bien définie:

    $ echo $PYTHONPATH # devrait afficher le chemin du dépôt local

Il doit y avoir un mécanisme similaire pour Windows...