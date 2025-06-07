#!/bin/bash

#nazwa pliku koncowego (.enc oznacza encrypted)
output="$1.enc"

#odczytanie hasla do zaszyfrowania
read -sp "Podaj haslo do zaszyfrowania: " password
echo

#szyfrowanie (algorytm AES, klucz 256-bitowy, tryb CBC), solenie
openssl enc -aes-256-cbc -pbkdf2 -salt -in "$1" -out "$output" -k "$password"

#wyswietlenie wyniku
echo "Plik zostal zaszyfrowany jako $output"
echo
echo "Tresc: " 
cat "$output"
