import sys

class quiz():

    questions_choisies = ["Combien de fois la France a gagné la coupe du monde ? ", "Quand a été fondé Apple ? ", "Qui a fondé SpaceX ? "]
    reponses_choisies = ["2", "1976", "Elon Musk"]
    nb_vie_choisi = 3

    #Initialisation des variables
    def __init__(self, questions = questions_choisies, reponses = reponses_choisies, nb_vie = nb_vie_choisi):
        self.question = questions
        self.reponse = reponses
        self.nb_vie = nb_vie
    
    #Poser la question et obtenir la réponse de l'utilisateur
    def get_answer(self, question_number):
        reponse = input(self.question[question_number])
        return reponse

    #Vérifier la réponse par rapport à la question posée
    def ask_question(self, question_number):
        correct_answer = self.reponse[question_number]
        
        answer = self.get_answer(question_number)
        
        if answer == correct_answer:
            print("⭐ Bien joué, prochaine question ! ⭐")

        while answer != correct_answer:
            self.nb_vie -= 1
            print("Dommage ! Il te reste {} chances".format(self.nb_vie), "\n Essayez encore !!!")
            if self.nb_vie == 0:
                print("Oh non ! Tu as perdu le jeu...")
                sys.exit("Le jeu est terminé. Vous avez perdu :( \n Veuillez relancer le programme pour recommencer le Quiz, Bonne chance à vous 😁")
            answer = self.get_answer(question_number)
            if answer == correct_answer:
                print("⭐ Bien joué, prochaine question ! ⭐")

        return self.nb_vie
  
    #Fonction permettant de faire tourner l'entièreté du quiz             
    def run_quiz(self):
        # Process (main loop)
        for i in range(len(self.question)):
            self.ask_question(i)
        
        if self.nb_vie > 0:
            return print("Bravo ! Tu as gagné le quiz !")
            
#Pour lancer le quiz directement en démarrant la cellule.
if __name__ == "__main__":
    quiz().run_quiz()
