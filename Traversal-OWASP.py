import requests

BASE_URL = "http://localhost:3000"
endpoint = "/ftp/"

#pliki ktore recznie sprawdzilam w przegladarce i wiem ze sa w ftp
files = [
    "acquisitions.md",
    "announcement_encrypted.md",
    "coupons_2013.md.bak",
    "eastere.gg",
    "encrypt.pyc",
    "incident-support.kdbx",
    "legal.md",
    "package.json.bak"
]

headers = {
    "Content-Type": "application/json"
}

for filename in files:
    url = BASE_URL + endpoint + filename
    print(f"Pobieram plik: {url}")
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            print(f"Pobranie udane: {filename}")
            print(response.text[:300])  #wyswietlam fragment pliku aby zobaczyc czy jest w porzadku
        else:
            print(f"Nie udało się pobrać pliku {filename}, status: {response.status_code}")
    except Exception as e:
        print(f"Błąd: {e}")
