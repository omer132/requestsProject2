import requests

site = "google.com"

def check_url(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass 

with open("enterSearchWord.txt") as file:
    for kkk in file:
        kkk = kkk.strip()
        url = "http://" + kkk + "." + site  # Düzgün protokol kullanımı
        response = check_url(url)  # Fonksiyon ismi değiştirildi
        if response:
            print(f"Bulundu: {url}")
        else:
            print(f"Bulunamadı: {url}")
