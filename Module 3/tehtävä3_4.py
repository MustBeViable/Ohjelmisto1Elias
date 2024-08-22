vuosi = int(input("Anna vuosiluku: "))
if vuosi % 4 == 0:
    if vuosi % 100 != 0:
        print("Antamasi vuosi on karkausvuosi.")
    elif vuosi % 100 == 0:
        if vuosi % 400 == 0:
            print("Antamasi vuosi on karkausvuosi.")
        else:
            print("Antamasi vuosi ei ole karkausvuosi.")
else:
    print("Antamasi vuosi ei ole karkausvuosi.")