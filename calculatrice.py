def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        raise ValueError("Division par 0? Serieux?")
    return x / y

def calculatrice_v2():
    try:
        nombre1 = float(input("Entre le premier nombre : "))
        operation = input("Entre l'opération (+, -, *, /) : ")
        nombre2 = float(input("Entre le deuxième nombre : "))

        if operation == '+':
            resultat = addition(nombre1, nombre2)
        elif operation == '-':
            resultat = soustraction(nombre1, nombre2)
        elif operation == '*':
            resultat = multiplication(nombre1, nombre2)
        elif operation == '/':
            resultat = division(nombre1, nombre2)
        else:
            raise ValueError("Opération non valide, reveille toi..")

        print("Le résultat de {} {} {} est : {}".format(nombre1, operation, nombre2, resultat))

    except ValueError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Bonjour, une petite erreur est là pour vous: {e}")

calculatrice_v2()