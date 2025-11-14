# Rejestr zasobow RPi 4

Lekka aplikacja do rejestru zasobów na Raspberry Pi 4 (Tkinter + SQLite). Interfejs w Tkinter z bazą danych w pliku data/inventory.db.

Funkcje
- automatyczne połączenie z bazą SQLite (tworzy tabelę przy pierwszym uruchomieniu)
- podgląd zasobów w tabeli (Treeview)
- dodawanie wpisu
- usuwanie zaznaczonego wpisu
- odświeżanie listy
- edycja istniejącego wpisu
- filtrowanie wpisów po kategorii
- sortowania wpisów według daty dodania (rosnąco/malejąco)
- wyszukiwanie wpisów po części nazwy lub numeru seryjnego
- eksport danych do pliku CSV

Wymagania
- Raspberry Pi 4 z Raspberry Pi OS
- Python 3.x
- Tkinter (python3-tk) i sqlite3
  - sudo apt update
  - sudo apt install -y python3-tk sqlite3
- Tkcalendar
  - sudo apt install python3-pip
  - pip3 install --user tkcalendar
    - w przypadku pojawienia się błędu o zablokowaniu instalacji z powodu błędu o treści "externally-managed-environment" trzeba użyć --break-system-packages
    - UWAGA! Użycie tego łączy się z ryzykiem uszkodzenia instalacji pythona lub całego systemu operacyjnego!
    -  Można obejść ten problem, lecz to będzie wymagało użycia wirtualnego środowiska (venv) i aplikacja będzie dostępna tylko w nim.

Uruchomienie
1) Sklonuj/kopiuj repozytorium na RPi.
2) Upewnij się, że istnieją puste pliki ui/__init__.py i logic/__init__.py (dla importów).
3) Uruchom:
   - python3 main.py

Struktura projektu
```
project_root/
├── data/
│   └── inventory.db        # baza SQLite (tworzona automatycznie)
├── ui/
│   ├── __init__.py
│   └── views.py            # GUI (Tkinter: formularz + tabela)
├── logic/
│   ├── __init__.py
│   └── db.py               # obsługa SQLite
├── main.py                 # punkt startowy aplikacji
└── README.md
```

Dostosowanie pod użytkownika
- Kategorie w Combobox: edytuj listę self.categories w ui/views.py (np. ["Narzędzia", "IT", "Oprogramowanie", "Wyposażenie biurowe", "Transport", "BHP", "Meble", "Inne"]).
- Lokalizacja bazy: zmień ścieżkę w main.py (domyślnie data/inventory.db).