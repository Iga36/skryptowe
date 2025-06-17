import socket  #importujemy moduł socket do komunikacji sieciowej
import sys     #importujemy sys do obsługi argumentów i ewentualnych błędów
from datetime import datetime  #do pomiaru czasu skanowania

#funkcja skanująca porty w zadanym zakresie
def scan_ports(ip, start_port, end_port):
    print(f"Rozpoczynanie skanowania {ip} w zakresie portów {start_port}-{end_port}")

    for port in range(start_port, end_port + 1):  #iterujemy przez każdy port w zadanym zakresie
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #tworzymy socket TCP
        sock.settimeout(1)  #ustawiamy timeout 1 sekunda, żeby nie czekać zbyt długo

        result = sock.connect_ex((ip, port))  # Próbujemy połączyć się z danym portem (zwraca 0 jeśli sukces)
        if result == 0:
            print(f"Port {port} jest OTWARTY")  # Jeśli port jest otwarty, wypisujemy go
        sock.close()  #zamykamy socket

#główna część programu
if __name__ == "__main__":
    #np.: ip = "localhost" lub "127.0.0.1" jeśli OWASP Juice Shop działa lokalnie
    ip = input("Podaj adres IP serwera (np. 127.0.0.1): ")  #pobieramy adres IP od użytkownika

    #pobieramy zakres portów do skanowania
    try:
        start_port = int(input("Podaj początkowy port: "))
        end_port = int(input("Podaj końcowy port: "))
    except ValueError:
        print("Podano nieprawidłowy numer portu. Użyj liczb całkowitych.")
        sys.exit(1)  # kończymy działanie programu jeśli porty nie są poprawne

    #uruchamiamy funkcję skanującą
    scan_ports(ip, start_port, end_port)
