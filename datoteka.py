# -*- coding: utf-8 -*-

print("Dobrodošli v pretvorniku")

racun = "bla"

while racun != "ne":
    racun = raw_input("Želite pretvorite enote? (da/ne)")

    if racun == "da":
        print('Za pretvorbo dolžine, vpišite "dolzina"')
        print('Za pretvorbo teže, vpišite "teza"')
        pretvorba = raw_input("Kaj želite pretvoriti?")

        if pretvorba == "dolzina":
            print('Če želite pretvoriti centimetre v metre, vpišite: "cmvm"')
            print('Če želite pretvoriti centimetre v decimetre, vpišite "cmvdm"')
            print('Če želite pretvoriti decimetre v metre, vpišite "dmvm"')
            print('Če želite pretvoriti decimetre v centimetre, vpišite "dmvcm"')
            print('Če želite pretvoriti metre v decimetre, vpišite "mvdm"')
            print('Če želite pretvoriti metre v centimetre, vpišite "mvcm"')
            dolzina = raw_input("Kaj želite izračunati?")
            cifra = str(raw_input("Vpišite cifro, ki jo želite pretvoriti"))
            cifra = cifra.replace(",", ".")

            try:
                val = float(cifra)

                cifra = float(cifra)

                if dolzina == "cmvm":
                    cifra = str(cifra * 0.01)
                    print(cifra.replace(".", ",") + "m")
                elif dolzina == "cmvdm":
                    cifra = str(cifra * 0.1)
                    print(cifra.replace(".", ",") + "dm")
                elif dolzina == "dmvm":
                    cifra = str(cifra * 0.1)
                    print(cifra.replace(".", ",") + "m")
                elif dolzina == "dmvcm":
                    cifra = str(cifra * 10)
                    print(cifra.replace(".", ",") + "cm")
                elif dolzina == "mvdm":
                    cifra = str(cifra * 10)
                    print(cifra.replace(".", ",") + "dm")
                elif dolzina == "mvcm":
                    cifra = str(cifra * 100)
                    print(cifra.replace(".", ",") + "cm")
                else:
                    print("Error!")
                    print("Niste vpisali pravilne pretvorbe!")

            except ValueError:
                val = None
                print("Prosim, vpišite cifro")

        elif pretvorba == "teza":
            print('Če želite pretvoriti grame v kilograme, vpišite: "gvkg"')
            print('Če želite pretvoriti grame v dekagrame, vpišite "gvdag"')
            print('Če želite pretvoriti dekagrame v kilograme, vpišite "dagvkg"')
            print('Če želite pretvoriti dekagrame v grame, vpišite "dagvg"')
            print('Če želite pretvoriti kilograme v dekagrame, vpišite "kgvdag"')
            print('Če želite pretvoriti kilograme v grame, vpišite "kgvg"')
            teza = raw_input("Kaj želite izračunati?")
            cifra = str(raw_input("Vpišite cifro, ki jo želite pretvoriti"))
            cifra = cifra.replace(",", ".")

            try:
                val = float(cifra)

                cifra = float(cifra)

                if teza == "gvkg":
                    teza = str(cifra * 0.001)
                    print(teza.replace(".", ",") + "kg")
                elif teza == "gvdag":
                    teza = str(cifra * 0.1)
                    print(teza.replace(".", ",") + "dag")
                elif teza == "dagvkg":
                    teza = str(cifra * 0.01)
                    print(teza.replace(".", ",") + "kg")
                elif teza == "dagvg":
                    teza = str(cifra * 10)
                    print(teza.replace(".", ",") + "g")
                elif teza == "kgvdag":
                    teza = str(cifra * 100)
                    print(teza.replace(".", ",") + "dag")
                elif teza == "kgvg":
                    teza = str(cifra * 1000)
                    print(teza.replace(".", ",") + "g")
                else:
                    print("Error!")
                    print("Niste vpisali pravilne pretvorbe!")

            except ValueError:
                val = None
                print("Prosim, vpišite cifro")

        else:
            print("Error!")
            print("Niste vpisali pravilne pretvorbe!")

    elif racun == "ne":
        print("Hvala da ste uporabljali moj pretvornik enot")

    else:
        print('Prosim vpišite "da" ali "ne"')
