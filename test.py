from view import View


view = View(title="Bienvenue sur chess manager version 1.0",
            content=["Gérer les joueurs", "Gérer les tournois"])

print(view.show())