import hashlib
import rsa

#funkcja generująca parę kluczy RSA (prywatny i publiczny)
def generate_keys():
    # Generujemy klucze 2048-bitowe RSA
    (public_key, private_key) = rsa.newkeys(2048)
    return public_key, private_key

#funkcja podpisująca plik przy pomocy klucza prywatnego
def sign_file(file_path, private_key):
    # Odczytujemy zawartość pliku w trybie binarnym
    with open(file_path, 'rb') as f:
        file_data = f.read()

    #tworzymy skrót SHA-256 z zawartości pliku
    file_hash = hashlib.sha256(file_data).digest()

    #podpisujemy skrót kluczem prywatnym RSA
    signature = rsa.sign(file_hash, private_key, 'SHA-256')

    return signature

#fuunkcja zapisująca podpis do pliku
def save_signature(signature, signature_file):
    with open(signature_file, 'wb') as f:
        f.write(signature)

#funkcja weryfikująca podpis pliku za pomocą klucza publicznego
def verify_signature(file_path, signature_file, public_key):
    with open(file_path, 'rb') as f:
        file_data = f.read()

    with open(signature_file, 'rb') as f:
        signature = f.read()

    file_hash = hashlib.sha256(file_data).digest()

    try:
        #sprawdzamy czy podpis jest poprawny
        rsa.verify(file_hash, signature, public_key)
        print("Podpis jest poprawny.")
        return True
    except rsa.VerificationError:
        print("Podpis jest niepoprawny!")
        return False

#użycie skryptu
if __name__ == "__main__":
    #generujemy parę kluczy 
    pub_key, priv_key = generate_keys()

    #ścieżka do pliku, który chcemy podpisać
    plik_do_podpisu = "do_podpisu.txt"
    #ścieżka do pliku, gdzie zapiszemy podpis
    plik_podpisu = "plik_do_podpisu.sig"

    #tworzymy podpis cyfrowy pliku
    podpis = sign_file(plik_do_podpisu, priv_key)

    #zapisujemy podpis do pliku
    save_signature(podpis, plik_podpisu)

    #weryfikujemy podpis 
    verify_signature(plik_do_podpisu, plik_podpisu, pub_key)
