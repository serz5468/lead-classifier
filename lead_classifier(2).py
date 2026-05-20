leads = [ {'imie': "Kacper", 'budzet': 499},
       {'imie': "Anna", 'budzet': 698},
       {'imie': "Bartosz", 'budzet': 476},
       {'imie': "Kuba", 'budzet': 825},
       {'imie': "Oliwia", 'budzet': 655},
       {'imie': "Jagoda", 'budzet': 900},
       {'imie': "Marek", 'budzet': 303}
]
def classify_lead(budzet):
    if budzet < 500:
        return("COLD")
    elif 500 <= budzet <= 700:
        return("WARM")
    else:
        return("HOT")
while True:
 nowe_imie = input(f"Nowe dane dla listy:\nPodaj imie: ") 
 nowy_budzet = int(input(f'Podaj budzet: '))

 leads.append({
    'imie': nowe_imie,
    'budzet': nowy_budzet
})


 with open(r"C:\Users\user\Desktop\python\raport.txt", "a") as raport:
  for lead in leads:
    wynik = classify_lead(lead['budzet'])
    raport.write(f"{lead['imie']} {"->"} {wynik}\n")
 decyzja = input(f'Chcesz kontynuowac?: ')
 if decyzja == "nie":
    break

