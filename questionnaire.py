import json
# PROJET QUESTIONNAIRE V3 : POO
#
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement
#
# -> Définir les entitées (données, actions)
#
# Question
#    - titre       - str
#    - choix       - (str)
#    - bonne_reponse   - str
#
#    - poser()  -> bool
#
# Questionnaire
#    - questions      - (Question)
#
#    - lancer()
#

class Question:
    def __init__(self, titre, choix, bonne_reponse, numero=0):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse
        self.numero=numero

    # def FromData(data):
    #     for q_data in data["questions"]:
    #         for k,v in q_data["choix"].items():
    #             if v:
    #                 bonne_reponse = k
    #         q = Question(q_data["titre"], list(q_data["choix"].keys()), bonne_reponse)
    #     return q

    def poser(self):
        print(f"QUESTION {self.numero} :")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int-1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    def lancer(self):
        score = 0
        for question in self.questions:
            if question.poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score


"""questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

lancer_questionnaire(questionnaire)"""

# q1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
# q1.poser()

# data = (("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris", "Quelle est la capitale de la France ?")
# q = Question.FromData(data)
# print(q.__dict__)

# Questionnaire(
#     (
#     Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
#     Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
#     Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
#     )
# ).lancer()

def choose_file():
    JASON_DATA=[
        "animaux_leschats_confirme.json",
        "animaux_leschats_debutant.json",
        "animaux_leschats_expert.json",
        "arts_museedulouvre_confirme.json",
        "arts_museedulouvre_debutant.json",
        "arts_museedulouvre_expert.json",
        "cinema_alien_confirme.json",
        "cinema_alien_debutant.json",
        "cinema_alien_expert.json",
        "cinema_starwars_confirme.json",
        "cinema_starwars_debutant.json",
        "cinema_starwars_expert.json"
    ]
    print("LISTE DES FICHIERS DISPONIBLES :")
    for j in JASON_DATA:
        print(" -", j)
    try:
        json_data=input("Nom du fichier json de questionnaire à charger (ex: "+JASON_DATA[0]+") : ")
        if json_data not in JASON_DATA:
            print(f"ERREUR : Le fichier {json_data} n'est pas dans la liste des fichiers disponibles")
            return choose_file()
    except:
        print(f"ERREUR : Le fichier {json_data} n'existe pas")
        return choose_file()
    return json_data

json_data = choose_file()
with open(json_data, "r", encoding="utf-8") as json_file:
    data = json.load(json_file) 

questions_list = []
for idx, q_data in enumerate(data["questions"], start=1):
    for k,v in q_data["choix"]:
        if v:
            bonne_reponse = k
    q = Question(q_data["titre"], [ch[0] for ch in q_data["choix"]], bonne_reponse, idx)
    questions_list.append(q)
    
Questionnaire(questions_list).lancer()
