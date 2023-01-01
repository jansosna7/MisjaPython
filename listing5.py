planety = {"Merkury": ["Najmniejsza planeta, najbliżej Słońca", False, 0],
           "Wenus": ["Obrót planety Wenus zajmuje 243 dni", False, 0],
           "Ziemia": ["Jedyna planeta, na której rozwineło się życie", False, 1],
           "Mars": ["Czerwona planeta to druga po Merkurym najmniejsz planeta", False, 2],
           "Jowisz": ["Najwięksa planeta jest gazowym olbrzymem", True, 67],
           "Saturn": ["Gazowy olbrzym, drugi pod względem wielkości", True, 62],
           "Uran": ["Lodowy olbrzym z systemem pierścieni", True, 27],
           "Neptun": ["Lodowy olbrzym i najdalej od Słońca", True, 14],
           "Pluton": ["Największa planeta karłowata w Układzie Słonecznym", False, 5]
           }

while True:
    pyanie = input("Która planeta Cię interesuje ?")
    if pyanie in planety.keys():
        print(planety[pyanie][0])
        print("czy ma pierścienie? ", planety[pyanie][1])
    else:
        print("Brak danych")
