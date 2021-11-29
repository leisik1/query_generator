import random as rand


def adres_z_poczta(n):
    miasto = ['Warszawa', 'Krakow', 'Lodz', 'Poznan', 'Bogatki',
              'Olsztyn', 'Wroclaw', 'Bialystok', 'Szczytno']
    ulica = ['Lewandowskiego', 'Lenina', 'Sojki', 'Leningradzka', 'Dobra',
             'Dluga', 'Szeroka', 'Radnych', 'Prezydencka', 'Lisa', 'Sosenki']
    for i in range(n):
        wybrane_miasto = rand.choice(miasto)
        wybrana_uliaca = rand.choice(ulica)
        print(
            f"INSERT INTO Poczty (Kod_poczty, Poczta) VALUES('{str(rand.randint(0, 9))+str(rand.randint(0, 9))+'-'+str(rand.randint(0, 9))+str(rand.randint(0, 9)) + str(rand.randint(0, 9))}', '{wybrane_miasto}')")
        # Co robimy z tym numerem
        print(
            f"INSERT INTO Adresy (Miasto, Ulica, Nr_lokalu, Nr_poczty) VALUES('{wybrane_miasto}','{wybrana_uliaca}','{rand.randint(1,100)}', {i+1})")


def klient(n):
    imie = ['Adam', 'Marek', 'Bartosz', 'Monika', 'Anna', 'Kasia',
            'Alojzy', 'Beata', 'Karolina', 'Filip', 'Oliwia', 'Weronika']
    nazwisko = ['Kowal', 'Kasperek', 'Kisiel', 'Komnata', 'Doniczka',
                'Solniczka', 'Radziwil', 'Franco', 'Brando', 'Mussolini']
    plec = ['Mezczyzna', 'Kobieta']

    for i in range(n):
        wybrane_imie = rand.choice(imie)
        wybrane_nazwisko = rand.choice(nazwisko)
        wybrana_plec = rand.choice(plec)
        wybrany_mail = wybrane_imie+wybrane_nazwisko + \
            str(rand.randint(10, 90))+'@gmail.com'
        telefon = str(rand.randint(100, 999)) + \
            str(rand.randint(100, 999))+str(rand.randint(100, 999))
        print(
            f"INSERT INTO Klienci (Imie, Nazwisko, Plec, Email, Telefon, Nr_adresu) VALUES('{wybrane_imie}','{wybrane_nazwisko}','{wybrana_plec}','{wybrany_mail}','{telefon}',{i+1})")


def pracownicy(n):
    imie = ['Stefan', 'Karol', 'Jan', 'Maja', 'Martyna', 'Leokadia',
            'Marek', 'Jacek', 'Piotr', 'Franciszek', 'Julka', 'Aneta', 'Anastazja']
    nazwisko = ['Drzewo', 'Wilk', 'Cygan', 'Mop', 'Szyba',
                'Solniczka', 'Schmidt', 'Mol', 'Brando', 'Mussolini']
    plec = ['Mezczyzna', 'Kobieta']
    miesiac = ['JAN', 'FEB', 'MAR', 'APR', 'MAY',
               'JUN', 'JUL', 'AUG', 'SEP', 'NOV', 'DEC']

    for i in range(n):
        wybrane_imie = rand.choice(imie)
        wybrane_nazwisko = rand.choice(nazwisko)
        data_ur = str(rand.randint(10, 28)) + '-' + \
            rand.choice(miesiac) + '-' + str(rand.randint(1950, 2000))
        pesel = str(rand.randint(1000, 9999) +
                    rand.randint(1000, 9999)+rand.randint(100, 999))
        numer_konta = str(rand.randint(
            10000, 99999)+rand.randint(10000, 99999)+rand.randint(1000, 9999))
        data_zatr = str(rand.randint(10, 28)) + '-' + \
            rand.choice(miesiac) + '-' + str(rand.randint(2000, 2020))

        stanowisko = rand.randint(1, 4)

        print(
            f"INSERT INTO Pracownicy (Imie, Nazwisko, Data_urodzenia, Pesel, Numer_konta, Data_zatrudnienia, Nr_osrodka, Nr_adresu, Nr_stanowiska) VALUES('{wybrane_imie}','{wybrane_nazwisko}','{data_ur}','{pesel}','{numer_konta}','{data_zatr}', 1, {i+21}, {stanowisko})")


def sesje(n):
    nazwa = ['Orientalny poranek', 'Fiki miki', 'Rajski wieczor', 'Wachlarz wrazen', 'Sosnowy zagajnik',
             'Kwiatowa polana', 'Aromatyczne przyprawy', 'Olbasowy strzal', 'Jurtowy klimat']
    nr_osrodak = 1

    for i in range(n):
        nazwa_wybrana = rand.choice(nazwa)
        liczba_minut = rand.randint(30, 120)
        print(
            f"INSERT INTO Sesje (Nazwa_sesji, Liczba_minut, Opis_sesji, Nr_osrodka) VALUES('{nazwa_wybrana}','{liczba_minut}','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi quis sem a justo fringilla varius. Aliquam lacinia dolor lacus, eu rhoncus sem sagittis viverra. Nunc varius et quam venenatis aliquam.',{nr_osrodak})")


def sauny(n):
    typ_sauny = ['Finska', 'Rzymska', 'Mokra', 'Na_podczerwien', 'Inny']
    aromat = ['olbas', 'gozdzikowy', 'lawenda', 'sandalowiec', 'amol',
              'jalowiec', 'sosna', 'india', 'herbaciany', 'eukaliptus', 'cedr']
    nr_osrodak = 1
    for i in range(n):
        temperatura = round(rand.random()*100, 1)
        wyb_typ_sauny = rand.choice(typ_sauny)
        l_osob = rand.randint(3, 15)
        wyb_aromat = rand.choice(aromat)
        print(
            f"INSERT INTO Sauny (Temperatura, Typ_sauny, Liczba_osob, Aromat, Nr_osrodka) VALUES('{temperatura}','{wyb_typ_sauny}','{l_osob}','{wyb_aromat}',{nr_osrodak})")


def stanowiska(n):
    nazwa = ['Recepcjonista', 'Technik', 'Ksiegowa', 'Fizjoterapeuta']
    opis = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi quis sem a justo fringilla varius. Aliquam lacinia dolor lacus, eu rhoncus sem sagittis viverra. Nunc varius et quam venenatis aliquam.'
    for naz in nazwa:
        print(
            f"INSERT INTO Sauny (Nazwa_stanowiska, Opis_stanowiska) VALUES('{naz}'', '{opis}')")


def karty(n):
    miesiac = ['JAN', 'FEB', 'MAR', 'APR', 'MAY',
               'JUN', 'JUL', 'AUG', 'SEP', 'NOV', 'DEC']
    akt = ['Y', 'N']
    for i in range(n):
        wazny_od = str(rand.randint(10, 28)) + '-' + \
            rand.choice(miesiac) + '-' + str(rand.randint(2018, 2019))
        wazny_do = str(rand.randint(10, 28)) + '-' + \
            rand.choice(miesiac) + '-' + str(rand.randint(2020, 2021))
        l_sesji = rand.randint(2, 45)
        aktywnosc = rand.choice(akt)
        rabat = round(rand.randint(20, 50))
        print(
            f"INSERT INTO Karty (Pozostala_liczba_sesji, Wazny_od, Wazny_do, Rabat, Czy_aktywna, Nr_osrodka, Nr_klienta) VALUES({l_sesji}, TO_DATE({wazny_od}), TO_DATE({wazny_do}), {rabat}, '{aktywnosc}', 1, {i+1} );")


def wynagrodzenia(n):
    miesiac = ['JAN', 'FEB', 'MAR', 'APR', 'MAY',
               'JUN', 'JUL', 'AUG', 'SEP', 'NOV', 'DEC']
    for i in range(n):
        podstawa = rand.randint(2800, 3200)
        dodatek = rand.randint(500, 800)
        data = str(rand.randint(10, 28)) + '-' + \
            rand.choice(miesiac) + '-' + str(rand.randint(2020, 2021))

        print(
            f"INSERT INTO Wynagrodzenia (Kwota_podstawowa, Kwota_dodatkowa, Data_wyplacenia, Nr_pracownika) VALUES({podstawa}, {dodatek}, TO_DATE({data}), {i+1} );")


def technicy(n):
    miesiac = ['JAN', 'FEB', 'MAR', 'APR', 'MAY',
               'JUN', 'JUL', 'AUG', 'SEP', 'NOV', 'DEC']
    for i in range(n):
        nr_licencji = int(str(rand.randint(
            2800, 3200)) + str(rand.randint(1000, 9999)) + str(rand.randint(1000, 9999)))
        dodatek = rand.randint(500, 800)
        data = str(rand.randint(10, 28)) + '-' + \
            rand.choice(miesiac) + '-' + str(rand.randint(2022, 2023))

        print(
            f"INSERT INTO Technicy (Nr_pracownika, Nr_licencji, Data_wygasniecia) VALUES(NUMER , {nr_licencji}, TO_DATE({data}), {i+1} );")


def fizjoterapeuci(n):
    miesiac = ['JAN', 'FEB', 'MAR', 'APR', 'MAY',
               'JUN', 'JUL', 'AUG', 'SEP', 'NOV', 'DEC']
    for i in range(n):
        nr_licencji = int(str(rand.randint(
            2800, 3200)) + str(rand.randint(1000, 9999)) + str(rand.randint(1000, 9999)))
        dodatek = rand.randint(500, 800)
        data = str(rand.randint(10, 28)) + '-' + \
            rand.choice(miesiac) + '-' + str(rand.randint(2022, 2023))

        print(
            f"INSERT INTO Technicy (Nr_pracownika, Specjalizacja, Nr_licencji) VALUES(NUMER , {nr_licencji}, TO_DATE({data}), {i+1} );")
