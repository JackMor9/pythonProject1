class Livre:
    """
    Classe livre
    """
    def __init__(self, p_titre = "", p_auteur = "", p_prix = 0):
        """
        Constructeur de la classe livre
        :param p_titre: titre du livre
        :param p_auteur: auteur du livre
        :param p_prix: prix du livre
        """

        self._titre = p_titre
        self._auteur = p_auteur
        self._prix = p_prix

#propriété titre
    def _get_titre(self):
        return self._titre

    def _set_titre(self, v):
        self._titre = v
    Titre = property(_get_titre, _set_titre)
#propriété auteur

    def _get_auteur(self):
        return self._auteur

    def _set_auteur(self, v):
        self._auteur = v
    Auteur = property(_get_auteur, _set_auteur)
#propriété prix
    def _get_prix(self):
        return self._prix

    def _set_prix(self, v):
        self._prix = v
    Prix = property(_get_prix, _set_prix)


#AFFICHER

