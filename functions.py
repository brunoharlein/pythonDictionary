dic_name = {
        "chien": "dog",
        "chat": "cat",
        "maison": "house",
        "rouge": "red",
        "voiture": "car",
        "un": "one",
        "deux": "two",
        "hélice": "propeller"
}

def dictionary(dic_name):
    """
    function that asks the user to enter a word to translate it.
    If the user types stop the program stops.
    """
    while 1:  # tant que 1 est True
        user = input("mot à traduire")  # user = le mot que la personne veut traduire
        if user == "stop":  # Si user == stop
            break  # Alors la boucle s'arrete
        try:  # essaie la variable "traduire" == mot dans le dictionaire "dico"
            traduire = dic_name[user]
        except:  # exception le mot n'existe pas dans le dictionnaire
            traduire = "je ne connais pas"

        print("résultat : {}".format(
            traduire))  # affiche le resultat de la variable "traduire" (mot du dictionnaire ou je ne sais pas)
