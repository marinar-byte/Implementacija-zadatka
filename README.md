# **Parcijalni Ispit - Razvoj Web Aplikacija u Programskom Jeziku Python**

## **Upute za Rješavanje Zadatka**

### 1. **Priprema okruženja**
- Forkajte repozitorij na GitHubu:
  - Posjetite [GitHub repozitorij projekta](https://github.com/algebra-pydev/parcijalni-ispit-04-razvoj-web-aplikacija-u-programskom-jeziku-python).
  - Kliknite na gumb **"Fork"** kako biste stvorili vlastitu kopiju repozitorija.
- Dodijelite repozitoriju naziv u formatu `pydev_parcijalni_ime_prezime` (npr. `pydev_parcijalni_ana_kovačić`).
- **VAŽNO:** Nemojte raditi **clone** glavnog repozitorija jer nemate pravo mijenjanja originalnog koda.

---

### 2. **Postavljanje projekta**
#### Struktura projekta:
```
offers_calculator/            # Glavni direktorij Django projekta
│
├── db.sqlite3                # SQLite baza podataka
│
├── offers_calculator/        # Direktorij glavnih postavki projekta
│   ├── __init__.py           # Oznaka za Python paket
│   ├── asgi.py               # Konfiguracija za ASGI server
│   ├── settings.py           # Postavke projekta
│   ├── urls.py               # Globalne rute aplikacije
│   ├── wsgi.py               # Konfiguracija za WSGI server
│   └── manage.py             # Glavna skripta za upravljanje projektom
│
├── accounts/                 # Aplikacija za upravljanje korisnicima (Django User model)
│   ├── __init__.py
│   ├── admin.py              # Registracija modela u admin sučelju
│   ├── apps.py               # Konfiguracija aplikacije
│   ├── models.py             # Modeli za korisnike
│   ├── serializers.py        # Serializacija podataka za REST API (opcionalno)
│   ├── urls.py               # Rute aplikacije za korisnike
│   ├── views.py              # Pogledi za korisnike
│   └── migrations/           # Migracije baze podataka
│       └── __init__.py
│
├── products/                 # Aplikacija za upravljanje proizvodima
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # Modeli za proizvode
│   ├── serializers.py        # Serializacija podataka za REST API (opcionalno)
│   ├── urls.py               # Rute aplikacije za proizvode
│   ├── views.py              # Pogledi za proizvode
│   └── migrations/
│       └── __init__.py
│
├── offers/                   # Aplikacija za upravljanje ponudama
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # Modeli za ponude
│   ├── serializers.py        # Serializacija podataka za REST API (opcionalno)
│   ├── urls.py               # Rute aplikacije za ponude
│   ├── views.py              # Pogledi za ponude
│   └── migrations/
│       └── __init__.py
│
├── scripts/                  # Direktorij za Python skripte koje pomažu u administraciji i inicijalizaciji projekta
│   └── seed_database.py      # Skripta za inicijalno popunjavanje baze podataka s testnim podacima (seed)
│
├── templates/                # Globalni direktorij za HTML predloške
│   ├── base.html             # Osnovni HTML predložak za aplikaciju
│   ├── users/
│   │   └── user_list.html    # Predložak za prikaz korisnika
│   ├── products/
│   │   └── product_list.html # Predložak za prikaz proizvoda
│   └── offers/
│       └── offer_list.html   # Predložak za prikaz ponuda
│
└── static/                   # Globalni direktorij za statičke datoteke
    ├── css/                  # CSS datoteke
    ├── js/                   # JavaScript datoteke
    └── images/               # Slike
```

#### Koraci:
1. Klonirajte repozitorij:
   ```bash
   git clone https://github.com/vaše-korisničko-ime/parcijalni-ispit.git
   cd parcijalni-ispit
   ```

2. Kreirajte virtualno okruženje:
   ```bash
   python -m venv venv
   ```

3. Aktivirajte virtualno okruženje:
   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. Instalirajte potrebne module:
   ```bash
   pip install -r requirements.txt
   ```

5. Pokrenite migracije:
   ```bash
   python manage.py migrate
   ```

6. Kreirajte administratorski račun:
   ```bash
   python manage.py createsuperuser
   ```

7. Popunite bazu podataka:
   ```bash
   python manage.py runscript seed_database
   ```

8. Pokrenite razvojni server:
   ```bash
   python manage.py runserver
   ```
   - Aplikaciju otvorite u pregledniku na adresi: `http://127.0.0.1:8000`.

---

### 3. **Zadaci za implementaciju**
Dodajte novu Django aplikaciju **customers** za rad s podacima o tvrtkama (kupcima). 
- **Model Customer**:
  - `name` (ime tvrtke)
  - `vat_id` (OIB tvrtke)
  - `street` (ulica)
  - `city` (grad)
  - `country` (država)
  
Ažurirajte postojeće modele i funkcionalnosti:
- **Offer**:
  - Korisnik (`User`) sada predstavlja osobu koja je kreirala ponudu.
  - Kupac (`Customer`) je tvrtka za koju je ponuda napravljena.
- Implementirajte:
  - Kreiranje novih kupaca.
  - Ažuriranje postojećih kupaca.
  - Prikaz svih kupaca u tablici.
  - Omogućite odabir kupca prilikom kreiranja ponude.

---

### **Dodatne Upute**
- Nemojte mijenjati ostale dijelove aplikacije. Prilagodite svoje rješenje aplikaciji, a ne obrnuto.
- Koristite `TypeHints` prema uputama u komentarima kako biste osigurali konzistentnost tipova podataka.

---

## **Podnošenje Rješenja**

1. Napravite **commit** za sve promjene koristeći opciju:
   ```bash
   git commit -am "Implementacija zadatka"
   ```

2. Pushajte promjene na GitHub:
   ```bash
   git push
   ```

3. Podijelite repozitorij s predavačem:
   - Otvorite vaš repozitorij na GitHubu.
   - Kliknite na **Settings**.
   - Pronađite opciju **Collaborators** i dodajte predavača kao **Contributor**.
   - Unesite korisničko ime predavača i pošaljite pozivnicu.

**VAŽNO:** Provjerite da su sve promjene commitane i pushane prije dodavanja predavača.

**Sretno!**