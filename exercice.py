#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number>0 :
       return  number

    return number*(-1)


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    word_liste=[]
    for i in prefixes :
     word_liste.append(i+suffixe)
    return word_liste


def prime_integer_summation() -> int:
    pass



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

def verify_ages(groups: List[List[int]]) -> List[bool]:
    verify=[]
    under_groups=[]
    for numero_groupe in groups :
        if len(numero_groupe) > 10 or len(numero_groupe) <= 3:
            verify.append("false")
        else :
        for condition in groups[len(numero_groupe)] :
         if condition == 25 :
             verify.append("true")
          elif condition<18 :
            verify.append("false")
         elif condition >70 :
          verify.append("false")

        else : verify.append("true")

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
