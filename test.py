from form import Form
from menu import Menu

# view = View(title="title 1",
#             content= "content1")
# print(view.show())

# Menu(title="Bienvenue sur chess manager version 1.0",
#      options=["Gérer les joueurs", "Gérer les tournois"]).show()

print(Form(title="Ajouter un joueur", fields=["Nom",
                                        "prénom",
                                        "annee de naissance",
                                        "mois de naissance",
                                        "jour de naissance",
                                        "sexe",
                                        "classement"]).show())