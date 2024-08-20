leiviska = int(input("Anna leiviskät: "))
naula = int(input("Anna naula: "))
luodit = float(input("Anna luodit: "))
print(f"Anna leiviskät\n{leiviska}")
print(f"Anna naula\n{naula}")
print(f"Anna luodit\n{luodit}")
grammoina = ((naula*32)+(leiviska*20*32)+(luodit))*13.3
kilogrammoina = int(grammoina/1000)
tulos1 = kilogrammoina
tulos2 = grammoina-(kilogrammoina)*1000
print(f"Massa nykymittojen mukaan:\n{tulos1} kilogrammaa ja {tulos2: .2f} grammaa.")