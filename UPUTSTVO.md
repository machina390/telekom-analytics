# Zadatak za praksu: statistička analiza baze korisnika

Dobrodošao/la u Data & AI tim. Sledeće dve nedelje radiš jedan zadatak od početka do kraja: od sirovog CRM izvoza do izveštaja za menadžment. Pitanje na koje odgovaraš glasi: **ko nam odlazi i zašto?**

## Šta je u ovom paketu

| Fajl / folder | Šta je to |
|---|---|
| `telekom_korisnici.xlsx` | Podaci — 1.232 korisnika mobilnih usluga (sheet *Podaci*) i opis svake kolone (sheet *Rečnik_podataka*). Ovaj fajl nikad ne menjaš. |
| `moduli/index.html` | **Ovde počinješ.** Kontekst, plan po danima, kriterijumi ocenjivanja i linkovi ka tri modula sa zadacima. |
| `moduli/modul1.html`, `modul2.html`, `modul3.html` | Zadaci korak po korak, sa skeletonom Python koda, nagoveštajima i očekivanim rezultatima. |
| `prezentacije/P1…P3.pptx` | Teorija koja ti treba pre svakog modula: deskriptivna statistika, priprema podataka, eksplorativna analiza i izveštavanje. |

## Kako da počneš (prvi dan)

1. Raspakuj zip u jedan folder i u njemu napravi podfolder `rezultati/` — tu ide sve što napraviš.
2. Pripremi Python okruženje:
   ```
   python -m venv .venv
   .venv\Scripts\activate          (Windows)   ili   source .venv/bin/activate   (macOS/Linux)
   pip install pandas numpy scipy matplotlib seaborn openpyxl jupyter
   ```
3. Pogledaj prezentaciju `P1_Deskriptivna_statistika.pptx`.
4. Otvori `moduli/index.html` u pregledaču i kreni na Modul 1.

## Plan po danima

| Dan | Šta radiš | Prezentacija |
|---|---|---|
| 1–3 | **Modul 1** — učitavanje, profil kvaliteta podataka, mere centralne tendencije i disperzije (ručno i sa pandas-om), lista sumnjivih stvari | P1 |
| 3 | Kontrolna tačka 1 sa mentorom (15–20 min) | |
| 4–6 | **Modul 2** — čišćenje u osam koraka: kategorije, duplikati, tipovi, datumi, logička pravila, outlieri, imputacija, izvedene kolone | P2 |
| 6 | Kontrolna tačka 2 | |
| 7–9 | **Modul 3** — churn po segmentima, korelacije, tri hipoteze, grafikoni, pisanje izveštaja | P3 |
| 10 | Prezentacija nalaza mentoru: 10 minuta + 10 minuta pitanja | |

## Šta predaješ na kraju

- Tri notebooka koja se izvršavaju od početka do kraja bez greške: `01_profilisanje`, `02_ciscenje`, `03_analiza`
- `rezultati/korisnici_clean.csv` — očišćen dataset
- `rezultati/dnevnik_ciscenja.md` — svaka odluka o čišćenju: šta si našao/la, šta si uradio/la, zašto
- Izveštaj od 3–5 strana (PDF ili Word) i prezentacija do 8 slajdova

## Četiri pravila

1. Sirovi fajl se ne menja — svaka transformacija je u kodu i ponovljiva.
2. Excel je za gledanje; računanje je u Pythonu.
3. Svaku odluku o čišćenju zapiši sa obrazloženjem. Ko čita dnevnik treba da može da ponovi tvoj rad.
4. Ako zapneš — pitaj mentora, ali tek pošto možeš da kažeš šta si probao/la.

## Kako se ocenjuje

Profilisanje i mere 20 · Kvalitet čišćenja 25 · Analiza i interpretacija 25 · Vizuelizacije 10 · Izveštaj i prezentacija 20. Prag za uspešno završen zadatak je 70 od 100. Bonus 5 bodova ako pronađeš klasu greške u podacima koja nije pomenuta ni u jednom modulu. Detalji su na `moduli/index.html`.
