from cryptography.fernet import Fernet #fernet sluzy do szyfrowania i odszyfrowania
import sys

#sprawdzenie argumentów
if len(sys.argv) != 3:
    print("Użycie: python encrypt.py <plik_do_zaszyfrowania> <plik_z_kluczem>")
    sys.exit(1)

plik = sys.argv[1]
plik_klucz = sys.argv[2]

#gnerowanie losowego klucza symetrycznego AES (base64)
klucz = Fernet.generate_key()
#zapisanie wygenerowanego klucza
with open(plik_klucz, 'wb') as f:
    f.write(klucz)

#wczytanie danych
with open(plik, 'rb') as f:
    dane = f.read()
#przygotowanie narzedzia do szyfrowania
fernet = Fernet(klucz)
#szyfrowanie danych z pliku
dane_zaszyfrowane = fernet.encrypt(dane)
#zapisanie zaszyfrowanej tresci
with open(plik + '.enc', 'wb') as f:
    f.write(dane_zaszyfrowane)

print(f"Plik zaszyfrowany jako {plik}.enc")
print(f"Klucz zapisany w {plik_klucz}")
