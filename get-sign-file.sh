#!/bin/bash

#sprawdzenie czy podano argument
if [ "$#" -ne 1 ]; then
    echo "Użycie: $0 <plik_do_podpisania>"
    exit 1
fi

#stworzenie nazwy pliku wynikowego (sig.- signature)
signature="$1.sig"

#sprawdzanie czy plik private.gem nie istnieje, generowanie kluczy (RSA, dlugosc 2048 bitow)
if [ ! -f private.pem ]; then
    echo "Generowanie klucza prywatnego"
    openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048
    #tworzenie klucza publicznego z prywatnego
    openssl rsa -pubout -in private.pem -out public.pem
fi

#stworzenie skrotu pliku, funkcja skrotu SHA-256, podpisaniem kluczem prywatnym
openssl dgst -sha256 -sign private.pem -out "$signature" "$1"

#sprawdzenie, czy udalo sie podpisac klucz
if [ $? -eq 0 ]; then
    echo "Plik został podpisany cyfrowo jako $signature"
    echo "Tresc podpisu: "
    cat "$signature"
else
    echo "Błąd podczas podpisywania"
fi

