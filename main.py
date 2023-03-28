import bil

looping=True
Bmw_svart = bil.bil("Bmw", "svart", 3 )
merca_gul = bil.bil("merca", "gul", 6)
ferrari_röd = bil.bil("ferrari", "röd", 20)
toyota_blå = bil.bil("toyota", "blå", 7)

billista = [Bmw_svart, merca_gul, ferrari_röd, toyota_blå]

print(Bmw_svart.getfabrikat())


while looping:

    i= 0

    for bil in billista:
         print(str(i+1) + "fabrikat: " + bil.fabrikat +" Färg " + bil.color)
         i += 1 
               

    bil_nr = input("\nMata in bil nummer för vald bil: ")

    print("\n En" + billista[int(bil_nr) -1].fabrikat+ ", färg: " + billista[int(bil_nr) - 1].color)

    svar_anvandare = input("vill du avsluta programmet? j/n : ")

    if (svar_anvandare == "j"):
        break
