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
            if complexity == "2":
                digit_per_num = 3
                number_per_row = 4
                for num in range(number_per_row):
                    calc.append(f"{random.randint(1, 11)}{random.randint(1, 11)}")
            if complexity == "3":
                digit_per_num = 4
                number_per_row = 4
                for num in range(number_per_row):
                    calc.append(f"{random.randint(1, 11)}{random.randint(1, 11)}")
            if complexity == "4":
                digit_per_num = 5
                number_per_row = 3
                for num in range(number_per_row):
                    calc.append(f"{random.randint(1, 11)}{random.randint(1, 11)}")
            if complexity == "5":
                digit_per_num = 6
                number_per_row = 2
                for num in range(number_per_row):
                    calc.append(f"{random.randint(1, 11)}{random.randint(1, 11)}")
            string.append(" + ".join(calc))
        if type_calcul == "soustraction":
            digit_per_num = int
            number_per_row = int
            if complexity == "1":
                digit_per_num = 2
                number_per_row = 2
                for num in range(number_per_row):
                    calc.append(f"{random.randint(1, 11)}{random.randint(1, 11)}")
            if complexity == "2":
                digit_per_num = 3
                number_per_row = 4
                for num in range(number_per_row):
                    calc.append(f"{random.randint(1, 11)}{random.randint(1, 11)}")
            if complexity == "3":
                digit_per_num = 4
                number_per_row = 4
                for num in range(number_per_row):
                    calc.append(f"{random.randint(1, 11)}{random.randint(1, 11)}")
            if complexity == "4":
                digit_per_num = 5
                number_per_row = 3
                for num in range(number_per_row):
                    calc.append(f"{random.randint(1, 11)}{random.randint(1, 11)}")
            if complexity == "5":
                digit_per_num = 6
                number_per_row = 2
                for num in range(number_per_row):
                    calc.append(f"{random.randint(1, 11)}{random.randint(1, 11)}")
            string.append(" - ".join(calc))