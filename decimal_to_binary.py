def valeur_binaire(n):
    if n > 1:
        valeur_binaire(n // 2)
    print(n % 2, end='')

entier = int(input("Entrez un nombre entier: "))

valeur_binaire(entier)