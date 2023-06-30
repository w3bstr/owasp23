import requests
import urllib.parse
import pickle

class ExploitTool:
    def __init__(self):
        self.url = ''
        self.payload = ''
        self.choices = {
            '1': self.perform_injection,
            '2': self.perform_broken_authentication,
            '3': self.perform_sensitive_data_exposure,
            '4': self.perform_xxe,
            '5': self.perform_broken_access_control,
            '6': self.perform_security_misconfiguration,
            '7': self.perform_xss,
            '8': self.perform_insecure_deserialization
        }

    def perform_injection(self):
        response = requests.get(self.url, params={'username': self.payload})
        print(response.text)

    def perform_broken_authentication(self):
        username = input("Kullanıcı adını girin: ")
        password = input("Parolayı girin: ")
        response = requests.post(self.url, data={'username': username, 'password': password})
        print(response.text)

    def perform_sensitive_data_exposure(self):
        token = input("Yetkilendirme tokenını girin: ")
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(self.url, headers=headers)
        print(response.text)

    def perform_xxe(self):
        payload = input("Payload'ı girin: ")
        headers = {'Content-Type': 'application/xml'}
        response = requests.post(self.url, data=payload, headers=headers)
        print(response.text)

    def perform_broken_access_control(self):
        role = input("Rolü girin (admin/user): ")
        cookies = {'role': role}
        response = requests.get(self.url, cookies=cookies)
        print(response.text)

    def perform_security_misconfiguration(self):
        debug_mode = input("Debug modunu açmak için 'true', kapatmak için 'false' girin: ")
        headers = {'X-Debug-Mode': debug_mode}
        response = requests.get(self.url, headers=headers)
        print(response.text)

    def perform_xss(self):
        payload = input("Payload'ı girin: ")
        payload = urllib.parse.quote(payload)
        response = requests.get(self.url, params={'search': payload})
        print(response.text)

    def perform_insecure_deserialization(self):
        serialized_data = input("Serileştirilmiş veriyi girin: ")
        obj = pickle.loads(serialized_data)
        # İşlem yapılacak güvensiz serileştirilmiş nesneyi kullanın
        print(obj)

    def run(self):
        self.print_banner()

        while True:
            print("Açığı seçin:")
            print("1. Injection (Enjeksiyon)")
            print("2. Broken Authentication (Bozuk Kimlik Doğrulama)")
            print("3. Sensitive Data Exposure (Hassas Veri Açığa Çıkması)")
            print("4. XXE (XML External Entities)")
            print("5. Broken Access Control (Bozuk Erişim Kontrolü)")
            print("6. Security Misconfiguration (Güvenlik Yanılandırması)")
            print("7. Cross-Site Scripting (XSS)")
            print("8. Insecure Deserialization (Güvensiz Serileştirme)")
            print("0. Çıkış")
            choice = input("Seçiminizi yapın: ")

            if choice == '0':
                break

            self.url = input("URL'yi girin: ")
            self.choices.get(choice, self.invalid_choice)()

    def print_banner(self):
        print("****************************")
        print("*        OWASP 23          *")
        print("*   Exploit Academy Tool   *")
        print("*   Geliştirici: WebsteR   *")
        print("****************************")
        print()

    def invalid_choice(self):
        print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    tool = ExploitTool()
    tool.run()
