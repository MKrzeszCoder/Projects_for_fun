import random
print("A teraz zagrajmy w kamień papier nożyce:)")
while True:
    print("podaj swoj wybor (nożyce,kamień,papier):")
    wybor=str(input())
    wybor2=random.choice(["nożyce","kamień","papier"])
    print(wybor2)
    if(wybor=="nożyce"):
        if wybor2=="nożyce":
            print("REMIS!")
        elif wybor2=="kamień":
            print("niestety przegrałeś :(")
        else:
            print("EKSTRA Wygrałeś!!!!")

    elif wybor=="kamień":
        if wybor2 == "kamień":
            print("REMIS!")
        elif wybor2 == "nożyce":
            print("EKSTRA Wygrałeś!!!!")
        else:
            print("niestety przegrałeś :(")
    elif wybor=="papier":
        if wybor2 == "kamień":
            print("EKSTRA Wygrałeś!!!!")
        elif wybor2 == "nożyce":
            print("niestety przegrałeś :(")
        else:
            print("REMIS!")
    else:
        print("oj niestety nie ma takiego wyboru spróbuj jeszcze raz!")
        continue
    print("gramy jeszcze raz?")
    one=input("YES/NO\n")
    if one=="NO":
        break
