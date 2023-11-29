historique = []

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

def afficher_historique():
    if historique:
        print("Historique des calculs :")
        for calcul in historique:
            print(calcul)
    else:
        print("Aucun calcul dans l'historique.")

def effacer_historique():
    historique.clear()
    print("L'historique a été effacé.")

while True:
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

        calcul = f"{nombre1} {operation} {nombre2} = {resultat}"
        historique.append(calcul)

        print(f"Le résultat de {nombre1} {operation} {nombre2} est : {resultat}")

        afficher_historique()

        reponse_effacer = input("Voulez-vous effacer l'historique? (oui/non): ")
        if reponse_effacer.lower() == "oui":
            effacer_historique()

        continuer = input("Voulez-vous faire un autre calcul? (oui/non): ")
        if continuer.lower() != "oui":
            break

    except ValueError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Bonjour, une petite erreur est là pour vous : {e}")