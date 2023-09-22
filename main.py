import random

complexite = (1,2,3,4,5)
type_func = ("carré", "inverse", "racine", "affine", "composé")
type_calcul = ("dérivation", "développement", "factorisation", "addition", "multiplication", "soustraction")

def func(n):
    global type_calcul
    global complexite
    calc = []
    string = []
    for _ in range(n):
        type_calcul = random.choice(type_calcul)
        complexity = random.choice(complexite)
        if type_calcul == "addition":
            digit_per_num = int
            number_per_row = int
            if complexity == "1":
                digit_per_num = 2
                number_per_row = 2
                for num in range(number_per_row):
                    calc.append(f"{random.randint(1, 11)}{random.randint(1, 11)}")
            string.append(" + ".join(calc))