from views.form import Form


class PlayerForm(Form):
    def __init__(self):
        super().__init__(title="Ajouter un joueur",
                         fields=[("Nom", "last_name", str),
                                 ("Prénom", "first_name", str),
                                 ("année de naissance", "birth_year", int),
                                 ("mois de naissance", "birth_month", int),
                                 ("jour de naisance", "birth_day", int),
                                 ("sexe", "gender", str),
                                 ("classement", "rank", int)])