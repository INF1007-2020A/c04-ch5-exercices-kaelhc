#!/usr/bin/env python
# -*- coding: utf-8 -*-


def convert_to_absolute(number: float) -> float:
    if number>0 :
       return  number
    return number*(-1)


def use_prefixes() -> list[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    word_liste=[]
    for i in prefixes :
     word_liste.append(i+suffixe)
    return word_liste

def find_premier (n)->bool :
    for nombre in range(2,n):
        if n%nombre== 0 :
            return False
    return True


def prime_integer_summation() -> int:
    liste12 = []
    n = 2
    while len(liste12) < 100:
        if find_premier(n):
            liste12.append(n)
        n += 1
    return sum(liste12)



def factorial(number: int) -> int:
    factorial_value = 1
    for i in range(2,number+1) :
        factorial_value*=i
    return factorial_value


def use_continue() -> None:
    for i in range(1,11) :
        if i ==5 :
            continue
        print(i)

def verify_ages(groups: list[list[int]]) -> list[bool]:
    verify=[]
    for groupe_i in groups :
        if len(groupe_i)>10 and len(groupe_i)<=3 :
            verify.append(False)
            continue
        elif 25 in groupe_i :
            verify.append(True)
            continue
        elif (min(groupe_i)<18 ) or (50 in groupe_i and max(groupe_i)>70) :
            verify.append(False)
            continue
        else :
            verify.append(True)
    return verify


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
