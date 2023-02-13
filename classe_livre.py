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


    def _get_titre(self):
        return self._titre

    def _set_titre(self, v):
        self._titre = v
    Titre = property(_get_titre, _set_titre)
