"""
Gra Kamien, papier, nozyce
"""

import sys
import random
import time

gramy = (input("Witaj w grze kamien-papier-nozyce"
               " Czy chcesz zagrać??? (t/n):\n"))
if gramy.lower() == "n":
    print("Moze nastepnym razem sprobujesz ;D")
    sys.exit(0)

print("W kazdym momencie mozesz przerwac klikajac '0'")

while True:
    print()
    wybor = int(input("Wybierasz:\n1.Papier\n2.Kamień\n3.Nożyce\n"))
    wybor_komputer = random.randrange(1, 3)

    if wybor == 0:
        sys.exit(0)

    if wybor == 1 and wybor_komputer == 1:
        print("Papier vs Papier")
        time.sleep(1)
        print("Remis")
    elif wybor == 2 and wybor_komputer == 2:
        print("Kamień vs Kamień")
        time.sleep(1)
        print("Remis")
    elif wybor == 3 and wybor_komputer == 3:
        print("Nożyce vs Nożyce")
        time.sleep(1)
        print("Remis")
    if wybor == 1 and wybor_komputer == 2:
        print("Papier vs Kamień")
        time.sleep(1)
        print("Wygrywasz")
    elif wybor == 2 and wybor_komputer == 3:
        print("Kamień vs Nożyce")
        time.sleep(1)
        print("Wygrywasz")
    elif wybor == 3 and wybor_komputer == 1:
        print("Nożyce vs Papier")
        time.sleep(1)
        print("Wygrywasz")
    if wybor == 1 and wybor_komputer == 3:
        print("Papier vs Nożyce")
        time.sleep(1)
        print("Przegrywasz")
    elif wybor == 2 and wybor_komputer == 1:
        print("Kamień vs Papier")
        time.sleep(1)
        print("Przegrywasz")
    elif wybor == 3 and wybor_komputer == 2:
        print("Nożyce vs Kamień")
        time.sleep(1)
        print("Przegrywasz")

    print()
    input("Wciśnij dowolny przycisk żeby grać dalej\n")