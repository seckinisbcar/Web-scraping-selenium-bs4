
#İlgili kütüphaneler içe aktarılır.
import requests
from bs4 import BeautifulSoup
import time
import os
import shutil

# "hedef_klasor" değişkeni oluşturularak hedef klasörün yolu belirlenir.
hedef_klasor = "C:\\Users\\se\\Desktop\\py\\hedef_klasor"

# Hedef klasörü oluşturun (varsa önce silin)
if os.path.exists(hedef_klasor):
    shutil.rmtree(hedef_klasor) #Eğer hedef klasör mevcutsa, klasör önce silinir (shutil.rmtree(hedef_klasor)).
os.makedirs(hedef_klasor) #Ardından, hedef klasör oluşturulur (os.makedirs(hedef_klasor)).

#Dosya yolu belirlenir ve L1.txt dosyası okunur.
file_path = "C:\\Users\\se\\Desktop\\py\\L1.txt"
with open(file_path, 'r', encoding="utf-8") as file:
    satirlar = file.readlines()
#Dosyadaki satırlar bir liste olarak satirlar değişkenine atanır.
satir_listesi = []
for satir in satirlar:
    satir_listesi.append(satir.strip())
 

for satir in satir_listesi:
    a12 = satir.strip()#Satırın başındaki ve sonundaki boşluklar temizlenir.
    url = "https:............." + a12 #URL oluşturulur.
    time.sleep(4) #4 saniye bekleme yapılır.
    response = requests.get(url) # Web sayfası alınır ve BeautifulSoup ile analiz edilir.
    soup = BeautifulSoup(response.content, "html.parser")
    diz = soup.find("div", class_="dscrptn").h1.next.next #Belirli bir <div> öğesinin içeriği ve ilgili metinler alınır.
    ad = soup.find("div", class_="dscrptn").h1
    add1 = ad.text
    with open("ad.txt", "a", encoding="utf-8") as dosya: #ad.txt dosyasına ilgili metin yazılır.
        dosya.write(str(add1) + "\n")
    add = str(ad.text) + ".txt" #Dosya adı oluşturulur.
    a = diz.split()[3]
    b = round(int(a)/24) #İlgili web sitesi sayfası  hesaplanır.
    time.sleep(1) #1 saniye bekleme yapılır.

#Sayfa numaraları ve link sabiti belirlenir.
baslangic = 1
bitis = int(b)
link_sabit = url + "?pi="

#Sayfa numarasına göre URL oluşturulur.
for sayfa in range(baslangic, bitis+1): 
    url1 = link_sabit + str(sayfa)
    time.sleep(3)
    response1 = requests.get(url1)
    #Sayfanın içeriği alınır ve BeautifulSoup ile analiz edilir.
    soup1 = BeautifulSoup(response1.content, "html.parser")
    #İlgili <div> öğesi ve içeriği alınır.
    div_element1 = soup1.find("div", class_="srch-prdcts-cntnr")
    div_element = div_element1.find("div", class_="search-store-advs-brand-card")
    H1 = div_element1.prettify()
    #c31.txt dosyasına içerik yazılır.
    with open("c31.txt", "w", encoding="utf-8") as dosya:
        dosya.write(str(H1))
    href_list = []
    #İlgili <div> öğeleri bulunur ve ilgili dosyalara yazılır.
    a_elements = div_element1.find_all("div",class_="p-card-chldrn-cntnr card-border")
    html_doc = str(a_elements)
    soup2 = BeautifulSoup(html_doc, 'html.parser')
    aa = soup2.prettify()
    for link in soup2.find_all('a'):
        ass = link.get('href')      
        with open(os.path.join(hedef_klasor, add), "a", encoding="utf-8") as dosya:
            dosya.write(str(ass) + "\n")
        with open("toplu_link.txt", "a", encoding="utf-8") as dosya:
            dosya.write(str(ass) + "\n")
    #c33.txt dosyasına soup2 içeriği yazılır.
    with open("c33.txt", "w", encoding="utf-8") as dosya:
        dosya.write(str(aa))


